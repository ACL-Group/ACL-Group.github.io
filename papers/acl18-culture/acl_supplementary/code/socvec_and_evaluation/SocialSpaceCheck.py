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
cn_dim_word = []
en_dim_word = []

### load dimension ###
print 'loading dim'
cur_en = True
for line in open(sys.argv[1],'r').read().split('\n'):
    ls = line.split(' ')
    if(len(ls)==151):
        if(cur_en):
            en_dim.append(np.array( [ float(ls[x]) for x in range(1,151) ] ))
            en_dim_word.append(ls[0])
            cur_en = False
        else:
            cn_dim.append(np.array( [ float(ls[x]) for x in range(1,151) ] ))
            cn_dim_word.append(ls[0])
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
    import heapq
    cn = CalcSocialVectorForChinese(cn)
    en = CalcSocialVectorForEnglish(en)
    cn_top = list(cn.argsort()[-50:][::-1])
    en_top = list(en.argsort()[-50:][::-1])

#    cn_top = heapq.nlargest(10,xrange(len(cn),cn.__getitem__))
#    en_top = heapq.nlargest(10,xrange(len(en),en.__getitem__))

    for x in range(50):
        print cn_dim_word[cn_top[x]] ,':',cn[cn_top[x]] , '\t\t\t\t', en_dim_word[en_top[x]],':',en[en_top[x]]

    '''
    print cn_dim_word[990]
    print cn_dim[990]
    print '索尼@@@ and 游戏', cn[990]
    cur = cn_we['索尼@@@']
    print cur
    print (1-spatial.distance.cosine(cur,cn_dim[990]) )
    '''

#print cn_we['习近平@@@']


ent_dict = {}

for l in open('./eval.set','r').read().split('\n'):
    ls = l.split('\t')
    if(len(ls)==3):
        ent_dict[ls[0]] = (ls[1],ls[2])
pid = str(raw_input('Input PairID: '))
while(pid in ent_dict):
    en,cn = ent_dict[pid]
    CalcCulturalSimilarity(en,cn)
    pid = str(raw_input('Input PairID: '))
