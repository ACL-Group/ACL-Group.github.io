#!/usr/bin/env python
# encoding: utf-8

import sys
import numpy as np
from scipy import spatial
from sklearn import preprocessing

#####
cn_we = {}
lines = open('/home/name/cdminer/naacl/corpus_data/w2v/chineseembedding_0207.txt').read().split('\n')
cnt = 0
for line in lines[:]:
    ls = line.split()
    if(len(ls)==151):
        vec = [ float(ls[x]) for x in range(1,151) ]
        cn_we[ls[0]] = vec
        cnt +=1
        if(cnt%1000==0):
            print(cnt,'/',len(lines)-1)
print("Done 1")


####
print('loading social emd')
en_sco = {}
lines = open('socialembedding_en.txt').read().split('\n')
cnt = 0
for line in lines[1:]:
    ls = line.split()
    if(len(ls)==5488):
        vec = [ float(ls[x]) for x in range(1,5488) ]
        en_sco[ls[0]] = vec
        cnt +=1
        if(cnt%1000==0):
            print(cnt,'/',len(lines)-1)
print('Done 2')
### load dimension ###
cn_dim = []
en_dim = []
print('loading dim')
cur_en = True
for line in open('/home/name/cdminer/naacl/soling-lex/cat.tdim','r').read().split('\n'):
    ls = line.split(' ')
    if(len(ls)==151):
        if(cur_en):
            en_dim.append(np.array( [ float(ls[x]) for x in range(1,151) ] ))
            cur_en = False
        else:
            cn_dim.append(np.array( [ float(ls[x]) for x in range(1,151) ] ))
            cur_en = True
print('Done 3')

import json
trans = json.load(open('/home/name/slang/trans_en.json'))
def CalcSocialVectorForChinese(title):
    title = title
    cur = cn_we[title]
    res = []
    for dim in cn_dim:
        res.append(1-spatial.distance.cosine(cur,dim))
    return np.array(res)
def GetMostSimilar(cn):
    allres = []
    cn_sco = CalcSocialVectorForChinese(cn)
    cn_sco = preprocessing.normalize([cn_sco],norm='l2')
    for e in en_sco:
        #allres.append((e,spatial.distance.euclidean(en_sco[e],cn_sco[0])))
        allres.append(e)
    allres.sort(key = lambda x:x[1])
    return allres
cnt = 1
for line in open('OOV_zh2en.txt').read().split('\n'):
    ls = line.split('\t')
    zh = ls[0]
    if(zh in cn_we):
        print(zh)
        f = open('trans_res/'+str(cnt)+'.txt','w')
        res = GetMostSimilar(zh)
        for r in res:
            f.write(r[0]+'\n')
        f.close()
        cnt += 1
