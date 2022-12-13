import datetime
from sys import exit

car_park = {

}

print('Добро пожаловать в Car Park\nВсе места свободны паркуйтесь!\n')


def login_car():
    log_car = input('1 - Припаркавать\n2 - Выехать\n3 - Места на парковке:\n4 - Выйти:\n:')

    if log_car == '1':
        while True:
            if len(car_park) == 5:
                print('Все места заняты!\n')
                return login_car()

            car = input('Название вашей машины: ')

            def car_parking():

                car_park[car] = datetime.datetime.now()
                print(f'{car_park}\n')

                return login_car()

            car_parking()

    if log_car == '2':
        while True:
            if len(car_park) == 0:
                print('Парковка пустая\n')
                return login_car()

            log_index = input('Название вашей машины: ')

            def car_out_park():
                if log_index in car_park:
                    pay = (datetime.datetime.now() - car_park.get(log_index))
                    car_park.pop(log_index)
                    print(f'Вы должны оплатить {pay.seconds * 0.05} som {log_index}!')
                    return login_car()
                else:

                    print('Нету такой машины!\n')
                    return login_car()

            car_out_park()

    if log_car == '3':
        place_car_park = len(car_park)
        if place_car_park == 5:
            print('Все места заняты!')

        else:

            print(f'В парке есть свободных мест {5 - place_car_park}\n')
            return login_car()

    if log_car == '4':
        exit()


login_car()
