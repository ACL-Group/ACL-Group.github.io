#!/usr/bin/env python
# encoding: utf-8

import gensim
from keras.preprocessing.text import text_to_word_sequence
import sys
import argparse


class Sent_Generator(object):
    def __init__(self=None):
        self.count = 0

    def __iter__(self):
        self.count = 0
        for line in open('/home/frank/relation/corpus/gutenberg/lem/all_lem.txt', 'r'):
            self.count += 1
            if self.count % 100000 == 0:
                print(str(self.count))
            tokens = text_to_word_sequence(line.strip())
            yield tokens


if __name__ == '__main__':
    sentences = Sent_Generator()
    print('Start Training')
    model = gensim.models.Word2Vec(sentences, size=50, window=5, min_count=5, workers=30)
    print('Saving')
    with open('data/EMD/all_50.emd', 'w') as fout:
        for word in model.wv.vocab:
            fout.write(word + ' ' + ' '.join(map(str, model.wv[word])) + '\n')
