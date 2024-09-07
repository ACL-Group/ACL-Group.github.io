#!/usr/bin/env python
# encoding: utf-8

import scipy.stats
import sys

gold_dic = {}
toeval_dic = {}

for line in open(sys.argv[1],'r').read().split('\n'):
    ls = line.split('\t')
    if(len(ls)==4):
        gold_dic[int(ls[0])] = float(ls[3])

for line in open(sys.argv[2],'r').read().split('\n'):
    ls = line.split('\t')
    if(len(ls)==4):
        toeval_dic[int(ls[0])] = float(ls[3])


gold = []
toeval = []

for k in gold_dic.keys():
    gold.append(gold_dic[k])
    toeval.append(toeval_dic[k])
print(scipy.stats.pearsonr(gold,toeval))



