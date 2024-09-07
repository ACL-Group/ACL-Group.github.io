# -*- coding:utf-8 -*-
from scipy import spatial
import cPickle
import sys
reload(sys)
sys.setdefaultencoding('utf8')


cn_embedding = {}
en_embedding = {}

def init():
    global cn_embedding,en_embedding
    f = open('/home/asd/cdminer/naacl/corpus_data/w2v/englishembedding_0207.txt')
    cnt = 0
    for line in f.readlines():
        ls = line.split()
        if(len(ls)==151):
            vec = [ float(ls[x]) for x in range(1,151) ]
            en_embedding[ls[0]] = vec
            cnt +=1
    f.close()

    print 'en done'

    cnt = 0
    f = open('../eval/trans_chinesefinal_0211.txt')
    cnt = 0
    for line in f.readlines():
        ls = line.split()
        if(len(ls)==151):
            vec = [ float(ls[x]) for x in range(1,151) ]
            cn_embedding[ls[0]] = vec
            cnt +=1
    f.close()
    print 'cn done'

init()



def CalcCulturalSimilarity(en,cn):
    cn = cn_embedding[cn]
    en = en_embedding[en]
    return 1-spatial.distance.cosine(cn,en)


pid = str(raw_input('Input Your Two Word (like sony@@@ gaming): '))
while( len(pid.split()) == 2):
    a,b = pid.split()
    print CalcCulturalSimilarity(a,b)
    pid = str(raw_input('Input Your Two Word (like sony@@@ gaming): '))
