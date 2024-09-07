from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

stop = set(stopwords.words('english'))
wordnet_lemmatizer = WordNetLemmatizer()
fout = open('AtLocation_en.tsv', 'w')
with open('AtLocation.tsv') as f:
    for line in f:
        line = line.strip()
        ls = line.split('\t')
        start = ls[0]
        end = ls[1]
        weight = ls[2]
        if start.startswith('/c/en/') and end.startswith('/c/en/') and '_' not in start and '_' not in end:
            start_split = start.split('/')
            end_split = end.split('/')
            start_split[3] = wordnet_lemmatizer.lemmatize(start_split[3])
            end_split[3] = wordnet_lemmatizer.lemmatize(end_split[3])
            if start_split[3] not in stop and end_split[3] not in stop:
                fout.write('/'.join(start_split) + '\t' + '/'.join(end_split) + '\t' + str(weight) + '\n')
fout.close()
