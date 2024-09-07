words = []
sent_len = []

with open("semeval2010.txt", encoding="utf-8") as inf, open("label5000.sent", 'w', encoding="utf-8") as of:
    for line in inf:
        ls = line.strip().split('|')
        tokens = ls[3].split()
        words.extend([len(token) for token in tokens])
        sent_len.append(len(tokens))

print(sum(words)/len(words))
print(sum(sent_len)/len(sent_len))
