#!/usr/bin/env python
# encoding: utf-8

import sys
import numpy as np
from scipy import spatial
from sklearn import preprocessing
import gensim


#####
cn_we = {}
lines = open('/home/asd/cdminer/naacl/corpus_data/w2v/chineseembedding_0207.txt').read().split('\n')
cnt = 0
for line in lines[:]:
    ls = line.split()
    if(len(ls)==151):
        vec = [ float(ls[x]) for x in range(1,151) ]
        cn_we[ls[0]] = vec
        cnt +=1
        if(cnt%100000==0):
            print(cnt,'/',len(lines)-1)


model_cn = gensim.models.Word2Vec.load_word2vec_format('/home/asd/cdminer/naacl/corpus_data/w2v/chineseembedding_0207_toload.txt',binary=False)
print("Done 1")

####
print('loading social emd')
en_sco = {}
lines = open('socialembedding_en.txt.0216').read().split('\n')
cnt = 0
for line in lines[1:]:
    ls = line.split()
    if(len(ls)==3805):
        vec = [ float(ls[x]) for x in range(1,3805) ]
        en_sco[ls[0]] = vec
        cnt +=1
        if(cnt%1000==0):
            print(cnt,'/',len(lines)-1)
print('Done 2')
### load dimension ###
cn_dim = []
en_dim = []
print('loading dim')
cur_en = True
for line in open('/home/asd/cdminer/naacl/soling-lex/opn.gdim','r').read().split('\n'):
    ls = line.split(' ')
    if(len(ls)==151):
        if(cur_en):
            en_dim.append(np.array( [ float(ls[x]) for x in range(1,151) ] ))
            cur_en = False
        else:
            cn_dim.append(np.array( [ float(ls[x]) for x in range(1,151) ] ))
            cur_en = True
print('Done 3')

import json
trans = json.load(open('/home/asdf/slang/trans_en.json'))
def CalcSocialVectorForChinese(title):
    title = title
    cur = cn_we[title]
    res = []
    for dim in cn_dim:
        res.append(1-spatial.distance.cosine(cur,dim))
    return np.array(res)
def GetMostSimilar_single(cn):
    allres = []
    if cn not in cn_we:
        return allres
    cn_sco = CalcSocialVectorForChinese(cn)
    cn_sco = preprocessing.normalize([cn_sco],norm='l2')
    for e in en_sco:
        allres.append((e,1-spatial.distance.euclidean(en_sco[e],cn_sco[0])))
    allres.sort(key = lambda x:x[1],reverse=True)
    return allres[:5]


def GetMostSimilar(cn):
    allres = list()
    allres += GetMostSimilar_single(cn)
    for item in model_cn.most_similar(cn.decode('utf-8'), topn=2):
        allres += GetMostSimilar_single(item[0].encode('utf-8'))

    allres.sort(key=lambda x: x[1])
    # final_res = [x[0] for x in allres]
    res_dic = {}
    for l in allres:
        if(l[0] not in res_dic):
            res_dic[l[0]] = 0.0
        res_dic[l[0]] += l[1]
    finalres = list(res_dic.items())
    finalres.sort(key=lambda x: x[1],reverse=True)
    finalres = [x[0] for x in finalres]
    return finalres[:5]
from scipy import spatial
import numpy as np

en_emd = dict()
def loadEMD():
    # lines = open('/home/asdfg/2.14/Validgoogleword2vec.txt').read().split('\n')
    lines = open('/home/asd/cdminer/naacl/corpus_data/w2v/englishembedding_0207.txt').read().split('\n')
    cnt = 1
    print('loading')
    for line in lines:
        ls = line.split()
        if len(ls)==151:
            en_emd[ls[0]] = np.array([float(k) for k in ls[1:151]])
            cnt += 1
            if cnt%10000==0:
                print(str(cnt)+'/'+str(len(lines)))
loadEMD()

def calcAvgSim(a_list,b_list):
    sim = 0.0
    sim_cnt = 0
    for a  in a_list:
        for b in b_list:
            a = a.lower()
            b = b.lower()
            if a not in en_emd:
                sim_cnt +=1
                continue
            if b not in en_emd:
                continue
            sim += 1 - spatial.distance.cosine(en_emd[a],en_emd[b])
            sim_cnt += 1
    if(sim_cnt==0):
        return 0.0
    return sim/sim_cnt
cnt = 1
google_res = 0.0
bing_res = 0.0
baidu_res = 0.0
cc_res = 0.0
soc_res = 0.0

for line in open('ZH_OOV.tsv','r').read().split('\n'):
    ls = line.split('\t')

    if(len(ls)!=7):
        title = ls[0]
        if(title not in cn_we):
            continue
        print title
        google = ls[1]
        bing = ls[2]
        baidu = ls[3]
        cc = ls[4]
        truth = ls[5]
        soc_list = GetMostSimilar(title)
        print ' '.join(soc_list)
        google_res += calcAvgSim(google.strip().split(),truth.strip().split())
        bing_res += calcAvgSim(bing.strip().split(),truth.strip().split())
        baidu_res += calcAvgSim(baidu.strip().split(),truth.strip().split())
        cc_res +=  calcAvgSim(cc.strip().split(),truth.strip().split())
        soc_res += calcAvgSim(soc_list ,truth.strip().split())
        cnt += 1

print(google_res , bing_res , baidu_res , cc_res , soc_res)
