import csv
import itertools
import json
import sys


if len(sys.argv) < 3:
    print('Missing LEM and POS')
    exit(0)
LEM = sys.argv[1]
POS = sys.argv[2]

with open('refined_objects.txt') as base_f:
    physical_objects = set([line.strip() for line in base_f])

with open('blacklist.txt') as black_f:
    blacklist = set([line.strip() for line in black_f])

for item in blacklist:
    physical_objects.remove(item)

reader = csv.reader(open('AtLocation_en.tsv'), delimiter='\t')
all_objects = set()
pos_pairs = set()
for row in reader:
    name_a = row[0].split('/')[3]
    name_b = row[1].split('/')[3]
    if name_a in physical_objects and name_b in physical_objects:
        all_objects.add(name_a)
        all_objects.add(name_b)
        if name_a != name_b:
            pos_pairs.add(frozenset((name_a, name_b)))

all_combinations = set(map(frozenset, itertools.combinations(all_objects, 2)))
neg_pairs = all_combinations - pos_pairs

print('Total Objects:',  len(all_objects))
print('Total Pairs:',  len(all_combinations))
print('Positive Pairs',  len(pos_pairs))
print('Negative Pairs',  len(neg_pairs))

with open('objects.txt', 'w') as obj_f:
    for obj in all_objects:
        obj_f.write(obj + '\n')

pos_sentences = {}
neg_sentences = {}
for k in pos_pairs:
    pos_sentences[k] = []
for k in neg_pairs:
    neg_sentences[k] = []

with open(LEM) as text_f, open(POS) as pos_f:
    idx = 0
    for line1, line2 in zip(text_f, pos_f):
        if idx % 10000 == 0:
            print(idx)
        l = line1.strip()
        pos_tags = line2.strip().split(' ')
        all_tokens = l.split(' ')
        if 5 <= len(all_tokens) <= 30:
            try:
                assert len(all_tokens) == len(pos_tags)
            except AssertionError as e:
                print(e)
                print("idx: " + str(idx))
                exit(0)
            noun_token_set = set([all_tokens[i] for i, pos_tag in enumerate(pos_tags) if pos_tag in ('NN', 'NNS')])
            intersect = noun_token_set.intersection(all_objects)
            if len(intersect) == 0:
                continue
            this_combinations = set(map(frozenset, itertools.combinations(intersect, 2)))
            for pair in this_combinations:
                if pair in pos_pairs:
                    pos_sentences[pair].append(idx)
                else:
                    neg_sentences[pair].append(idx)
        idx += 1

with open('pos_sentences.txt', 'w') as fpos:
    for pair in pos_sentences:
        a, b = pair
        fpos.write(a + '\t' + b + '\t' + json.dumps(pos_sentences[pair]) + '\n')

with open('neg_sentences.txt', 'w') as fneg:
    for pair in neg_sentences:
        a, b = pair
        fneg.write(a + '\t' + b + '\t' + json.dumps(neg_sentences[pair]) + '\n')
