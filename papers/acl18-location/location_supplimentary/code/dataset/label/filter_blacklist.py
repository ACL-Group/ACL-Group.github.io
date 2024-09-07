import csv

with open('../blacklist.txt') as black_f:
    blacklist = set([line.strip() for line in black_f])

fin = open('gutenberg_label_1000.tsv')
f = open('gutenberg_label_filtered.tsv', 'w')
for line in fin:
    row = line.strip().split('\t')
    name_a = row[2]
    name_b = row[3]
    if name_a not in blacklist and name_b not in blacklist:
        f.write(row[0] + '\t' + row[1] + '\t' + row[2] + '\t' + row[3] + '\t' + row[4] + '\n')
