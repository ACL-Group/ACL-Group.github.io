import csv
import datetime
import json
import os
import time
import pickle
import gc

from os.path import expanduser, exists
from pprint import pprint
from zipfile import ZipFile
import numpy as np

from sklearn.metrics import f1_score, accuracy_score, roc_auc_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from keras import backend as K, optimizers
from keras.callbacks import ModelCheckpoint, EarlyStopping
from keras.layers import Embedding, Dense, Merge, BatchNormalization, TimeDistributed, Lambda, LSTM, SimpleRNN, Dropout, \
    Input, Bidirectional, GRU, Convolution1D
from keras.models import Sequential
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer, text_to_word_sequence
from keras.utils.data_utils import get_file
from helper import WordNet_44_categories, GR_19_categories, POS_15_categories, lst_2_dic, sequence_from_dic, \
    train_val_test_split
from keras.utils import plot_model


RNG_SEED = 1337
np.random.seed(RNG_SEED)

KERAS_DATASETS_DIR = expanduser('~/.keras/datasets/')
SENNA_EMD_FILE = '/home/frank/relation/embedding/senna/embeddings/merged_embeddings.txt'
SRL_EMD_FILE = 'data/EMD/out_51k_50_corpus.emd'
LEMMA_EMD_FILE = 'data/EMD/96w_corpus.emd'
CORPUS_EMD_FILE = 'data/EMD/all_50.emd'
GLOVE_EMD_FILE = 'data/EMD/glove.6B.100d.txt'
LABELED_FILE = 'data/ORIG/label5000.txt'
NORM_FILE = 'data/NORM/label5000.norm_termab'
LEMMA_FILE = 'data/LEM/label5000.lemma'
COMPRESSED_NORM_TERMAB_FILE = 'data/COMPRESSED/label5000.compressed_norm_termab'

WORD_EMBEDDING_MATRIX_FILE = 'word_embedding_matrix.npy'
MAX_NB_WORDS = 20000
MAX_SEQUENCE_LENGTH = 40
EMBEDDING_DIM = 100
POS_EMBEDDING_DIM = 5
MODEL_WEIGHTS_FILE = 'lstm5k_weights.h5'
VALIDATION_SPLIT = 0.25
TEST_SPLIT = 0.2
NB_EPOCHS = 40

all_text_data = []
labels = []
lemma_sentences = []
position_a_seqs = []
position_b_seqs = []
sentences = []
srl_sentences = []
norm_sentences = []
postag_list = []
terma_list = []
termb_list = []

# load all text for tokenizer
#
DIR_NAME = '/home/frank/relation/dataset/gutenberg/pair_sentences/norm_sent_termab'
for filename in os.listdir(DIR_NAME):
    if filename.endswith('.norm_termab'):
        file = os.path.join(DIR_NAME, filename)
        for line in open(file, encoding='utf-8'):
            all_text_data.append(line.strip())

with open(LABELED_FILE, encoding='utf-8') as labeled_file, \
        open(NORM_FILE, encoding='utf-8') as norm_file:
    for line1, line2 in zip(labeled_file, norm_file):
        ls1 = line1.strip().split('\t')
        terma_list.append(ls1[2])
        termb_list.append(ls1[3])
        labels.append(ls1[4])
        norm_sentences.append(line2.strip())

tokenizer = Tokenizer(num_words=MAX_NB_WORDS)
tokenizer.fit_on_texts(all_text_data + norm_sentences)
pickle.dump(tokenizer, open('tokenizer.pk', 'wb'))
exit(0)
word_sequences = tokenizer.texts_to_sequences(norm_sentences)
word_index = tokenizer.word_index

# calculate position sequences
terma_index = word_index['terma']
termb_index = word_index['termb']
for idx, sent in enumerate(word_sequences):
    position_a = sent.index(terma_index)
    position_b = sent.index(termb_index)
    position_a_seqs.append(' '.join([str(i - position_a) for i in range(len(sent))]))
    position_b_seqs.append(' '.join([str(i - position_b) for i in range(len(sent))]))


seq_tokenizer = Tokenizer(num_words=MAX_NB_WORDS, filters='')
seq_tokenizer.fit_on_texts(position_a_seqs + position_b_seqs)
position_a_seqs = seq_tokenizer.texts_to_sequences(position_a_seqs)
position_b_seqs = seq_tokenizer.texts_to_sequences(position_b_seqs)
pos_index = seq_tokenizer.word_index

print("Words in index: %d" % len(word_index))
nb_words = min(MAX_NB_WORDS, len(word_index))
print("Positions in index: %d" % len(pos_index))
nb_pos = min(MAX_NB_WORDS, len(pos_index))

embeddings_index = {}
with open(GLOVE_EMD_FILE, encoding='utf-8') as f:
    for line in f:
        values = line.split(' ')
        word = values[0]
        embedding = np.asarray(values[1:], dtype='float32')
        embeddings_index[word] = embedding

print('Total Word embeddings: %d' % len(embeddings_index))
#
word_embedding_matrix = np.zeros((nb_words + 1, EMBEDDING_DIM))
for word, i in word_index.items():
    if i > MAX_NB_WORDS:
        continue
    embedding_vector = embeddings_index.get(word)
    if embedding_vector is not None:
        word_embedding_matrix[i] = embedding_vector

print('Null word embeddings: %d' % np.sum(np.sum(word_embedding_matrix, axis=1) == 0))
# np.save(WORD_EMBEDDING_MATRIX_FILE, word_embedding_matrix)

# assert len(word_sequences) == len(position_a_seqs)
# assert len(position_a_seqs) == len(position_b_seqs)
# assert len(position_b_seqs) == len(labels)
# assert len(labels) == len(terma_list)
# assert len(terma_list) == len(termb_list)

word_sequences = pad_sequences(word_sequences, maxlen=MAX_SEQUENCE_LENGTH)
position_a_seqs = pad_sequences(position_a_seqs, maxlen=MAX_SEQUENCE_LENGTH)
position_b_seqs = pad_sequences(position_b_seqs, maxlen=MAX_SEQUENCE_LENGTH)
terma_vectors = np.array([embeddings_index[word] for word in terma_list])
termb_vectors = np.array([embeddings_index[word] for word in termb_list])
termab_vectors = np.concatenate((terma_vectors, termb_vectors), axis=1)
labels = np.array(labels, dtype=int)

# X = np.stack((word_sequences, position_a_seqs, position_b_seqs), axis=1)

X_train, X_test, termab_train, termab_test, y_train, y_test, \
position_a_train, position_a_test, position_b_train, position_b_test = train_test_split(word_sequences, termab_vectors,
                                                                                        labels, position_a_seqs,
                                                                                        position_b_seqs,
                                                                                        stratify=labels, test_size=1000,
                                                                                        random_state=RNG_SEED)
# X_train, X_val, X_test = train_val_test_split(word_sequences, id_file=TRAIN_VAL_TEST_ID_FILE)
# termab_train, termab_val, termab_test = train_val_test_split(termab_vectors, id_file=TRAIN_VAL_TEST_ID_FILE)
# y_train, y_val, y_test = train_val_test_split(labels, id_file=TRAIN_VAL_TEST_ID_FILE)

print(termab_train.shape)
print('Shape of train data tensor:', X_train.shape)
# print('Shape of val data tensor:', X_val.shape)
print('Shape of test tensor:', X_test.shape)

# word_embedding_matrix = np.zeros((nb_words + 1, EMBEDDING_DIM))
# position_embedding_matrix = np.zeros((nb_pos + 1, POS_EMBEDDING_DIM))

W = Sequential()
W.add(Embedding(nb_words + 1, EMBEDDING_DIM, weights=[word_embedding_matrix], trainable=True))
# W.add(Dropout(0.2))
W.add(BatchNormalization())

POS1 = Sequential()
POS1.add(Embedding(nb_pos + 1, POS_EMBEDDING_DIM, trainable=True))
POS1.add(BatchNormalization())

POS2 = Sequential()
POS2.add(Embedding(nb_pos + 1, POS_EMBEDDING_DIM, trainable=True))
POS2.add(BatchNormalization())


model_LSTM = Sequential()
# model_LSTM.add(W)
model_LSTM.add(Merge([W, POS1, POS2], mode='concat'))
# model_LSTM.add(Convolution1D(60, kernel_size=3, padding="valid", activation="relu",))
# model_LSTM.add(Convolution1D(60, kernel_size=8, padding="valid", activation="relu",))

# model_LSTM.add(LSTM(60, dropout=0.5, recurrent_dropout=0.5, return_sequences=True))
# model_LSTM.add(LSTM(60, dropout=0.5, recurrent_dropout=0.5, return_sequences=True))
model_LSTM.add(LSTM(100, dropout=0.5, recurrent_dropout=0.5))

model_LSTM.add(BatchNormalization())

termab = Sequential()
termab.add(BatchNormalization(input_shape=(200,)))
termab.add(Dense(100, activation='relu'))

model = Sequential()
model.add(Merge([model_LSTM, termab], mode='concat'))
model.add(BatchNormalization())
# model.add(Dense(50, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

sgd = optimizers.SGD(lr=0.1, decay=1e-5, momentum=0.9, nesterov=True)
adam = optimizers.Adam()

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

callbacks = [ModelCheckpoint(MODEL_WEIGHTS_FILE, monitor='val_acc', save_best_only=True),
             EarlyStopping(monitor='val_acc', patience=10)]

print("Starting training at", datetime.datetime.now())

t0 = time.time()
history = model.fit([X_train, position_a_train, position_b_train, termab_train], y_train,
                    epochs=NB_EPOCHS,
                    validation_split=0.2,
                    # validation_data=([X_val, termab_val], y_val),
                    batch_size=128,
                    verbose=1,
                    callbacks=callbacks)
t1 = time.time()

print("Training ended at", datetime.datetime.now())

print("Minutes elapsed: %f" % ((t1 - t0) / 60.))

model.load_weights(MODEL_WEIGHTS_FILE)
y_pred1 = model.predict_classes([X_test, position_a_test, position_b_test, termab_test], batch_size=500)
y_proba = model.predict_proba([X_test, position_a_test, position_b_test, termab_test], batch_size=500)

print('Acc:', accuracy_score(y_test, y_pred1))
print('precision', precision_score(y_test, y_pred1))
print('recall_score', recall_score(y_test, y_pred1))
print('F:', f1_score(y_test, y_pred1))
print('AUC', roc_auc_score(y_test, y_proba))
plot_model(model, to_file='model.png', show_shapes=True)

print('\n\n')
y_pred_train = model.predict_classes([X_train, position_a_train, position_b_train, termab_train], batch_size=500)
print('Acc:', accuracy_score(y_train, y_pred_train))
print('precision', precision_score(y_train, y_pred_train))
print('recall_score', recall_score(y_train, y_pred_train))
print('F:', f1_score(y_train, y_pred_train))
