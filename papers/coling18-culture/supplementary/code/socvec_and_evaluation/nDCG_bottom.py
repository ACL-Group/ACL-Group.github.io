#!/usr/bin/env python
# encoding: utf-8

import scipy.stats
import sys
import numpy as np
gold_dic = {}
toeval_dic = {}


ideal = []

for line in open(sys.argv[1],'r').read().split('\n'):
    ls = line.split('\t')
    if(len(ls)==4):
        gold_dic[int(ls[0])] = 11.0 - float(ls[3])
        ideal.append(11.0-float(ls[3]))
ideal.sort(reverse=True)
ideal_r = ideal[:]
ideal_r.sort()
IDCG = 0.0
DCG = 0.0
cnt = 1
for line in open(sys.argv[2],'r').read().split('\n'):
    ls = line.split('\t')
    if(len(ls)==4):
        #toeval_dic[int(ls[0])] = float(ls[3])
        pid = int(ls[0])
        rel_i = gold_dic[pid]
        DCG += ideal_r[cnt-1] / np.log2(cnt+1.0)
        IDCG += ideal[cnt-1] / np.log2(cnt+1.0)
        cnt +=1
print DCG/IDCG

