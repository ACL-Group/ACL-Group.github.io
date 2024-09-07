#!/usr/bin/env python
# encoding: utf-8

#coding=utf8
import sys
import os
import json
import cPickle as cp
reload(sys)
sys.setdefaultencoding('utf8')

f = open('enset.txt')
enset = set(f.read().split('\n'))
f.close()

f = open('cnset.txt')
cnset =set(f.read().split('\n'))
f.close()
'''
f = open('./seed.txt')
trans = {}
cnt = 0
for l in f.read().split('\n'):
    ls = l.split()
    if(len(ls)==3 and ls[0] in enset and ls[1] in cnset):
        cnt += 1
        if(cnt % 10000 == 0):
            print cnt
        if(ls[0] not in trans.keys()):
            trans[ls[0]] = []
        trans[ls[0]].append( (ls[1],float(ls[2]) ) )
f.close()

cp.dump(trans, open('trans_c.dict','wb'))
'''
trans =  cp.load(open('trans_c.dict','rb'))

print 'Done'


#load embeddings

cn_embedding = {}
en_embedding = {}


f = open('/home/asd/cdminer/naacl/corpus_data/w2v/chineseembedding_0207.txt')
for line in f.readlines():
    ls = line.split()
    if(len(ls)==151):
        if(ls[0] in cnset):
            cn_embedding[ls[0]] = line
f.close()

f = open('/home/asd/cdminer/naacl/corpus_data/w2v/englishembedding_0207.txt')
for line in f.readlines():
    ls = line.split()
    if(len(ls)==151):
        if(ls[0] in enset):
            en_embedding[ls[0]] = line
f.close()

#gen dims

import sys
import numpy as np
f = open(sys.argv[1],'r')
dim_en = set(f.read().split('\n'))
f.close()
f = open(sys.argv[2],'w')
for d in dim_en:
    if(d not in trans.keys()):
        continue
    f.write(en_embedding[d])
    trans[d].sort(key=lambda x : x[1],reverse=True)
    dc = trans[d][0]
    ls  = cn_embedding[dc[0]].split()
    vec = np.array( [float(ls[x]) for x in range(1,151)] )
    cnvec = vec
    line = d + '#cn ' + ' '.join(map(str,list(cnvec))) + '\n'
    f.write(line)

f.close()
