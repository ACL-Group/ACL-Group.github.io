import os
import random

from openpyxl import load_workbook

random.seed(123123)

all_labeled_data = []
for filename in os.listdir('to_label'):
    if filename.endswith('_done.xlsx'):
        file = os.path.join('to_label', filename)
        print(filename)
        workbook = load_workbook(file, read_only=True)
        ws = workbook.active
        for row in ws.rows:
            assert len(row) == 5
            all_labeled_data.append([cell.value for cell in row])

with open('label/label1000.txt', encoding='utf-8') as lf:
    for line in lf:
        all_labeled_data.append(line.strip().split('\t'))

print(len(all_labeled_data))

random.shuffle(all_labeled_data)

with open('label/label3000.txt', 'w', encoding='utf-8') as of:
    for line in all_labeled_data:
        of.write('\t'.join(map(str, line)) + '\n')
