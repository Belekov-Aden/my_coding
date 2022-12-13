# Высокие значения в словаре
high_numbers = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20, 'w': 10_000}
print(f'Старое значение {high_numbers}\n')
# в новую переменную ссылаемся на класс dict.keys
new = list(high_numbers.items())

# Сортировка list, анонимной функцией по убыванию
new_really = sorted(new, key=lambda number: number[1], reverse=True)

# Получаем первые три больших числа
full = dict(new_really[:3:])

# Ссылаемся на новый обьект(по условию сохранить в новую переменную КЛЮЧИ)
keys_high = list(full.keys())
print(f'Новый список с ключом и значением\n{full}')

# Удалить эти значение в старом dict
for elem in keys_high:
    del high_numbers[elem]

print(f'\nУдаленный словарь {high_numbers}')
