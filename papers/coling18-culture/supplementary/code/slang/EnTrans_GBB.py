import os

from scipy import spatial
import numpy as np

en_emd = dict()
def loadEMD():
    # lines = open('/home/asdfg/2.14/Validgoogleword2vec.txt').read().split('\n')
    lines = open('/home/asd/cdminer/naacl/corpus_data/w2v/chineseembedding_0207.txt').read().split('\n')
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

for line in open('EN_OOV.tsv','r').read().split('\n'):
    ls = line.split('\t')

    if(len(ls)>=3):
        title = ls[0]
        print title
        google = ls[3]
        bing = ls[4]
        baidu = ls[5]
        truth = ls[2]
        google_res += calcAvgSim(google.strip().split(),truth.strip().split())
        bing_res += calcAvgSim(bing.strip().split(),truth.strip().split())
        baidu_res += calcAvgSim(baidu.strip().split(),truth.strip().split())
        cnt += 1

print(google_res , bing_res , baidu_res , cc_res , soc_res)