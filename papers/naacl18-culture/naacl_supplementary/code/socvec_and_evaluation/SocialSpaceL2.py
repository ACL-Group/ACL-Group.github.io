#!/usr/bin/env python
# encoding: utf-8

import sys
import cPickle as cp
import numpy as np
from scipy import spatial
from sklearn import preprocessing
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

SocialSpace_cn = []
SocialSpace_en = []



def CalcCulturalSimilarity(en,cn):
    cn = CalcSocialVectorForChinese(cn)
    en = CalcSocialVectorForEnglish(en)
    SocialSpace_cn.append(cn)
    SocialSpace_en.append(en)

def CalcAll():
    global SocialSpace_cn,SocialSpace_en
    ori_res = []
    cnt = 0
    for line in open('./eval.set','r').read().split('\n'):
        ls = line.split()
        if(len(ls)==3):
            ori_res.append(line)
            CalcCulturalSimilarity(ls[1],ls[2])
            cnt += 1
            print cnt
            #print len(res)
    SocialSpace_cn = np.array(SocialSpace_cn)
    SocialSpace_cn = preprocessing.scale(SocialSpace_cn)
    SocialSpace_cn = preprocessing.normalize(SocialSpace_cn,norm='l2')

    SocialSpace_en = np.array(SocialSpace_en)
    SocialSpace_en = preprocessing.scale(SocialSpace_en)
    SocialSpace_en = preprocessing.normalize(SocialSpace_en,norm='l2')


    final = []
    cnt = 0
    for line in open('./eval.set','r').read().split('\n'):
        ls = line.split()
        if(len(ls)==3):
            cur_cn = SocialSpace_cn[cnt]
            cur_en = SocialSpace_en[cnt]

            final.append( (line, -spatial.distance.euclidean(cur_cn,cur_en) ) )

            cnt += 1

    final.sort(key=lambda x:x[1])
    f = open(sys.argv[2],'w')
    for i in range(len(final)):
        f.write(final[i][0] + '\t' + str(final[i][1]) + '\n')
    f.close()

CalcAll()
#print CalcCulturalSimilarity('xi_jinping','习近平')#.decode('utf8'))









