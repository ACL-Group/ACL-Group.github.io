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
        elif(float(ls[3])<3):
            diff_set.add(int(ls[0]))
y_true = []
y_scores= []

for line in open(sys.argv[2],'r').read().split('\n'):
    ls = line.split('\t')
    if(len(ls)==4):
        if(int(ls[0]) in diff_set):
            y_true.append(0)
        else:
            y_true.append(1)
        y_scores.append(float(ls[3]))
import numpy as np
from sklearn.metrics import average_precision_score
print average_precision_score(y_true,y_scores)




