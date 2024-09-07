#!/usr/bin/env python
# encoding: utf-8



ent_dict = {}

for l in open('./eval.set','r').read().split('\n'):
    ls = l.split('\t')
    if(len(ls)==3):
        ent_dict[ls[0]] = (ls[1],ls[2])
import gensim
print 'loading emd.....'
#model_en = gensim.models.Word2Vec.load_word2vec_format('/home/asdfg/cdminer/naacl/corpus_data/w2v/englishembedding_0207_toload.txt',binary=False)
model_cn = gensim.models.Word2Vec.load_word2vec_format('/home/asdfg/cdminer/naacl/corpus_data/w2v/chineseembedding_0207_toload.txt',binary=False)
print 'Done'

pid = str(raw_input('Input Your Word (游戏): '))
while( len(pid) >= 1):
    try:
        for item in  model_cn.most_similar(pid.decode('utf-8'),topn=15):
            print item[0] , '\t' , item[1]
    except Exception,e:
        print e

    pid = str(raw_input('Input Your Word (游戏): '))
