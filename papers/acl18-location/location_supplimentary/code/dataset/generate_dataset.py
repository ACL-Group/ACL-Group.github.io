import json
import sys

if len(sys.argv) < 4:
    print('Missing LEM and ORIG and POSTAG')
    exit(0)
LEM = sys.argv[1]
ORIG = sys.argv[2]
POSTAG = sys.argv[3]


all_sentenceIds = set()
pos_sentences = {}
neg_sentences = {}

print('Reading pos sentences')
with open('pos_sentences.txt') as pos_f:
    for line in pos_f:
        ls = line.strip().split('\t')
        name_a = ls[0]
        name_b = ls[1]
        sentenceId_list = json.loads(ls[2])
        if len(sentenceId_list) != 0:
            all_sentenceIds.update(sentenceId_list)
            for idx in sentenceId_list:
                if idx not in pos_sentences:
                    pos_sentences[idx] = [name_a + ' ' + name_b]
                else:
                    pos_sentences[idx].append(name_a + ' ' + name_b)

print('Reading neg sentences')
with open('neg_sentences.txt') as neg_f:
    for line in neg_f:
        ls = line.strip().split('\t')
        name_a = ls[0]
        name_b = ls[1]
        sentenceId_list = json.loads(ls[2])
        if len(sentenceId_list) != 0:
            all_sentenceIds.update(sentenceId_list)
            for idx in sentenceId_list:
                if idx not in neg_sentences:
                    neg_sentences[idx] = [name_a + ' ' + name_b]
                else:
                    neg_sentences[idx].append(name_a + ' ' + name_b)

print('Total sentences:' + str(len(all_sentenceIds)))
print('Reading lemmatized')
with open(LEM) as lem_f:
    lem = [line.strip() for line in lem_f]

print('Reading original')
with open(ORIG) as orig_f:
    orig = [line.strip() for line in orig_f]

print('Reading postag')
with open(POSTAG) as postag_f:
    postags = [line.strip().split(' ') for line in postag_f]

print('organizing')
with open('sentences_dataset.txt', 'w') as out_f, \
        open('sentences_train.txt', 'w') as train_f, \
        open('sentences_pair.txt', 'w') as pair_f:
    for idx in sorted(all_sentenceIds):
        all_pairs = []
        line = str(idx) + '\t'
        line += orig[idx] + '\t'
        line += lem[idx] + '\t'
        if idx in pos_sentences:
            all_pairs.extend(pos_sentences[idx])
            line += json.dumps(pos_sentences[idx]) + '\t'
        else:
            line += '[]' + '\t'
        if idx in neg_sentences:
            all_pairs.extend(neg_sentences[idx])
            line += json.dumps(neg_sentences[idx]) + '\t'
        else:
            line += '[]' + '\t'
        line += '\n'
        out_f.write(line)

        for pair in all_pairs:
            new_tokens = []
            name_a = pair.split(' ')[0]
            name_b = pair.split(' ')[1]
            pair_f.write(str(idx) + '\t' + orig[idx] + '\t' + name_a + '\t' + name_b + '\n')

            valid_idx = set([i for i, pos_tag in enumerate(postags[idx]) if pos_tag in ('NN', 'NNS')])
            tokens = lem[idx].split(' ')
            for i, token in enumerate(tokens):
                if name_a == token and i in valid_idx:
                    new_tokens.append('<E1>')
                elif name_b == token and i in valid_idx:
                    new_tokens.append('<E2>')
                else:
                    new_tokens.append(token)
            train_f.write(' '.join(new_tokens) + '\n')
