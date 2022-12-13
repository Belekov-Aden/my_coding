# Словарь
dict1 = {'a': 5, 'b': 3, 'c': 8, 'd': 14}
dict2 = {'a': 33, 'b': 3, 'c': 5, 'd': 15}


def key_values(a):
    print(a)
    for i in a.items():
        if i[1] % 3 == 0:
            print(f'{i[0]} = Hi')

        elif i[1] % 5 == 0:
            print(f'{i[0]} = Bye')


key_values(dict1)
key_values(dict2)
