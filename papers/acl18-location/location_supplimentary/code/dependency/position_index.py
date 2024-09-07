FILE5w = 'data/sentences_50k'
FILE1000 = 'data/label1000'


def get_vocab_dic_split(filename):
    with open(filename) as inf:
        vocab = {}
        words = [line.strip().split() for line in inf]
        for index, word in enumerate(words):
            for w in word:
                vocab[w] = index
        return vocab


def get_vocab_dic(filename):
    with open(filename) as inf:
        vocab = {}
        words = [line.strip() for line in inf]
        for index, word in enumerate(words):
            vocab[word] = index
        return vocab

adv_dic = get_vocab_dic('adverbs.txt')
prep1_dic = get_vocab_dic_split('prep-1.txt')
prep2_dic = get_vocab_dic('prep-2.txt')

with open(FILE5w + '.txt', encoding='utf-8') as in_f, \
     open(FILE5w + '.lemma', encoding='utf-8') as lemma_f, \
     open(FILE5w + '.posa', 'w', encoding='utf-8') as ofa, \
     open(FILE5w + '.posb', 'w', encoding='utf-8') as ofb:
    posa = []
    posb = []
    for line1, line2 in zip(in_f, lemma_f):
        ls = line1.strip().split('\t')
        terma = ls[2]
        termb = ls[3]
        lemma_sent = line2.strip()
        tokens = line1.strip().split()
        terma_idx = tokens.index('terma')
        termb_idx = tokens.index('termb')
        position_a = []
        position_b = []
        for idx, token in enumerate(tokens):
            position_a.append(idx - terma_idx)
            position_b.append(idx - termb_idx)
        posa.append(position_a)
        posb.append(position_b)
    ofa.write('\n'.join([' '.join(map(str, line)) for line in posa]))
    ofb.write('\n'.join([' '.join(map(str, line)) for line in posb]))

with open(FILE1000 + '.txt', encoding='utf-8') as in_f, \
        open(FILE1000 + '.posa', 'w', encoding='utf-8') as ofa, \
        open(FILE1000 + '.posb', 'w', encoding='utf-8') as ofb:
    posa = []
    posb = []
    for line in in_f:
        tokens = line.strip().split()
        terma_idx = tokens.index('terma')
        termb_idx = tokens.index('termb')
        position_a = []
        position_b = []
        for idx, token in enumerate(tokens):
            position_a.append(idx - terma_idx)
            position_b.append(idx - termb_idx)
        posa.append(position_a)
        posb.append(position_b)
    ofa.write('\n'.join([' '.join(map(str, line)) for line in posa]))
    ofb.write('\n'.join([' '.join(map(str, line)) for line in posb]))
