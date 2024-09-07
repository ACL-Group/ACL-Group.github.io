# -*- coding:utf-8 -*-
from scipy import spatial
import cPickle
import sys
reload(sys)
sys.setdefaultencoding('utf8')


enset = set()
cnset = set()

for l in open('./eval.set').read().split('\n'):
    ls = l.split()
    if(len(ls)==3):
        enset.add(ls[1].lower()+'@@@')
        cnset.add(ls[2]+'@@@')


cn_embedding = {}
en_embedding = {}

def init():
    global cn_embedding,en_embedding
    f = open('/home/asdfg/cdminer/naacl/corpus_data/w2v/englishembedding_0207.txt')
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
    f = open('en_ent_0207.emd','wb')
    cPickle.dump(en_embedding,f)
    f.close()

    print 'en done'

    cnt = 0
    f = open('./trans_chinesefinal_0211.txt')
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
    f = open('cn_ent_0207.emd','wb')
    cPickle.dump(cn_embedding,f)
    f.close()

    print 'cn done'

init()



def CalcCulturalSimilarity(en,cn):
    cn = cn_embedding[cn+'@@@']
    en = en_embedding[en.lower()+'@@@']
    return 1-spatial.distance.cosine(cn,en)


def CalcAll():
    res = []
    for line in open('./final_exp/eval.set.0212','r').read().split('\n'):
        ls = line.split()
        if(len(ls)==3):
            res.append((line,CalcCulturalSimilarity(ls[1],ls[2])))
            print len(res)
    res.sort(key=lambda x:x[1])
    f = open(sys.argv[1],'w')
    for r in res:
        f.write(r[0] + '\t' + str(r[1]) + '\n')
    f.close()

CalcAll()
