#!/usr/bin/env python
# encoding: utf-8



ent_dict = {}

for l in open('./eval.set','r').read().split('\n'):
    ls = l.split('\t')
    if(len(ls)==3):
        ent_dict[ls[0]] = (ls[1],ls[2])
import gensim
print 'loading emd.....'
model_en = gensim.models.Word2Vec.load_word2vec_format('/home/asdfg/cdminer/naacl/corpus_data/w2v/englishembedding_0207_toload.txt',binary=False)
model_cn = gensim.models.Word2Vec.load_word2vec_format('/home/asdfg/cdminer/naacl/corpus_data/w2v/chineseembedding_0207_toload.txt',binary=False)
print 'Done'

pid = str(raw_input('Input PairID: '))
while(pid in ent_dict):


    print '\n\n\nMost Similar English Words of ', ent_dict[pid][0]
    for item in  model_en.most_similar([ent_dict[pid][0].lower() + '@@@' ],topn=100):
        print item[0] , '\t' , item[1]

    print '\nMost Similar Chinese Words of ', ent_dict[pid][1]
    for item in  model_cn.most_similar([ent_dict[pid][1].decode('utf8') + '@@@' ],topn=100):
        print item[0] , '\t' , item[1]
    print '----------------------------------------'
    pid = str(raw_input('\nInput PairID: '))
