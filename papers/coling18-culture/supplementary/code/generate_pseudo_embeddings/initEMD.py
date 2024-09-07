# -*- coding:utf-8 -*-
from scipy import spatial
import cPickle
import sys
reload(sys)
sys.setdefaultencoding('utf8')


enset = set()
cnset = set()

for l in open('./seed.txt').read().split('\n'):
    ls = l.split()
    if(len(ls)==3):
        enset.add(ls[0])
        cnset.add(ls[1])


cn_embedding = {}
en_embedding = {}

def init():
    global cn_embedding,en_embedding
    f = open('/home/asd/cdminer/naacl/corpus_data/w2v/englishembedding_0207.txt')
    cnt = 0
    for line in f.readlines():
        ls = line.split()
        if(len(ls)==151):
            if(ls[0] in enset):
                vec = [ float(ls[x]) for x in range(1,151) ]
                en_embedding[ls[0]] = vec
                cnt +=1
                if(cnt%100==0):
                    print cnt,'/',len(enset)
    f.close()
    f = open('en_0207.emd','wb')
    cPickle.dump(en_embedding,f)
    f.close()

    print 'en done'

    cnt = 0
    f = open('/home/asd/cdminer/naacl/corpus_data/w2v/chineseembedding_0207.txt')
    cnt = 0
    for line in f.readlines():
        ls = line.split()
        if(len(ls)==151):
            if(ls[0] in cnset):
                vec = [ float(ls[x]) for x in range(1,151) ]
                cn_embedding[ls[0]] = vec
                cnt +=1
                if(cnt%100==0):
                    print cnt,'/',len(cnset)
    f.close()
    f = open('cn_0207.emd','wb')
    cPickle.dump(cn_embedding,f)
    f.close()

    print 'cn done'

init()


