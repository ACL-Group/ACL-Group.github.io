#!/usr/bin/env python
# encoding: utf-8


f = open('./categories.tsv','r')
for line in f.read().split('\n'):
    if(line.startswith('~')):
        ls = line[1:].split('\t')
        for item in ls:
            if(' ' not in item):
                print item
