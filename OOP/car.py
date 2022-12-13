class Car():
    '''Класс car с приватными методами для работы с аргументами!'''

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
        self.fuel = 70  # литра

    def __add_distance(self, r):
        self.odometer += r

    def __sub_fuel(self, r):
        self.fuel -= r

    def drive(self, r):
        if self.fuel >= r:
            self.__add_distance(r)
            self.__sub_fuel(r)
            print(f'Let`s drive\n{self.__dict__}')

        else:
            print(f'Need more fuel, please, fill more!\n{self.__dict__}')


a = Car('Japan', 'JZD', 2022)
a.drive(100)
