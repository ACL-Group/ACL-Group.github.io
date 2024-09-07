#!/usr/bin/env python
# encoding: utf-8

import sys
import cPickle as cp
import numpy as np
from scipy import spatial
from sklearn import preprocessing
print 'loading word embedding'
cn_we = {}
lines = open('/home/asd/cdminer/naacl/corpus_data/w2v/chineseembedding_0207.txt').read().split('\n')
cnt = 0
for line in lines[:]:
    ls = line.split()
    if(len(ls)==151):
        vec = [ float(ls[x]) for x in range(1,151) ]
        cn_we[ls[0]] = vec
        cnt +=1
        if(cnt%100000==0):
            print(cnt,'/',len(lines)-1)
print("Done 1")
cn_dim = []
en_dim = []
trans = {}
trans = cp.load(open('../soling-lex/trans.dict','rb'))
### load dimension ###
print 'loading dim'
cur_en = True
for line in open('../soling-lex/opn.gdim','r').read().split('\n'):
    ls = line.split(' ')
    if(len(ls)==151):
        if(cur_en):
            en_dim.append(np.array( [ float(ls[x]) for x in range(1,151) ] ))
            cur_en = False
        else:
            cn_dim.append(np.array( [ float(ls[x]) for x in range(1,151) ] ))
            cur_en = True
print 'load dim done'
def CalcSocialVectorForEnglish(title):
    title = title.lower()
    cur = en_we[title]
    res = []
    for dim in en_dim:
        res.append(1-spatial.distance.cosine(cur,dim))
    return np.array(res)
def CalcSocialVectorForChinese(title):
    title = title
    cur = cn_we[title]
    res = []
    for dim in cn_dim:
        res.append(1-spatial.distance.cosine(cur,dim))
    return np.array(res)
SocialSpace_en = []
def CalcCulturalSimilarity(en,cn):
    cn = CalcSocialVectorForChinese(cn)
    en = CalcSocialVectorForEnglish(en)
    SocialSpace_cn.append(cn)
    SocialSpace_en.append(en)
def CalcAll():
    global SocialSpace_en
    lst_e = []
    cnt = 0
    cnword_set = set()
    for e in trans.keys():
        cnword_set = cnword_set.union(set(trans[e]))
    for c in cnword_set:
        s_cn = CalcSocialVectorForChinese(c)
        SocialSpace_en.append(s_cn)
        lst_e.append(c)
        cnt += 1
        if (cnt % 1000==0):
            print cnt,'/',len(cnword_set)
    SocialSpace_en = np.array(SocialSpace_en)
    SocialSpace_en = preprocessing.scale(SocialSpace_en)
    SocialSpace_en = preprocessing.normalize(SocialSpace_en,norm='l2')
    f = open('socialembedding_cn.txt','w')
    f.write(str(cnt)+' '+str(len(en_dim))+'\n')
    for i in range(cnt):
        f.write(lst_e[i] + ' ' + ' '.join(map(str,SocialSpace_en[i]))+'\n')
    f.close()
CalcAll()