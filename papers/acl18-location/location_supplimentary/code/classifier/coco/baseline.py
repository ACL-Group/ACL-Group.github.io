import csv
import datetime
import json
import time
from os.path import expanduser, exists
from zipfile import ZipFile

import numpy as np
from keras import backend as K
from keras.callbacks import ModelCheckpoint
from keras.layers import Embedding, Dense, Merge, BatchNormalization, TimeDistributed, Lambda
from keras.models import Sequential
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
from keras.utils.data_utils import get_file
from sklearn.model_selection import train_test_split

KERAS_DATASETS_DIR = expanduser('~/.keras/datasets/')
POS_PAIRS_FILE = 'pos_count.txt'
NEG_PAIRS_FILE = 'neg_pair.txt'
GLOVE_ZIP_FILE_URL = 'http://nlp.stanford.edu/data/glove.840B.300d.zip'
GLOVE_ZIP_FILE = 'glove.840B.300d.zip'
GLOVE_FILE = 'glove.840B.300d.txt'
W1_TRAINING_DATA_FILE = 'w1_train.npy'
W2_TRAINING_DATA_FILE = 'w2_train.npy'
LABEL_TRAINING_DATA_FILE = 'label_train.npy'
NB_WORDS_DATA_FILE = 'nb_words.json'
MAX_NB_WORDS = 200000
MAX_SEQUENCE_LENGTH = 25
EMBEDDING_DIM = 300
MODEL_WEIGHTS_FILE = 'word_pairs_weights.h5'
VALIDATION_SPLIT = 0.1
TEST_SPLIT = 0.3
RNG_SEED = 13371447
NB_EPOCHS = 25

if exists(W1_TRAINING_DATA_FILE) and exists(W2_TRAINING_DATA_FILE) and exists(LABEL_TRAINING_DATA_FILE):
    w1_data = np.load(open(W1_TRAINING_DATA_FILE, 'rb'))
    w2_data = np.load(open(W2_TRAINING_DATA_FILE, 'rb'))
    labels = np.load(open(LABEL_TRAINING_DATA_FILE, 'rb'))

else:
    print("Data Pre-Processing")

    word1 = []
    word2 = []
    is_location = []
    with open(POS_PAIRS_FILE, encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        for row in reader:
            word1.append(row[0])
            word2.append(row[1])
            is_location.append(1)

    with open(NEG_PAIRS_FILE, encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        for row in reader:
            word1.append(row[0])
            word2.append(row[1])
            is_location.append(0)
    print('Word pairs: %d' % len(word1))

    if not exists(KERAS_DATASETS_DIR + GLOVE_ZIP_FILE):
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

    w1_data = []
    w2_data = []
    for w in word1:
        w1_data.append(embeddings_index[w])
    for w in word2:
        w2_data.append(embeddings_index[w])
    w1_data = np.array(w1_data)
    w2_data = np.array(w2_data)
    labels = np.array(is_location, dtype=int)

    print('Shape of word1 data tensor:', w1_data.shape)
    print('Shape of word2 data tensor:', w2_data.shape)
    print('Shape of label tensor:', labels.shape)

    np.save(open(W1_TRAINING_DATA_FILE, 'wb'), w1_data)
    np.save(open(W2_TRAINING_DATA_FILE, 'wb'), w2_data)
    np.save(open(LABEL_TRAINING_DATA_FILE, 'wb'), labels)

X = np.concatenate((w1_data, w2_data), axis=1)
y = labels
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=TEST_SPLIT, random_state=RNG_SEED)
# W1_train = X_train[:, 0]
# W2_train = X_train[:, 1]
# W_train = np.concatenate((W1_train, W2_train), axis=1)

# W1_test = X_test[:, 0]
# W2_test = X_test[:, 1]
# W_test = np.concatenate((W1_test, W2_test), axis=1)

# Q1 = Sequential()
# Q1.add(Dense(32, input_dim=EMBEDDING_DIM))
#
# Q2 = Sequential()
# Q2.add(Dense(32, input_dim=EMBEDDING_DIM))

model = Sequential()
# model.add(Merge([Q1, Q2], mode='concat'))
model.add(BatchNormalization(input_shape=(600,)))
model.add(Dense(200, activation='relu'))
model.add(BatchNormalization())
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy', 'precision', 'recall', 'fbeta_score'])

callbacks = [ModelCheckpoint(MODEL_WEIGHTS_FILE, monitor='val_acc', save_best_only=True)]

print("Starting training at", datetime.datetime.now())

t0 = time.time()
history = model.fit(X_train,
                    y_train,
                    nb_epoch=NB_EPOCHS,
                    validation_split=VALIDATION_SPLIT,
                    verbose=1,
                    callbacks=callbacks)
t1 = time.time()

print("Training ended at", datetime.datetime.now())

print("Minutes elapsed: %f" % ((t1 - t0) / 60.))

model.load_weights(MODEL_WEIGHTS_FILE)

loss, accuracy, precision, recall, fbeta_score = model.evaluate(X_test, y_test)
print('')
print('loss      = {0:.4f}'.format(loss))
print('accuracy  = {0:.4f}'.format(accuracy))
print('precision = {0:.4f}'.format(precision))
print('recall    = {0:.4f}'.format(recall))
print('F         = {0:.4f}'.format(fbeta_score))
