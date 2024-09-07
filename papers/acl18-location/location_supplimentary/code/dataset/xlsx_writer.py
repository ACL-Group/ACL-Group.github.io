import os

import xlsxwriter

counter = 0
for filename in os.listdir('label_split'):
    file = os.path.join('label_split', filename)
    print(filename)
    counter += 1
    workbook = xlsxwriter.Workbook(str(counter) + '.xlsx')
    worksheet = workbook.add_worksheet()
    for idx, line in enumerate(open(file, encoding='utf-8')):
        ls = line.strip().split('\t')
        worksheet.write_row(idx, 0, ls)
    workbook.close()
