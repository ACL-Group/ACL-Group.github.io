from pprint import pprint

from collections import OrderedDict
import json
import networkx as nx

import math


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def calc_score(x, y):
    return x + (1 - x) * math.pow(y, (1/x))


LABELED_FILE = 'data/ORIG/label5000.txt'

labeled_pairs = {}
# build a simple KB
for line in open(LABELED_FILE, encoding='utf-8'):
    ls = line.strip().split('\t')
    termab = (ls[2], ls[3])
    if int(ls[4]) == 1:
        if termab not in labeled_pairs:
            labeled_pairs[termab] = 1
        else:
            labeled_pairs[termab] += 1

G = nx.Graph()
for pair in labeled_pairs:
    G.add_edge(pair[0], pair[1], weight=labeled_pairs[pair])

print(G.number_of_nodes())
print(G.number_of_edges())


def calculate_semantic_score(G, terma, termb):
    if G.has_node(terma) and G.has_node(termb):
        terma_neighbors = set(nx.neighbors(G, terma))
        termb_neighbors = set(nx.neighbors(G, termb))
        intersect = terma_neighbors.intersection(termb_neighbors)
        intersect_score = sum((G[node][terma]['weight'] + G[node][termb]['weight']) for node in intersect)
        union_score = sum(G[node][terma]['weight'] for node in terma_neighbors) + \
                      sum(G[node][termb]['weight'] for node in termb_neighbors)
        if G.has_edge(terma, termb):
            intersect_score += G[terma][termb]['weight']
            union_score += G[terma][termb]['weight']
        return float(intersect_score)/union_score
    else:
        return 0.0

proba_dict = OrderedDict()

with open('lstm_proba.txt', encoding='utf-8') as proba_file:
    for idx, line in enumerate(proba_file):
        ls = line.strip().split('\t')
        terma = ls[0]
        termb = ls[1]
        proba = float(json.loads(ls[2])[0])
        proba_dict[idx] = {'terma': terma, 'termb': termb, 'proba': proba}

to_add = [1]
while to_add:
    print('Starting Iter')
    for key in proba_dict:
        proba = proba_dict[key]['proba']
        terma = proba_dict[key]['terma']
        termb = proba_dict[key]['termb']
        semantic_score = calculate_semantic_score(G, terma, termb)
        proba_dict[key]['semantic'] = semantic_score
        proba_dict[key]['score'] = calc_score(proba_dict[key]['proba'], proba_dict[key]['semantic'])

    toplist = sorted(proba_dict.items(), key=lambda x: x[1]['score'], reverse=True)
    print(toplist[:5])
    to_add = [item for item in toplist if item[1]['score'] >= 0.9]
    print(to_add)
    for item in to_add:
        del proba_dict[item[0]]
        terma = item[1]['terma']
        termb = item[1]['termb']
        if G.has_edge(terma, termb):
            G[terma][termb]['weight'] += 1
        else:
            G.add_edge(terma, termb, weight=1)
print(G.number_of_nodes())
print(G.number_of_edges())
