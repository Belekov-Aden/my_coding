# 1 Problem
import json
import pprint

first_dict = {

    'login': 'Name',
    'Email': 'com',
    'Age': 9,
    'phone_num': +996

}

second_dict = {

    'login': 'Аден',
    'Email': 'com',
    'Age': 11,
    'phone_num': +990

}

third_dict = {

    'login': 'Исмаил',
    'Email': 'com',
    'Age': 15,
    'phone_num': +995

}

new_spisok = list(zip(first_dict.items(), second_dict.items(), third_dict.items()))
print(new_spisok)

# with open('test_spisok.json', 'w') as w:
#     write = json.dump(new_spisok, w, indent=4)
#     print(w)
#
# with open('test_spisok.json', 'r') as r:
#     read = json.load(r)
#     print(read)


import json
import pprint

with open('character.json', 'r') as f:
    read = json.load(f)
new = {}
c = 0
for i in read['results']:
    new[f'episode{c + 1}'] = i['episode']
    c += 1

pprint.pprint(new)
