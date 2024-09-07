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

from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split
from keras import backend as K, optimizers
from keras.callbacks import ModelCheckpoint, EarlyStopping
from keras.layers import Embedding, Dense, Merge, BatchNormalization, TimeDistributed, Lambda, LSTM, SimpleRNN, Dropout, \
    Input, Bidirectional, Convolution1D
from keras.models import Sequential, load_model
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer, text_to_word_sequence
from keras.utils.data_utils import get_file
from helper import WordNet_44_categories, GR_19_categories, POS_15_categories, lst_2_dic, sequence_from_dic, \
    train_val_test_split

RNG_SEED = 123123
np.random.seed(RNG_SEED)

KERAS_DATASETS_DIR = expanduser('~/.keras/datasets/')
MAX_NB_WORDS = 20000
SENNA_EMD_FILE = '/home/frank/relation/embedding/senna/embeddings/merged_embeddings.txt'
GLOVE_EMD_FILE = 'data/EMD/glove.6B.100d.txt'
MODEL_WEIGHTS_FILE = 'lstm5k_weights.h5'
MAX_SEQUENCE_LENGTH = 40
EMBEDDING_DIM = 100
POS_EMBEDDING_DIM = 5


data = []
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

DIR_NAME = '/home/frank/relation/dataset/gutenberg/pair_sentences/norm_sent_termab'
for filename in os.listdir(DIR_NAME):
    if filename.endswith('.norm_termab'):
        file = os.path.join(DIR_NAME, filename)
        termab = filename.split('.')[0]
        terma = termab.split('_')[0]
        termb = termab.split('_')[1]
        for line in open(file, encoding='utf-8'):
            terma_list.append(terma)
            termb_list.append(termb)
            norm_sentences.append(line.strip())

tokenizer = pickle.load(open('tokenizer.pk', 'rb'))
word_sequences = tokenizer.texts_to_sequences(norm_sentences)
word_index = tokenizer.word_index

# calculate position sequences
terma_index = word_index['terma']
termb_index = word_index['termb']
for idx, sent in enumerate(word_sequences):
    # terma_index = word_index[terma_list[idx]]
    # termb_index = word_index[termb_list[idx]]
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

word_embedding_matrix = np.zeros((nb_words + 1, EMBEDDING_DIM))
for word, i in word_index.items():
    if i > MAX_NB_WORDS:
        continue
    embedding_vector = embeddings_index.get(word)
    if embedding_vector is not None:
        word_embedding_matrix[i] = embedding_vector

print('Null word embeddings: %d' % np.sum(np.sum(word_embedding_matrix, axis=1) == 0))

word_sequences = pad_sequences(word_sequences, maxlen=MAX_SEQUENCE_LENGTH)
position_a_seqs = pad_sequences(position_a_seqs, maxlen=MAX_SEQUENCE_LENGTH)
position_b_seqs = pad_sequences(position_b_seqs, maxlen=MAX_SEQUENCE_LENGTH)
terma_vectors = np.array([embeddings_index[word] if word in embeddings_index else embeddings_index['UNK'] for word in terma_list])
termb_vectors = np.array([embeddings_index[word] if word in embeddings_index else embeddings_index['UNK'] for word in termb_list])
termab_vectors = np.concatenate((terma_vectors, termb_vectors), axis=1)

print('Shape of sequence data tensor:', word_sequences.shape)
print('Shape of termab data tensor:', termab_vectors.shape)
total_data_num = word_sequences.shape[0]

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

model.load_weights(MODEL_WEIGHTS_FILE)
y_pred = model.predict_classes([word_sequences, position_a_seqs, position_b_seqs, termab_vectors], batch_size=50000)
y_proba = model.predict_proba([word_sequences, position_a_seqs, position_b_seqs, termab_vectors], batch_size=50000)

gc.collect()
filtered_terms = {'head', 'hand', 'man', 'woman'}
labeled_pair_count = {}
labeled_pair_proba = {}
for idx, label in enumerate(y_pred):
    terma = terma_list[idx]
    termb = termb_list[idx]
    termab = terma + ' ' + termb
    proba = y_proba[idx]
    if terma not in filtered_terms and termb not in filtered_terms:
        if termab not in labeled_pair_count:
            labeled_pair_count[termab] = [0, 0]
            labeled_pair_count[termab][int(label)] += 1
            labeled_pair_proba[termab] = proba
        else:
            labeled_pair_count[termab][int(label)] += 1
            labeled_pair_proba[termab] += proba

with open('extract_result_final.txt', 'w') as of:
    for pair in labeled_pair_count:
        of.write(pair + '\t' + str(labeled_pair_count[pair][0]) + '\t' + str(labeled_pair_count[pair][1]) + '\t' +
                 str(float(labeled_pair_proba[pair])) + '\n')
