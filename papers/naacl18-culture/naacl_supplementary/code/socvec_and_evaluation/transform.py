#!/usr/bin/env python
# encoding: utf-8
import sys
import numpy

def load_w2v_model(model_file):
    model = {}
    with open(model_file, 'r') as fin:
        for line in fin:
            items = line.strip().split()
            if len(items) < 2:
                continue
            word = items[0]
            vector = numpy.array(map(float, items[1:]))
            model[word] = vector
    return model


if __name__ == '__main__':
    american_model = load_w2v_model('/home/asdfg/cdminer/naacl/corpus_data/w2v/chineseembedding_0207.txt')
    british_model = load_w2v_model('/home/asdfg/cdminer/naacl/corpus_data/w2v/englishembedding_0207.txt')
    fp = open('/home/asdfg/cdminer/naacl/soling-lex/seed.txt', 'r')
    ch = set()
    en = set()
    interest_a = dict()
    interest_b = dict()
    for word in american_model.keys():
        interest_a[word] = 1
    for word in british_model.keys():
        interest_b[word] = 1

    used = dict()
    cnt = 0
    for line in fp.readlines():
        arr = line.split('\t')
        if (used.has_key(arr[0])):
            continue
        if (used.has_key(arr[1])):
            continue
        cnt += 1
        if (cnt > 1000):
            break
        if (interest_b.has_key(arr[0]) == 0):
            continue
        if (interest_a.has_key(arr[1]) == 0):
            continue
        en.add(arr[0])
        ch.add(arr[1])
        used[arr[0]] = 1
        used[arr[1]] = 1


    print len(en), len(ch)
    american_matrix = numpy.array([american_model[word] for word in ch])
    british_matrix = numpy.array([british_model[word] for word in en])
    print american_matrix.shape
    print british_matrix.shape
    american_matrix_with_c = numpy.vstack([american_matrix.T, numpy.ones(len(american_matrix))]).T
    print len(american_matrix)
    print len(british_matrix)
    result = numpy.linalg.lstsq(american_matrix_with_c, british_matrix)[0]
    print result.shape
    with open('/home/asdfg/cdminer/naacl/corpus_data/w2v/chineseembedding_0207.txt', 'r') as fin, open('trans_chinesefinal_0211.txt', 'w') as fout:
        for line in fin:
            items = line.strip().split()
            if len(items) <= 150:
                continue
            else:
                american_vector = american_model[items[0]]
                transformed_american_vector = numpy.dot(numpy.append(american_vector, 1), result)
                fout.write(items[0] + ' ' + ' '.join(map(str, transformed_american_vector)) + '\n')

