import json
from pprint import pprint

from sklearn.metrics import average_precision_score

pair_score = {}
with open('final.txt', encoding='utf-8') as infile:
    for line in infile:
        ls = line.strip().split()
        terma = ls[0]
        termb = ls[1]
        score = float(ls[7])
        pair_score[terma + ' ' + termb] = score

truth = set()
all_500 = set()
with open('final_500_test.pairs', encoding='utf-8') as test_f:
    for line in test_f:
        ls = line.strip().split()
        terma = ls[0]
        termb = ls[1]
        label = int(ls[2])
        if label == 1:
            truth.add(terma + ' ' + termb)
        all_500.add(terma + ' ' + termb)
sorted_pair = sorted(pair_score.items(), key=lambda x: x[1], reverse=True)
# labels = [i[1] for i in truth]
# labeled_pair_list = [i[0] for i in truth]
# out_list = []
# for item in truth:
#     out_list.append(pair_score[item[0]])
# print(average_precision_score(labels, out_list))
#
# for pair, score in sorted_pair:
#     if pair in labeled_pair_list:
# print(sorted_pair)
right = 0
cnt = 0
for p in sorted_pair:
    if p[0] not in all_500:
        continue
    if p[0] in truth:
        right+=1
    cnt+=1
    if cnt%50==0:
        print(cnt,float(right)/float(cnt))
