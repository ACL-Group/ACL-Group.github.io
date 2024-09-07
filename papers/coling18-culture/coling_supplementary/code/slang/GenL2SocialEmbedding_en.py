#!/usr/bin/env python
# encoding: utf-8

import sys
import cPickle as cp
import numpy as np
from scipy import spatial
from sklearn import preprocessing
print 'loading word embedding'

#cn_we = cp.load(open('./cn_all.emd','rb'))
en_we = cp.load(open('./en_all.emd','rb'))

print 'Done'

cn_dim = []
en_dim = []
trans = {}
trans = cp.load(open('../soling-lex/trans.dict','rb'))

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

SocialSpace_cn = []
SocialSpace_en = []



def CalcCulturalSimilarity(en,cn):
    cn = CalcSocialVectorForChinese(cn)
    en = CalcSocialVectorForEnglish(en)
    SocialSpace_cn.append(cn)
    SocialSpace_en.append(en)

def CalcAll():
    global SocialSpace_cn,SocialSpace_en

    '''
    SocialSpace_cn = np.array(SocialSpace_cn)
    SocialSpace_cn = preprocessing.scale(SocialSpace_cn)
    SocialSpace_cn = preprocessing.normalize(SocialSpace_cn,norm='l2')
    '''
    lst_e = []
    cnt = 0
    for e in trans.keys():
        s_en = CalcSocialVectorForEnglish(e)
        SocialSpace_en.append(s_en)
        lst_e.append(e)
        cnt += 1
        if(cnt%1000):
            print cnt,'/',len(trans)
    SocialSpace_en = np.array(SocialSpace_en)
    SocialSpace_en = preprocessing.scale(SocialSpace_en)
    SocialSpace_en = preprocessing.normalize(SocialSpace_en,norm='l2')
    f = open('socialembedding_en.txt','w')
    f.write(str(cnt)+' '+str(len(en_dim))+'\n')
    for i in range(cnt):
        f.write(lst_e[i] + ' ' + ' '.join(map(str,SocialSpace_en[i]))+'\n')
    f.close()
CalcAll()
