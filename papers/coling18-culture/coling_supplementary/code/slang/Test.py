

lines = open("./EN_OOV.tsv").read().split('\n')


for l in lines:
    ls = l.split('\t')
    title = ls[0]
    truth = ls[2]



    print title
    print truth

