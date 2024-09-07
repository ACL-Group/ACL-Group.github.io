#!/usr/bin/env python
# encoding: utf-8



ent_dict = {}

for l in open('./eval.set','r').read().split('\n'):
    ls = l.split('\t')
    if(len(ls)==3):
        ent_dict[ls[0]] = (ls[1],ls[2])
import gensim
print 'loading emd.....'
model_en = gensim.models.Word2Vec.load_word2vec_format('/home/asdfg/cdminer/naacl/corpus_data/w2v/englishembedding_0207_toload.txt',binary=False)
print 'Done'

pid = str(raw_input('Input Your Two Word (like sony@@@ gaming): '))
while( len(pid.split()) == 2):
    a,b = pid.split()
    try:
        print model_en.similarity(a.decode('utf8'),b.decode('utf8'))
    except Exception,e:
        print e

    pid = str(raw_input('Input Your Two Word (like sony@@@ gaming): '))
