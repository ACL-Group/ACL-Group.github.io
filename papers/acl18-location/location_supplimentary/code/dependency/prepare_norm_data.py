import os

import networkx as nx
import sys
from pycorenlp import StanfordCoreNLP
from pprint import pprint
import json

subdir = sys.argv[1]
port = sys.argv[2]

nlp = StanfordCoreNLP('http://localhost:{0}'.format(port))


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


def get_stanford_annotations(text, port=9000,
                             annotators='tokenize,ssplit,pos,lemma,depparse,parse'):
    output = nlp.annotate(text, properties={
        "timeout": "10000",
        "ssplit.isOneSentence": "true",
        'annotators': annotators,
    })
    return output

adv_dic = get_vocab_dic('adverbs.txt')
prep1_dic = get_vocab_dic_split('prep-1.txt')
prep2_dic = get_vocab_dic('prep-2.txt')


DIR_NAME = os.path.join('/home/frank/relation/dataset/gutenberg/pair_sentences', subdir)
for filename in os.listdir(DIR_NAME):
    if filename.endswith('.txt'):
        file = os.path.join(DIR_NAME, filename)
        with open(file, encoding='utf-8') as in_file, \
                open(os.path.splitext(file)[0] + '.norm_termab', 'w', encoding='utf-8') as norm_termab_file, \
                open(os.path.splitext(file)[0] + '.pos', 'w', encoding='utf-8') as pos_file, \
                open(os.path.splitext(file)[0] + '.lemma', 'w', encoding='utf-8') as lemma_file:
            print(filename)
            termab = filename.split('.txt')[0]
            token1 = termab.split('_')[0]
            token2 = termab.split("_")[1]

            for line in in_file:
                ls = line.strip().split('\t')
                sent_id = ls[0]
                document = ls[1].strip()

                # The code expects the document to contains exactly one sentence.
                # document = 'The men, crowded upon each other, stared stupidly like a flock of sheep.'
                # print('document: {0}'.format(document))

                # Parse the text
                annotations = get_stanford_annotations(document, port=9000,
                                                       annotators='tokenize,ssplit,pos,lemma,depparse')
                annotations = json.loads(annotations, encoding="utf-8", strict=False)
                tokens = annotations['sentences'][0]['tokens']

                # Load Stanford CoreNLP's dependency tree into a networkx graph
                edges = []
                dependencies = {}
                root_index = annotations['sentences'][0]['basic-dependencies'][0]["dependent"]
                for edge in annotations['sentences'][0]['basic-dependencies']:
                    edges.append((edge['governor'], edge['dependent']))
                    dependencies[(edge['governor'], edge['dependent'])] = edge

                graph = nx.DiGraph(edges)

                # Find the shortest path
                # print(token1)
                # print(token2)
                token_list = [token['originalText'].lower() for token in tokens]
                pos_list = [token['pos'] for token in tokens]
                lemma_list = [token['lemma'].lower() for token in tokens]
                if token1 in lemma_list and token2 in lemma_list:
                    lemma_file.write(' '.join(lemma_list) + '\n')
                    # self-designed sentence normalization
                    # norm changed termab
                    sent_norm = [pos[:2] for pos in pos_list]
                    pos_file.write(' '.join(sent_norm) + '\n')
                    changed = [False] * len(pos_list)
                    changeda = False
                    changedb = False

                    for i, pos in enumerate(pos_list):
                        # change terma and termb
                        if lemma_list[i] == token1 and not changeda:
                            sent_norm[i] = 'terma'
                            changeda = True
                            changed[i] = True
                        elif lemma_list[i] == token2 and not changedb:
                            sent_norm[i] = 'termb'
                            changedb = True
                            changed[i] = True

                        # change verb and nsubj and dobj back
                        elif pos.startswith('V') and not changed[i]:
                            verb = lemma_list[i]
                            sent_norm[i] = verb
                            changed[i] = True
                            for child in graph.successors(i + 1):
                                if dependencies[(i + 1, child)]['dep'] == "nsubj" and not changed[child - 1]:
                                    sent_norm[child - 1] = verb + 'xxs'
                                    changed[child - 1] = True
                                elif dependencies[(i + 1, child)]['dep'] == "dobj" and not changed[child - 1]:
                                    sent_norm[child - 1] = verb + 'xxo'
                                    changed[child - 1] = True
                        # change prep and its father back
                        elif pos.startswith('IN') and not changed[i] and lemma_list[i] in prep1_dic:
                            prep = lemma_list[i]
                            sent_norm[i] = prep
                            changed[i] = True
                            father = graph.predecessors(i + 1)[0]
                            if dependencies[(father, i + 1)]['dep'] == 'case' and not changed[father - 1]:
                                sent_norm[father - 1] = prep + 'xxc'
                                changed[father - 1] = True
                        # change adv and its father back
                        elif pos.startswith('RB') and not changed[i] and lemma_list[i] in adv_dic:
                            adv = lemma_list[i]
                            sent_norm[i] = adv
                            changed[i] = True
                            # father = graph.predecessors(i + 1)[0]
                            # sent_norm[father - 1] = adv + '#predecessor'
                            # changed[father - 1] = True

                    norm_termab_file.write(' '.join(sent_norm) + '\n')
