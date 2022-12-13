#City список

from termcolor import colored, cprint

city = ['1. Добавить новый город',
'2. Отобразить список городов',
'3. Заменить город',
'4. Удалить город',
'5. Выход']

new_city = []

while True:
    print('\n'.join(city))

    answer = int(input(colored('\nВыберите действие: ', 'blue', attrs=['bold'])))

    if answer == 1:
        city_new = input('\nКакой город хотите добавить?: ')
        if city_new in new_city:
            print(colored('Такой город уже есть!\n', 'red', attrs=['reverse']))
        else:

            new_city.append(city_new)

            print(colored('Город успешно добавлен', 'green', attrs=['bold', 'reverse']))




    if answer == 2:
        print(f'Ваш список город (ов) \n{new_city}\n')






    if answer == 3:
        name_city_new = input('Какой город хотите заменить?: ')
        if name_city_new in new_city:
            new_city.remove(name_city_new)
            new_town = input('\nВведите новый город!:')
            new_city.append(new_town)
            print(colored('\nВаш новый список города \n{0}'.format(new_city), 'red'))

        else:
            print('Такого города нету!')






    if answer == 4:
        delete_in_city = input(f'Ваш данный список \n {new_city} \n Какой город хотите удалить?')

        if delete_in_city in new_city:
            new_city.remove(delete_in_city)
            print(f'Ваш город удален \n {new_city}')

        else:
            print('Такого города нету!')





    if answer == 5:
        print('Программа завершает работу!')
        break
    else:
        pass



