import networkx as nx
from pycorenlp import StanfordCoreNLP
from pprint import pprint
import json

FILE = "data/label5000"

nlp = StanfordCoreNLP('http://localhost:{0}'.format(9000))


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
        open(FILE + '.sst', encoding='utf-8') as sst_file, \
        open(FILE + '.lemma', 'w', encoding='utf-8') as lemma_file, \
        open(FILE + '.compressed', 'w', encoding='utf-8') as compressed_file, \
        open(FILE + '.compressed_sentence', 'w', encoding='utf-8') as compressed_sentence_file, \
        open(FILE + '.compressed_lemma', 'w', encoding='utf-8') as compressed_lemma_file, \
        open(FILE + '.compressed_wordnet', 'w', encoding='utf-8') as compressed_wordnet_file, \
        open(FILE + '.compressed_pos', 'w', encoding='utf-8') as compressed_pos_file, \
        open(FILE + '.compressed_norm_termab', 'w', encoding='utf-8') as compressed_norm_termab_file, \
        open(FILE + '.af', 'w', encoding='utf-8') as af_file, \
        open(FILE + '.af2', 'w', encoding='utf-8') as af2_file, \
        open(FILE + '.norm_space', 'w', encoding='utf-8') as norm_space_file, \
        open(FILE + '.postag', 'w', encoding='utf-8') as postag_file, \
        open(FILE + '.norm_space_termab', 'w', encoding='utf-8') as norm_space_termab_file, \
        open(FILE + '.norm_onlydep_termab', 'w', encoding='utf-8') as norm_onlydep_termab_file, \
        open(FILE + '.norm_termab', 'w', encoding='utf-8') as norm_termab_file:
    ssts = [line.strip().split(' ') for line in sst_file]
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
        sst = ssts[idx]

        # The code expects the document to contains exactly one sentence.
        # document = 'The men, crowded upon each other, stared stupidly like a flock of sheep.'
        # print('document: {0}'.format(document))

        # Parse the text
        annotations = get_stanford_annotations(document, port=9000,
                                               annotators='tokenize,ssplit,pos,lemma,depparse')
        annotations = json.loads(annotations, encoding="utf-8", strict=False)
        tokens = annotations['sentences'][0]['tokens']
        # print(len(tokens), len(sst))
        assert len(tokens) == len(sst)
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

        lemma_file.write(' '.join(lemma_list) + '\n')

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
            # print('path1: {0}'.format(path1))
            # print('path2: {0}'.format(path2))
            descendants1 = list(nx.algorithms.dag.descendants(graph, token1_index))
            descendants2 = list(nx.algorithms.dag.descendants(graph, token2_index))
        except Exception as e:
            print(document)
            print(token1)
            print(token2)
            print(e)
            break

        # compressed sentence
        all_idx = sorted(set(path1 + path2 + descendants1 + descendants2))
        new_idxa = all_idx.index(token1_index)
        new_idxb = all_idx.index(token2_index)
        compressed_position_a = [i - new_idxa for i in range(len(all_idx))]
        compressed_position_b = [i - new_idxb for i in range(len(all_idx))]
        compressed_tokens = [token_list[idx - 1] for idx in all_idx]
        compressed_lemmas = [lemma_list[idx - 1] for idx in all_idx]
        compressed_pos = [pos_list[idx - 1] for idx in all_idx]
        compressed_sst = [sst[idx - 1] for idx in all_idx]
        compressed_list.append(compressed_tokens)
        compressed_file.write(sent_id + '\t' +
                              ' '.join(compressed_tokens) + '\t' +
                              ' '.join(compressed_lemmas) + '\t' +
                              ' '.join(compressed_pos) + '\t' +
                              ' '.join(compressed_sst) + '\t' +
                              ' '.join(map(str, compressed_position_a)) + '\t' +
                              ' '.join(map(str, compressed_position_b)) + '\t' +
                              token1 + '\t' + token2 + '\n')
        compressed_sentence_file.write(' '.join(compressed_tokens) + '\n')
        compressed_lemma_file.write(' '.join(compressed_lemmas) + '\n')
        compressed_pos_file.write(' '.join(compressed_pos) + '\n')
        compressed_wordnet_file.write(' '.join(compressed_sst) + '\n')
        compressed_tokens_set = set(compressed_tokens)
        total_len = len(adv_dic) + len(prep1_dic) + len(prep2_dic)
        af2_vec = [0] * total_len
        for word in adv_dic:
            if word in compressed_tokens_set:
                af2_vec[adv_dic[word]] = 1

        for word in prep1_dic:
            if word in compressed_tokens_set:
                af2_vec[prep1_dic[word]] = 1

        for word in prep2_dic:
            if word in ' '.join(compressed_tokens):
                af2_vec[prep2_dic[word]] = 1

        af2_file.write(sent_id + '\t' + '\t'.join(map(str, af2_vec)) + '\n')

        # self-designed sentence normalization

        # norm space
        sent_norm = [pos[:2] for pos in pos_list]
        changed = [False] * len(pos_list)
        for i, pos in enumerate(pos_list):
            # change verb and nsubj and dobj back
            if pos.startswith('V') and not changed[i]:
                verb = lemma_list[i]
                sent_norm[i] = verb
                changed[i] = True
                for child in graph.successors(i + 1):
                    if dependencies[(i + 1, child)]['dep'] == "nsubj" and not changed[child - 1]:
                        sent_norm[child - 1] = verb + ' xxs'
                        changed[child - 1] = True
                    elif dependencies[(i + 1, child)]['dep'] == "dobj" and not changed[child - 1]:
                        sent_norm[child - 1] = verb + ' xxo'
                        changed[child - 1] = True
            # change prep and its father back
            elif pos.startswith('IN') or pos.startswith('RP') and not changed[i] and lemma_list[i] in prep1_dic:
                prep = lemma_list[i]
                sent_norm[i] = prep
                changed[i] = True
                father = graph.predecessors(i + 1)[0]
                if dependencies[(father, i + 1)]['dep'] == 'case' and not changed[father - 1]:
                    sent_norm[father - 1] = prep + ' xxc'
                    changed[father - 1] = True
            # change adv and its father back
            elif pos.startswith('RB') and not changed[i] and lemma_list[i] in adv_dic:
                adv = lemma_list[i]
                sent_norm[i] = adv
                changed[i] = True
                # father = graph.predecessors(i + 1)[0]
                # sent_norm[father - 1] = adv + '#predecessor'
                # changed[father - 1] = True

        norm_space_file.write(' '.join(sent_norm) + '\n')

        # only postag
        sent_norm = [pos[:2] for pos in pos_list]
        postag_file.write(' '.join(sent_norm) + '\n')

        # norm space changed termab
        sent_norm = [pos[:2] for pos in pos_list]
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
                        sent_norm[child - 1] = verb + ' xxs'
                        changed[child - 1] = True
                    elif dependencies[(i + 1, child)]['dep'] == "dobj" and not changed[child - 1]:
                        sent_norm[child - 1] = verb + ' xxo'
                        changed[child - 1] = True
            # change prep and its father back
            elif pos.startswith('IN') or pos.startswith('RP') and not changed[i] and lemma_list[i] in prep1_dic:
                prep = lemma_list[i]
                sent_norm[i] = prep
                changed[i] = True
                father = graph.predecessors(i + 1)[0]
                if dependencies[(father, i + 1)]['dep'] == 'case' and not changed[father - 1]:
                    sent_norm[father - 1] = prep + ' xxc'
                    changed[father - 1] = True
            # change adv and its father back
            elif pos.startswith('RB') and not changed[i] and lemma_list[i] in adv_dic:
                adv = lemma_list[i]
                sent_norm[i] = adv
                changed[i] = True
                # father = graph.predecessors(i + 1)[0]
                # sent_norm[father - 1] = adv + '#predecessor'
                # changed[father - 1] = True

        norm_space_termab_file.write(' '.join(sent_norm) + '\n')

        # norm only dep changed termab
        sent_norm = [pos[:2] for pos in pos_list]
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
                        sent_norm[child - 1] = 'xxs'
                        changed[child - 1] = True
                    elif dependencies[(i + 1, child)]['dep'] == "dobj" and not changed[child - 1]:
                        sent_norm[child - 1] = 'xxo'
                        changed[child - 1] = True
            # change prep and its father back
            elif pos.startswith('IN') or pos.startswith('RP') and not changed[i] and lemma_list[i] in prep1_dic:
                prep = lemma_list[i]
                sent_norm[i] = prep
                changed[i] = True
                father = graph.predecessors(i + 1)[0]
                if dependencies[(father, i + 1)]['dep'] == 'case' and not changed[father - 1]:
                    sent_norm[father - 1] = 'xxc'
                    changed[father - 1] = True
            # change adv and its father back
            elif pos.startswith('RB') and not changed[i] and lemma_list[i] in adv_dic:
                adv = lemma_list[i]
                sent_norm[i] = adv
                changed[i] = True
                # father = graph.predecessors(i + 1)[0]
                # sent_norm[father - 1] = adv + '#predecessor'
                # changed[father - 1] = True

        norm_onlydep_termab_file.write(' '.join(sent_norm) + '\n')

        # norm changed termab
        sent_norm = [pos[:2] for pos in pos_list]
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
            elif pos.startswith('IN') or pos.startswith('RP') and not changed[i] and lemma_list[i] in prep1_dic:
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
        compressed_norm_termab_sent = []
        for i in all_idx:
            compressed_norm_termab_sent.append(sent_norm[i - 1])
        compressed_norm_termab_file.write(' '.join(compressed_norm_termab_sent) + '\n')

        # data for PKU baseline
        left1 = []
        left2 = []
        left3 = []
        leftGR = []
        leftPOS = []
        leftWN = []
        right1 = []
        right2 = []
        right3 = []
        rightGR = []
        rightPOS = []
        rightWN = []

        sdpW = []
        sdpPOS = []
        sdpWN = []
        for token_id in path1:
            token = tokens[token_id - 1]
            token_text = token['word']
            left1.append(token_text + '-' + str(token_id - 1))

        for token_id in path2:
            token = tokens[token_id - 1]
            token_text = token['word']
            right1.append(token_text + '-' + str(token_id - 1))

        for token_id in sdp:
            token = tokens[token_id - 1]
            token_text = token['word']
            sdpW.append(token_text)
            sdpPOS.append(token['pos'])

        r_path1 = reversed(path1)
        r_path2 = reversed(path2)
        for token_id in r_path1:
            token = tokens[token_id - 1]
            token_text = token['word']
            left2.append(token_text)
            left3.append(token_text)
            leftPOS.append(token['pos'])
            leftWN.append(sst[token_id - 1])

        for token_id in r_path2:
            token = tokens[token_id - 1]
            token_text = token['word']
            right2.append(token_text)
            right3.append(token_text)
            rightPOS.append(token['pos'])
            rightWN.append(sst[token_id - 1])

        GR_path1 = reversed(list(zip(path1, path1[1:])))
        GR_path2 = reversed(list(zip(path2, path2[1:])))
        for e in GR_path1:
            leftGR.append(dependencies[e]["dep"].split(':')[0])
        for e in GR_path2:
            rightGR.append(dependencies[e]["dep"].split(':')[0])

        # for additional features v2
        propL = [word for idx, word in enumerate(left3) if leftPOS[idx].startswith("IN")]
        propR = [word for idx, word in enumerate(right3) if rightPOS[idx].startswith("IN")]
        propS = [word for idx, word in enumerate(sdpW) if sdpPOS[idx].startswith("IN")]
        propLD = [token_list[idx - 1] for idx in descendants1 if pos_list[idx - 1].startswith("IN")]
        propRD = [token_list[idx - 1] for idx in descendants2 if pos_list[idx - 1].startswith("IN")]

        advL = [word for idx, word in enumerate(left3) if leftPOS[idx].startswith("RB")]
        advR = [word for idx, word in enumerate(right3) if rightPOS[idx].startswith("RB")]
        advS = [word for idx, word in enumerate(sdpW) if sdpPOS[idx].startswith("RB")]
        advLD = [token_list[idx - 1] for idx in descendants1 if pos_list[idx - 1].startswith("RB")]
        advRD = [token_list[idx - 1] for idx in descendants2 if pos_list[idx - 1].startswith("RB")]

        nounL = [word for idx, word in enumerate(left3) if leftPOS[idx].startswith("NN")]
        nounR = [word for idx, word in enumerate(right3) if rightPOS[idx].startswith("NN")]
        nounS = [word for idx, word in enumerate(sdpW) if sdpPOS[idx].startswith("NN")]
        nounLD = [token_list[idx - 1] for idx in descendants1 if pos_list[idx - 1].startswith("NN")]
        nounRD = [token_list[idx - 1] for idx in descendants2 if pos_list[idx - 1].startswith("NN")]

        af_file.write(sent_id + '\t' + str(len(propL)) + '\t' + str(len(propR)) + '\t' + str(len(propS)) + '\t' +
                      str(len(propLD)) + '\t' + str(len(propRD)) + '\t' + str(len(advL)) + '\t' +
                      str(len(advR)) + '\t' + str(len(advS)) + '\t' + str(len(advLD)) + '\t' + str(len(advRD)) + '\t' +
                      str(len(nounL)) + '\t' + str(len(nounR)) + '\t' + str(len(nounS)) + '\t' +
                      str(len(nounLD)) + '\t' + str(len(nounRD)) + '\t' + str(len(sdp)) + '\n')

        data.append([left1, right1, left2, right2, left3, right3, leftPOS, rightPOS, leftGR, rightGR, leftWN, rightWN])

    with open(FILE + '.json', 'w', encoding='utf-8') as jf, \
            open(FILE + '_label.json', 'w', encoding='utf-8') as ljf, \
            open(FILE + '_compressed.json', 'w', encoding='utf-8') as cjf:
        json.dump(data, jf)
        json.dump(labels, ljf)
        json.dump(compressed_list, cjf)
