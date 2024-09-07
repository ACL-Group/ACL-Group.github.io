#!/usr/bin/env python
# encoding: utf-8

import sys
import cPickle as cp
import numpy as np
from scipy import spatial

print 'loading word embedding'
import gensim
model_en = gensim.models.Word2Vec.load_word2vec_format('/home/asdfg/cdminer/naacl/corpus_data/w2v/englishembedding_0207_toload.txt',binary=False)
model_cn = gensim.models.Word2Vec.load_word2vec_format('/home/asdfg/cdminer/naacl/corpus_data/w2v/chineseembedding_0207_toload.txt',binary=False)

print 'Done'

import cPickle as cp
trans = cp.load(open('../soling-lex/trans.dict','rb'))
print 'Done'

for line in open('./eval.set','r').read().split('\n'):
    ls = line.split()
    if(len(ls)==3):
        trans[ls[1].lower()+'@@@'] = [ls[2]+'@@@']
K = 500

trans_value_set = set()
for val in trans.values():
    trans_value_set = trans_value_set.union(set(val))


def CalcSocialVectorForEnglish(title):
    global K
    title = title.lower()+'@@@'
    res = []
    for item in model_en.most_similar([title.decode('utf8')],topn=K):
        if(item[0].encode('utf8') in trans):
            res.append(item[0].encode('utf8'))
    return res

def CalcSocialVectorForChinese(title):
    global K
    title = title+'@@@'
    res = []
    for item in model_cn.most_similar([title.decode('utf8')],topn=K):
        if(item[0].encode('utf8') in trans_value_set):
            res.append(item[0].encode('utf8'))
    return res

def CalcCulturalSimilarity(en,cn):
    cn_res = CalcSocialVectorForChinese(cn)
    en_res = CalcSocialVectorForEnglish(en)
    middle_set = set()
    for e in en_res:
        middle_set = middle_set.union(trans[e])
    cn_set = set(cn_res)
    #print len(middle_set),len(cn_set),len(middle_set.intersection(cn_set))
    return (len(middle_set.intersection(cn_set))+0.0) / len(middle_set.union(cn_set))


def CalcAll():
    res = []
    for line in open('./final_exp/eval.set.0212','r').read().split('\n'):
        ls = line.split()
        if(len(ls)==3):
            res.append((line,CalcCulturalSimilarity(ls[1],ls[2])))
            print len(res)
    res.sort(key=lambda x:x[1])
    f = open(sys.argv[1],'w')
    for r in res:
        f.write(r[0] + '\t' + str(r[1]) + '\n')
    f.close()

CalcAll()

