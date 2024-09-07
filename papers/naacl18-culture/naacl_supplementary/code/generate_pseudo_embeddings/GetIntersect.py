#!/usr/bin/env python
# encoding: utf-8

a_set = set()
b_set = set()
import sys
for l in open(sys.argv[1],'r').read().split('\n'):
    a_set.add(l)

for l in open(sys.argv[2],'r').read().split('\n'):
    b_set.add(l)

c_set = set.intersection(a_set,b_set)

for c in c_set:
    print c
