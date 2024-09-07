import json
import sys
import random

if len(sys.argv) < 3:
    print('Missing input sentence_dataset and output_label file')
    exit(0)

DAT = sys.argv[1]
LABEL = sys.argv[2]

with open(DAT) as dat_f, open(LABEL, 'w') as out_f:
    for line in dat_f:
        ls = line.strip().split('\t')
        sent_id = ls[0]
        orig_sent = ls[1]
        all_pairs = json.loads(ls[3]) + json.loads(ls[4])
        pair = random.choice(all_pairs)
        pair_s = pair.split(' ')
        out_f.write(sent_id + '\t' + orig_sent + '\t' + pair_s[0] + '\t' + pair_s[1] + '\n')
