import csv
import datetime
import json
import time
from os.path import expanduser, exists
from pprint import pprint
from zipfile import ZipFile

import numpy as np
from keras import backend as K, optimizers
from keras.callbacks import ModelCheckpoint
from keras.layers import Embedding, Dense, Merge, BatchNormalization, TimeDistributed, Lambda, LSTM, SimpleRNN, Dropout
from keras.models import Sequential
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
from keras.utils.data_utils import get_file
from sklearn.model_selection import train_test_split
from helper import WordNet_44_categories, GR_19_categories, POS_15_categories, lst_2_dic, sequence_from_dic


KERAS_DATASETS_DIR = expanduser('~/.keras/datasets/')
TRAIN_JSON_FILE = 'data/train4134.json'
TRAIN_LABEL_JSON_FILE = 'data/train4134_label.json'
TEST_JSON_FILE = 'data/test200.json'
TEST_LABEL_JSON_FILE = 'data/test200_label.json'
GLOVE_ZIP_FILE_URL = 'http://nlp.stanford.edu/data/glove.840B.300d.zip'
GLOVE_ZIP_FILE = 'glove.840B.300d.zip'
GLOVE_FILE = 'glove.840B.300d.txt'
WORD_EMBEDDING_MATRIX_FILE = 'word_embedding_matrix.npy'
MAX_NB_WORDS = 200000
MAX_SEQUENCE_LENGTH = 25
EMBEDDING_DIM = 300
POS_EMBEDDING_DIM = 50
GR_EMBEDDING_DIM = 50
WN_EMBEDDING_DIM = 50
MODEL_WEIGHTS_FILE = 'sdp_weights.h5'
VALIDATION_SPLIT = 0.1
TEST_SPLIT = 0.1
RNG_SEED = 13371447
NB_EPOCHS = 25
np.random.seed(RNG_SEED)

train_leftW = []
train_leftGR = []
train_leftPOS = []
train_leftWN = []

train_rightW = []
train_rightGR = []
train_rightPOS = []
train_rightWN = []

train_labels = []

test_leftW = []
test_leftGR = []
test_leftPOS = []
test_leftWN = []

test_rightW = []
test_rightGR = []
test_rightPOS = []
test_rightWN = []

test_labels = []

with open(TRAIN_JSON_FILE, encoding='utf-8') as train_file, \
        open(TRAIN_LABEL_JSON_FILE, encoding='utf-8') as train_label_file, \
        open(TEST_JSON_FILE, encoding='utf-8') as test_file, \
        open(TEST_LABEL_JSON_FILE, encoding='utf-8') as test_label_file:
    train_data = json.load(train_file)
    train_label_data = json.load(train_label_file)
    test_data = json.load(test_file)
    test_label_data = json.load(test_label_file)

for idx, data in enumerate(train_data):
    train_leftW.append(' '.join(data[4]))
    train_rightW.append(' '.join(data[5]))
    train_leftPOS.append(data[6])
    train_rightPOS.append(data[7])
    train_leftGR.append(data[8])
    train_rightGR.append(data[9])
    train_leftWN.append(data[10])
    train_rightWN.append(data[11])
    train_labels.append(train_label_data[idx])

for idx, data in enumerate(test_data):
    test_leftW.append(' '.join(data[4]))
    test_rightW.append(' '.join(data[5]))
    test_leftPOS.append(data[6])
    test_rightPOS.append(data[7])
    test_leftGR.append(data[8])
    test_rightGR.append(data[9])
    test_leftWN.append(data[10])
    test_rightWN.append(data[11])
    test_labels.append(test_label_data[idx])

print('Train numbers: %d' % len(train_data))
print('Test numbers %d' % len(test_data))

all_text = train_leftW + train_rightW + test_leftW + test_rightW
tokenizer = Tokenizer(num_words=MAX_NB_WORDS)
tokenizer.fit_on_texts(all_text)
train_leftW_word_sequences = tokenizer.texts_to_sequences(train_leftW)
train_rightW_word_sequences = tokenizer.texts_to_sequences(train_rightW)
test_leftW_word_sequences = tokenizer.texts_to_sequences(test_leftW)
test_rightW_word_sequences = tokenizer.texts_to_sequences(test_rightW)
word_index = tokenizer.word_index

print("Words in index: %d" % len(word_index))
nb_words = min(MAX_NB_WORDS, len(word_index))

pos_dic = lst_2_dic(POS_15_categories)
gr_dic = lst_2_dic(GR_19_categories)
wn_dic = lst_2_dic(WordNet_44_categories)
nb_pos = len(pos_dic)
nb_gr = len(gr_dic)
nb_wn = len(wn_dic)

train_leftPOS_word_sequences = sequence_from_dic(train_leftPOS, pos_dic)
train_rightPOS_word_sequences = sequence_from_dic(train_rightPOS, pos_dic)
test_leftPOS_word_sequences = sequence_from_dic(test_leftPOS, pos_dic)
test_rightPOS_word_sequences = sequence_from_dic(test_rightPOS, pos_dic)

train_leftGR_word_sequences = sequence_from_dic(train_leftGR, gr_dic)
train_rightGR_word_sequences = sequence_from_dic(train_rightGR, gr_dic)
test_leftGR_word_sequences = sequence_from_dic(test_leftGR, gr_dic)
test_rightGR_word_sequences = sequence_from_dic(test_rightGR, gr_dic)

train_leftWN_word_sequences = sequence_from_dic(train_leftWN, wn_dic)
train_rightWN_word_sequences = sequence_from_dic(train_rightWN, wn_dic)
test_leftWN_word_sequences = sequence_from_dic(test_leftWN, wn_dic)
test_rightWN_word_sequences = sequence_from_dic(test_rightWN, wn_dic)

if exists(WORD_EMBEDDING_MATRIX_FILE):
    word_embedding_matrix = np.load(open(WORD_EMBEDDING_MATRIX_FILE, 'rb'))
else:
    if not exists(KERAS_DATASETS_DIR + GLOVE_FILE):
        zipfile = ZipFile(get_file(GLOVE_ZIP_FILE, GLOVE_ZIP_FILE_URL))
        zipfile.extract(GLOVE_FILE, path=KERAS_DATASETS_DIR)

    print("Processing", GLOVE_FILE)

    embeddings_index = {}
    with open(KERAS_DATASETS_DIR + GLOVE_FILE, encoding='utf-8') as f:
        for line in f:
            values = line.split(' ')
            word = values[0]
            embedding = np.asarray(values[1:], dtype='float32')
            embeddings_index[word] = embedding

    print('Word embeddings: %d' % len(embeddings_index))

    word_embedding_matrix = np.zeros((nb_words + 1, EMBEDDING_DIM))
    for word, i in word_index.items():
        if i > MAX_NB_WORDS:
            continue
        embedding_vector = embeddings_index.get(word)
        if embedding_vector is not None:
            word_embedding_matrix[i] = embedding_vector

print('Null word embeddings: %d' % np.sum(np.sum(word_embedding_matrix, axis=1) == 0))

train_leftW_data = pad_sequences(train_leftW_word_sequences, maxlen=MAX_SEQUENCE_LENGTH)
train_rightW_data = pad_sequences(train_rightW_word_sequences, maxlen=MAX_SEQUENCE_LENGTH)
test_leftW_data = pad_sequences(test_leftW_word_sequences, maxlen=MAX_SEQUENCE_LENGTH)
test_rightW_data = pad_sequences(test_rightW_word_sequences, maxlen=MAX_SEQUENCE_LENGTH)

train_leftPOS_data = pad_sequences(train_leftPOS_word_sequences, maxlen=MAX_SEQUENCE_LENGTH)
train_rightPOS_data = pad_sequences(train_rightPOS_word_sequences, maxlen=MAX_SEQUENCE_LENGTH)
test_leftPOS_data = pad_sequences(test_leftPOS_word_sequences, maxlen=MAX_SEQUENCE_LENGTH)
test_rightPOS_data = pad_sequences(test_rightPOS_word_sequences, maxlen=MAX_SEQUENCE_LENGTH)

train_leftGR_data = pad_sequences(train_leftGR_word_sequences, maxlen=MAX_SEQUENCE_LENGTH)
train_rightGR_data = pad_sequences(train_rightGR_word_sequences, maxlen=MAX_SEQUENCE_LENGTH)
test_leftGR_data = pad_sequences(test_leftGR_word_sequences, maxlen=MAX_SEQUENCE_LENGTH)
test_rightGR_data = pad_sequences(test_rightGR_word_sequences, maxlen=MAX_SEQUENCE_LENGTH)

train_leftWN_data = pad_sequences(train_leftWN_word_sequences, maxlen=MAX_SEQUENCE_LENGTH)
train_rightWN_data = pad_sequences(train_rightWN_word_sequences, maxlen=MAX_SEQUENCE_LENGTH)
test_leftWN_data = pad_sequences(test_leftWN_word_sequences, maxlen=MAX_SEQUENCE_LENGTH)
test_rightWN_data = pad_sequences(test_rightWN_word_sequences, maxlen=MAX_SEQUENCE_LENGTH)
print(test_rightWN_data[0])

train_label_data = np.array(train_labels, dtype=int)
test_label_data = np.array(test_labels, dtype=int)

print('Shape of train_leftW data tensor:', train_leftW_data.shape)
print('Shape of train_rightPOS data tensor:', train_rightPOS_data.shape)
print('Shape of label tensor:', train_label_data.shape)

np.save(WORD_EMBEDDING_MATRIX_FILE, word_embedding_matrix)

# X = np.stack((q1_data, q2_data), axis=1)
# y = labels
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=TEST_SPLIT, random_state=RNG_SEED)
# Q1_train = X_train[:, 0]
# Q2_train = X_train[:, 1]
# Q1_test = X_test[:, 0]
# Q2_test = X_test[:, 1]

LeftW = Sequential()
LeftW.add(Embedding(nb_words + 1, EMBEDDING_DIM, weights=[word_embedding_matrix], input_length=MAX_SEQUENCE_LENGTH,
                 trainable=False, mask_zero=True))
LeftW.add(LSTM(EMBEDDING_DIM, activation='relu', return_sequences=True, dropout=0.5, recurrent_dropout=0.5))
LeftW.add(Lambda(lambda x: K.max(x, axis=1), output_shape=(EMBEDDING_DIM,)))

RightW = Sequential()
RightW.add(Embedding(nb_words + 1, EMBEDDING_DIM, weights=[word_embedding_matrix], input_length=MAX_SEQUENCE_LENGTH,
                 trainable=False, mask_zero=True))
RightW.add(LSTM(EMBEDDING_DIM, activation='relu', return_sequences=True, dropout=0.5, recurrent_dropout=0.5))
RightW.add(Lambda(lambda x: K.max(x, axis=1), output_shape=(EMBEDDING_DIM,)))

LeftPOS = Sequential()
LeftPOS.add(Embedding(nb_pos + 1, POS_EMBEDDING_DIM, input_length=MAX_SEQUENCE_LENGTH))
LeftPOS.add(LSTM(POS_EMBEDDING_DIM, activation='relu', return_sequences=True, dropout=0.35, recurrent_dropout=0.35))
LeftPOS.add(Lambda(lambda x: K.max(x, axis=1), output_shape=(POS_EMBEDDING_DIM,)))

RightPOS = Sequential()
RightPOS.add(Embedding(nb_pos + 1, POS_EMBEDDING_DIM, input_length=MAX_SEQUENCE_LENGTH))
RightPOS.add(LSTM(POS_EMBEDDING_DIM, activation='relu', return_sequences=True, dropout=0.35, recurrent_dropout=0.35))
RightPOS.add(Lambda(lambda x: K.max(x, axis=1), output_shape=(POS_EMBEDDING_DIM,)))

LeftGR = Sequential()
LeftGR.add(Embedding(nb_gr + 1, GR_EMBEDDING_DIM, input_length=MAX_SEQUENCE_LENGTH))
LeftGR.add(LSTM(GR_EMBEDDING_DIM, activation='relu', return_sequences=True, dropout=0.3, recurrent_dropout=0.3))
LeftGR.add(Lambda(lambda x: K.max(x, axis=1), output_shape=(GR_EMBEDDING_DIM,)))

RightGR = Sequential()
RightGR.add(Embedding(nb_gr + 1, GR_EMBEDDING_DIM, input_length=MAX_SEQUENCE_LENGTH))
RightGR.add(LSTM(GR_EMBEDDING_DIM, activation='relu', return_sequences=True, dropout=0.3, recurrent_dropout=0.3))
RightGR.add(Lambda(lambda x: K.max(x, axis=1), output_shape=(GR_EMBEDDING_DIM,)))

LeftWN = Sequential()
LeftWN.add(Embedding(nb_wn + 1, WN_EMBEDDING_DIM, input_length=MAX_SEQUENCE_LENGTH))
LeftWN.add(LSTM(WN_EMBEDDING_DIM, activation='relu', return_sequences=True, dropout=0.35, recurrent_dropout=0.35))
LeftWN.add(Lambda(lambda x: K.max(x, axis=1), output_shape=(WN_EMBEDDING_DIM,)))

RightWN = Sequential()
RightWN.add(Embedding(nb_wn + 1, WN_EMBEDDING_DIM, input_length=MAX_SEQUENCE_LENGTH))
RightWN.add(LSTM(WN_EMBEDDING_DIM, activation='relu', return_sequences=True, dropout=0.35, recurrent_dropout=0.35))
RightWN.add(Lambda(lambda x: K.max(x, axis=1), output_shape=(WN_EMBEDDING_DIM,)))


model = Sequential()
model.add(Merge([LeftW, RightW, LeftPOS, RightPOS, LeftGR, RightGR, LeftWN, RightWN], mode='concat'))
model.add(BatchNormalization())
model.add(Dropout(0.15))
model.add(Dense(100, activation='relu'))
model.add(BatchNormalization())
model.add(Dense(1, activation='sigmoid'))
sgd = optimizers.SGD(lr=0.001, decay=1e-5, momentum=0.9, nesterov=True)

model.compile(loss='binary_crossentropy',
              optimizer=sgd,
              metrics=['accuracy'])

callbacks = [ModelCheckpoint(MODEL_WEIGHTS_FILE, monitor='val_acc', save_best_only=True)]

print("Starting training at", datetime.datetime.now())

t0 = time.time()
history = model.fit([train_leftW_data, train_rightW_data, train_leftPOS_data, train_rightPOS_data,
                     train_leftGR_data, train_rightGR_data, train_leftWN_data, train_rightWN_data],
                    train_label_data,
                    epochs=NB_EPOCHS,
                    validation_split=VALIDATION_SPLIT,
                    verbose=1,
                    callbacks=callbacks)
t1 = time.time()

print("Training ended at", datetime.datetime.now())

print("Minutes elapsed: %f" % ((t1 - t0) / 60.))

model.load_weights(MODEL_WEIGHTS_FILE)
loss, accuracy = model.evaluate([test_leftW_data, test_rightW_data, test_leftPOS_data, test_rightPOS_data,
                                 test_leftGR_data, test_rightGR_data, test_leftWN_data, test_rightWN_data],
                                test_label_data)

print('')
print('loss      = {0:.4f}'.format(loss))
print('accuracy  = {0:.4f}'.format(accuracy))


# print('precision = {0:.4f}'.format(precision))
# print('recall    = {0:.4f}'.format(recall))
# print('F         = {0:.4f}'.format(fbeta_score))
