import statistics

def read_rank(infile, ranks):
    print(infile)
    with open(infile) as fin:
        for idx, line in enumerate(fin):
            info = line.strip().split('\t')
            ranks[info[0]].append(idx + 1)
    return ranks


def init_rank():
    ranks = {}
    pairs = {}
    with open('eval.set') as fpair:
        for line in fpair:
            info = line.strip().split('\t')
            pairs[info[0]] = {'en': info[1], 'zh': info[2]}
            ranks[info[0]] = []
    return ranks, pairs


if __name__ == '__main__':
    ranks, pairs = init_rank()
    files = ["cat.gdim.l2.res.0211",
             "cat.gdim.l1.res.0211",
             "cat.dim.l2.res.0211",
             "cat.dim.l1.res.0211",
            "emp.gdim.l2.res.0211",
             "emp.gdim.l1.res.0211",
             "emp.dim.l2.res.0211",
             "emp.dim.l1.res.0211",
             "opn.gdim.l2.res.0208",
             "opn.gdim.l1.res.0208",
             "opn.dim.l1.res.0211",
             "opn.dim.l2.res.0211",
             "all.l1.res.0211",
             "all.l2.res.0211",
             "lt_0211.res",
             "baseline.res"]
    for file in files:
        ranks = read_rank(file, ranks)
    final_rank = {}
    for entity in ranks:
        final_rank[entity] = statistics.mean(ranks[entity])
    rank_sort = sorted(final_rank, key = final_rank.get)
    with open('average.res', 'w') as fout:
        for w in rank_sort:
            fout.write(w + '\t' + pairs[w]['en'] + '\t' + pairs[w]['zh'] + '\t' + str(final_rank[w]) + '\n')

