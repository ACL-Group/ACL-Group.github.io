#!/usr/bin/env python
# encoding: utf-8

import sys
import cPickle as cp
import numpy as np
from scipy import spatial

print 'loading word embedding'
cn_we = cp.load(open('./cn_ent_0207.emd','rb'))
en_we = cp.load(open('./en_ent_0207.emd','rb'))
print 'Done'

cn_dim = []
en_dim = []


### load dimension ###
print 'loading dim'
cur_en = True
for line in open(sys.argv[1],'r').read().split('\n'):
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
    title = title.lower()+'@@@'
    cur = en_we[title]
    res = []
    for dim in en_dim:
        res.append(1-spatial.distance.cosine(cur,dim))
    return np.array(res)

def CalcSocialVectorForChinese(title):
    title = title+'@@@'
    cur = cn_we[title]
    res = []
    for dim in cn_dim:
        res.append(1-spatial.distance.cosine(cur,dim))
    return np.array(res)

def CalcCulturalSimilarity(en,cn):
    cn = CalcSocialVectorForChinese(cn)
    en = CalcSocialVectorForEnglish(en)
    return 1-spatial.distance.cosine(cn,en)


def CalcAll():
    res = []
    for line in open('./eval.set','r').read().split('\n'):
        ls = line.split()
        if(len(ls)==3):
            res.append((line,CalcCulturalSimilarity(ls[1],ls[2])))
            print len(res)
    res.sort(key=lambda x:x[1])
    f = open(sys.argv[2],'w')
    for r in res:
        f.write(r[0] + '\t' + str(r[1]) + '\n')
    f.close()

CalcAll()
#print CalcCulturalSimilarity('xi_jinping','习近平')#.decode('utf8'))









