#!/usr/bin/env python
# encoding: utf-8

import scipy.stats
import sys

gold_dic = {}
toeval_dic = {}

diff_set = set()
sim_set = set()




for line in open(sys.argv[1],'r').read().split('\n'):
    ls = line.split('\t')
    if(len(ls)==4):
        gold_dic[int(ls[0])] = float(ls[3])
        if(float(ls[3])>3):
            sim_set.add(int(ls[0]))
        else:
            diff_set.add(int(ls[0]))

res = 0.0
rank = 1.0
for line in open(sys.argv[2],'r').read().split('\n'):
    ls = line.split('\t')
    if(len(ls)==4):
        if(int(ls[0]) in diff_set):
            res += 1.0 / rank
        rank += 1

print res/len(diff_set)


