import json

with open('ttt_id.json') as json_file:
    id_list = json.load(json_file)
    train_id_list = id_list[0]
    val_id_list = id_list[1]
    test_id_list = id_list[2]

ind = 0
f1 = open('training600.norm2', 'w')
f2 = open('tuning200.norm2', 'w')
f3 = open('test200.norm2', 'w')
for l in open('data/NORM/label1000.norm2').read().split('\n'):
    # print ls
    if len(l) > 1:
        if ind in train_id_list:
            f1.write(l + '\n')
        elif ind in val_id_list:
            f2.write(l + '\n')
        elif ind in test_id_list:
            f3.write(l + '\n')
        ind += 1
f1.close()
f2.close()
f3.close()
