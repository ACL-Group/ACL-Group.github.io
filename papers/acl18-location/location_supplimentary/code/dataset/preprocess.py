import json

fout = open('AtLocation.tsv', 'w')
with open('conceptnet-assertions-5.5.0.csv') as f:
    for line in f:
        ls = line.split('\t')
        relation = ls[1]
        start = ls[2]
        end = ls[3]
        weight = json.loads(ls[4])['weight']
        if relation == '/r/AtLocation':
            fout.write(start + '\t' + end + '\t' + str(weight) + '\n')
fout.close()
