#!/usr/bin/env python
# encoding: utf-8

a_set = set()
b_set = set()

top = 200
import sys
for a in open(sys.argv[1]).read().split('\n'):
    ls = a.split('\t')
    if(len(ls)!=4):
        continue
    a_set.add(int(ls[0]))
    if(len(a_set)>=top):
        break

for b in open(sys.argv[2]).read().split('\n'):
    ls = b.split('\t')
    if(len(ls)!=4):
        continue
    b_set.add(int(ls[0]))
    if(len(b_set)>=top):
        break
print len(a_set)
print len(b_set)
print len(a_set.intersection(b_set))

