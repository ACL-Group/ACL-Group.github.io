import json
import sys
import os
import random

random.seed(123123)

if len(sys.argv) < 3:
    print('Missing input sentence_dataset and output folder')
    exit(0)

DAT = sys.argv[1]
OUT = sys.argv[2]

with open(DAT) as dat_f:
    all_pairs = {}
    pair_count = {}
    for line in dat_f:
        ls = line.strip().split('\t')
        sent_id = ls[0]
        orig_sent = ls[1]
        sent_pairs = json.loads(ls[3]) + json.loads(ls[4])
        if 25 >= len(orig_sent.split(' ')) >= 5:
            for pair in sent_pairs:
                if pair not in all_pairs:
                    all_pairs[pair] = []
                    all_pairs[pair].append((sent_id, orig_sent))
                else:
                    all_pairs[pair].append((sent_id, orig_sent))
    print(len(all_pairs))
    exit(0)
    for pair in all_pairs:
        num = len(all_pairs[pair])
        if num > 10:
            pair_count[pair] = num
    print(len(pair_count))

    for pair in pair_count:
        with open(os.path.join(OUT, '_'.join(pair.split()) + '.txt'), 'w', encoding='utf-8') as of:
            for line in all_pairs[pair]:
                of.write(line[0] + '\t' + line[1] + '\n')
    # pair_list = list(pair_count)
    # random.shuffle(pair_list)
    # selected_pairs = pair_list[:400]
    # selected_pair_sent = {}
    # for pair in selected_pairs:
    #     temp_list = all_pairs[pair]
    #     random.shuffle(temp_list)
    #     selected_pair_sent[pair] = temp_list[:10]
    # sent_to_label = []
    # for pair in selected_pair_sent:
    #     for sent in selected_pair_sent[pair]:
    #         sent_to_label.append(sent[0] + '\t' + sent[1] + '\t' +
    #                              pair.split()[0] + '\t' + pair.split()[1])
    # random.shuffle(sent_to_label)
    # with open(os.path.join(OUT, 'sent_to_label.txt'), 'w') as label_f:
    #     for line in sent_to_label:
    #         label_f.write(line + '\n')
