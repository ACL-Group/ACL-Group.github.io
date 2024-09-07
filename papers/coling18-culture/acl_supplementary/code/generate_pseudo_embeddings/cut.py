#!/usr/bin/env python
# encoding: utf-8

i = 0
for l in open('./bsl.dim'):
    l = l.split()[0]
    if i%2 == 1:
        print l
    else:
        print l,
    i += 1
