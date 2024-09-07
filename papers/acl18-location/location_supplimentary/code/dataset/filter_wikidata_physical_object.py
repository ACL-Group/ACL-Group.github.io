import json


physical_objects_set = set()
with open('physical_objects.json') as json_f:
    physical_objects = json.load(json_f)
    for item in physical_objects['results']['bindings']:
        physical_objects_set.add(item['label']['value'])
print(len(physical_objects_set))

with open('physical_objects_wikidata.txt', 'w') as obj_f:
    for obj in physical_objects_set:
        obj_f.write(obj + '\n')
