NAACL-HLT Submission #75 Supplementary Materials


# resources

1. Data we used in this paper
1.1. the Bilingual Lexicon from Bing Translator (dict.json)
1.2. the English and Chinese Socio-linguistic Lexicon (esv_opinonfinder.txt, esv_selected_empathy.txt, initial_csv_textmind.txt)
1.3. English slang glossary (en_slang.tsv slang t explanation t extracted target terms t google result t bing result t baidu result)
1.3. Chinese slang glossary (cn_slang.tsv slang t google result t bing result t baidu result t CC-CEDIT extracted terms t explanation t extracted target terms
1.4. ablation test resources: adj.lex / noun.lex / verb.lex / random.lex with similar sizes

2. Dataset we collected
2.1. the Bilingual Socio-linguistic Lexicon (full_bsl.lex a extend BSL without filtering by csv; a filtered smaller one can be obtained by using above three resources. )
2.2. the averaged cross-cultural differences scores dataset between named entities from human annotators; (cdiff_label_score_avg.txt)
2.3. the 700 entity pairs (entity_pairs.txt)
2.4. the word lists for each entity part (labeler_entitypair.csv and labeler_related.csv)


3. Experimental results
3.1. the cross-cultural differences scores computed from our SocVec (socvec_cdiff_res_best.txt)
3.2. SocVec based results of Chinese Slang to English common words (cnslang2en.txt)
3.3. SocVec based results of English Slang to Chinese common words (enslang2cn.txt)


# code (we will release more friendly prototype tools based on the codes that we used for conducting experiments)
generate_pseudo_embeddings/*.py (used for generate BSL psudo vectors)
socvec_and_evaluation/*.py (used for generate socvec and Task 1 related experiments)
slang/*.py (used for slang (Task 2) related experiments)
