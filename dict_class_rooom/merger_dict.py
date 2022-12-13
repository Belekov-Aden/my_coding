my_friends = {
    "Joomart": "+996555246810",
    "Atai": "+996777246810",
    "Aslan": "+996999246810"
}

your_friends = {
    "Adinai": "+996555013579",
    "Ermek": "+996777013579"
}
nomer = {
    'Aden': '+996706100450'
}


# Создание функций для слияние словарей
def merger_dictionary(old_dict, new_dict):
    new = old_dict | new_dict
    print(new)


# Вызов функций 1 аргумент принимает словарь и 2 аргумент тоже самое
merger_dictionary(my_friends, nomer)
