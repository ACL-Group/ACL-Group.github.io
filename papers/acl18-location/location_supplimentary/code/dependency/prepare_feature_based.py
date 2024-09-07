import networkx as nx
from pycorenlp import StanfordCoreNLP
from pprint import pprint
import json
import numpy as np
from scipy.spatial.distance import cosine

FILE = "data/label5000"

nlp = StanfordCoreNLP('http://localhost:{0}'.format(9000))

GLOVE_EMD_FILE = '/home/frank/relation/classifier/data/EMD/glove.6B.100d.txt'
CORPUS_EMD_FILE = '/home/frank/relation/classifier/data/EMD/all_50.emd'

embeddings_index_glove = {}
with open(GLOVE_EMD_FILE, encoding='utf-8') as f:
    for line in f:
        values = line.split(' ')
        word = values[0]
        embedding = np.asarray(values[1:], dtype='float32')
        embeddings_index_glove[word] = embedding

embeddings_index_corpus = {}
with open(GLOVE_EMD_FILE, encoding='utf-8') as f:
    for line in f:
        values = line.split(' ')
        word = values[0]
        embedding = np.asarray(values[1:], dtype='float32')
        embeddings_index_corpus[word] = embedding


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


with open(FILE + '.txt', encoding='utf-8') as in_file, \
        open(FILE + '.features', 'w', encoding='utf-8') as af3_file:
    data = []
    labels = []
    compressed_list = []
    adv_dic = get_vocab_dic('adverbs.txt')
    prep1_dic = get_vocab_dic_split('prep-1.txt')
    prep2_dic = get_vocab_dic('prep-2.txt')

    for idx, line in enumerate(in_file):
        if idx % 1000 == 0:
            print(idx)
        ls = line.strip().split('\t')
        sent_id = ls[0].strip()
        document = ls[1].strip()
        token1 = ls[2]
        token2 = ls[3]
        label = ls[4]
        labels.append(int(label))

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
        graph_undir = nx.Graph(edges)

        # Find the shortest path
        # print(token1)
        # print(token2)
        token_list = [token['originalText'].lower() for token in tokens]
        pos_list = [token['pos'] for token in tokens]
        lemma_list = [token['lemma'].lower() for token in tokens]

        token1_index = -1
        token2_index = -1

        for token in tokens:
            if token1 == token['lemma'].lower():
                token1_index = token['index']
                break
        for token in tokens:
            if token2 == token['lemma'].lower():
                token2_index = token['index']
                break

        try:
            path1 = nx.shortest_path(graph, source=root_index, target=token1_index)
            path2 = nx.shortest_path(graph, source=root_index, target=token2_index)
            sdp = nx.shortest_path(graph_undir, source=token1_index, target=token2_index)
            descendants1 = list(nx.algorithms.dag.descendants(graph, token1_index))
            descendants2 = list(nx.algorithms.dag.descendants(graph, token2_index))
        except Exception as e:
            print(document)
            print(token1)
            print(token2)
            print(e)
            break
        total_len = len(adv_dic) + len(prep1_dic) + len(prep2_dic)
        af2_vec = [0] * total_len
        for word in adv_dic:
            if word in token_list:
                af2_vec[adv_dic[word]] = 1

        for word in prep1_dic:
            if word in token_list:
                af2_vec[prep1_dic[word]] = 1

        for word in prep2_dic:
            if word in ' '.join(token_list):
                af2_vec[prep2_dic[word]] = 1

        #global_features
        af2_vec.append(len(lemma_list))
        af2_vec.append(len([pos for pos in pos_list if pos.startswith('NN')]))
        af2_vec.append(len([pos for pos in pos_list if pos.startswith('VB')]))
        af2_vec.append(len([pos for pos in pos_list if pos.startswith('RB')]))
        af2_vec.append(len([pos for pos in pos_list if pos.startswith('JJ')]))
        af2_vec.append(len([pos for pos in pos_list if pos.startswith('DT')]))
        af2_vec.append(len([pos for pos in pos_list if pos.startswith('IN') or pos.startswith('RP')]))
        af2_vec.append(len([pos for pos in pos_list if pos in ('$', '``', "''", '(', ')', ',', '--', ':')]))

        #shortest path
        sdp_pos = [pos_list[i - 1] for i in sdp]
        af2_vec.append(len(sdp))
        af2_vec.append(len([pos for pos in sdp_pos if pos.startswith('NN')]))
        af2_vec.append(len([pos for pos in sdp_pos if pos.startswith('VB')]))
        af2_vec.append(len([pos for pos in sdp_pos if pos.startswith('RB')]))
        af2_vec.append(len([pos for pos in sdp_pos if pos.startswith('JJ')]))
        af2_vec.append(len([pos for pos in sdp_pos if pos.startswith('DT')]))
        af2_vec.append(len([pos for pos in sdp_pos if pos.startswith('IN') or pos.startswith('RP')]))
        af2_vec.append(len([pos for pos in sdp_pos if pos in ('$', '``', "''", '(', ')', ',', '--', ':')]))

        # Glove similarity
        terma_vec = embeddings_index_glove[token1]
        termb_vec = embeddings_index_glove[token2]
        af2_vec.append(1 - cosine(terma_vec, termb_vec))

        terma_vec = embeddings_index_corpus[token1]
        termb_vec = embeddings_index_corpus[token2]
        af2_vec.append(1 - cosine(terma_vec, termb_vec))

        af3_file.write(sent_id + '\t' + '\t'.join(map(str, af2_vec)) + '\n')
