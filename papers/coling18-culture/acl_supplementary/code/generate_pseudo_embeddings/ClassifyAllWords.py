from nltk.corpus import wordnet as wn






nouns = set()
for synset in list(wn.all_synsets('n')):
    for l in synset.lemmas():
        nouns.add(l.name())

print len(nouns)


verbs = set()
for synset in list(wn.all_synsets('v')):
    for l in synset.lemmas():
        verbs.add(l.name())

print len(verbs)

adjs = set()
for synset in list(wn.all_synsets('a')):
    for l in synset.lemmas():
        adjs.add(l.name())

print len(adjs)


all_eng = set(open("all_eng.txt").read().split('\n'))

nouns = set.intersection(nouns, all_eng)
verbs = set.intersection(verbs, all_eng)
adjs = set.intersection(adjs, all_eng)


print len(nouns)
print len(verbs)
print len(adjs)

open('verb.lex', 'w').write("\n".join(list(verbs)))
open('adj.lex', 'w').write("\n".join(list(adjs)))