FILE = "data/train4134"

with open(FILE + ".txt", encoding="utf-8") as inf, open(FILE + ".sent", 'w', encoding="utf-8") as of:
    for line in inf:
        ls = line.strip().split('\t')
        of.write(ls[1].strip() + '\n')
