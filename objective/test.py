# class Restaurant:
#     ''''Name and last name'''
#
#     def __init__(self, restaurant_name, cuisine_type):
#         self.name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_serverd = 0
#
#     def describe_restaurant(self):
#         print(f'Name: {self.name}\nType: {self.cuisine_type}')
#
#     def open_restaurant(self):
#         print(f'Open')
#
#     def set_number_served(self, number):
#         if number >= self.number_serverd:
#             self.number_serverd = number
#         pass
#
#     def increment_number_served(self, number):
#         self.number_serverd += number
#
#
# #
# # restaurant = Restaurant('Dodo', 'pizza')
# # restaurant.describe_restaurant()
#
#
# class IceCreamStand(Restaurant):
#
#     def __init__(self, restaurant_name, cuisine_type):
#         super().__init__(restaurant_name, cuisine_type)
#         self.flavors = ['Magnum Unilever Group',
#                         'Haagen Dazs General Mills Inc',
#                         'Cornetto Unilever Group',
#                         'Ben & Jerry Unilever Group',
#                         'Breyers (Unilever Group)',
#                         'Carte D Unilever Group',
#                         'Dreyer Nestle SA',
#                         'Blue Bunny Wells Enterprises'
#                         ]
#
#     def ice_cream_all(self):
#         print(f'We have {self.flavors}')
#
#
# # icecreamstand = IceCreamStand('FDSsd', 'dfsdsf')
# # icecreamstand.ice_cream_all()
#
#
# class User:
#
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.login_attempts = 0
#
#     def describe_user(self):
#         print(f'Name: {self.first_name}\nLast name: {self.last_name}')
#
#     def greet_user(self):
#         print(f'Hello {self.first_name}')
#
#     def increment_login_attempts(self):
#         self.login_attempts += 1
#
#     def reset_login_attempts(self):
#         self.login_attempts = 0
#
#
# # aden = User('Aden', 'Belekov')
#
#
# class Privileges():
#
#     def __init__(self):
#         self.privileges = [
#             "разрешено добавлять сообщения",
#             "разрешено удалять пользователей",
#             "разрешено банить пользователей",
#             "просмотр админов",
#             "дать мут"
#         ]
#
#     def show_privileges(self):
#         print(f'Привилегий админу {self.privileges}')

# class Admin(User):
#
#     def __init__(self, first_name, last_name):
#         super().__init__('Admin', '')
#         self.privileges = Privileges()
# #
#
# admin = Admin('Admin', '')
# admin.describe_user()
# admin.privileges.show_privileges()

# class Car():
#     """Простая модель автомобиля."""
#
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
#
#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} miles on it.")
#
#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")
#
#     def increment_odometer(self, miles):
#         self.odometer_reading += miles


# camry = Car('Japan', 'Camry', 1998)
# print(camry.get_descriptive_name())
# camry.read_odometer()
#
#
# class Battery():
#     """Простая модель аккумулятора электромобиля."""
#
#     def __init__(self, battery_size=75):
#         """Инициализирует атрибуты аккумулятора."""
#         self.battery_size = battery_size
#
#     def describe_battery(self):
#         "Выводит информацию о мощности аккумулятора."""
#         print(f"This car has a {self.battery_size}-kWh battery.")
#
#     def get_range(self):
#         """Выводит приблизительный запас хода для аккумулятора."""
#         if self.battery_size == 75:
#             range = 260
#         elif self.battery_size == 100:
#             range = 315
#
#         print(f"This car can go about {range} miles on a full charge.")
#
#     def upgrade_battery(self):
#         if self.battery_size != 100:
#             self.battery_size = 100
#
#
# class ElectroCar(Car):
#
#     def __init__(self, make, model, year):
#         super().__init__(make, model, year)
#         self.battary_size = Battery()
#
#
# tesla = ElectroCar('tesla', 'tesla x50', 2021)
# tesla.battary_size.get_range()
# tesla.battary_size.upgrade_battery()
# tesla.battary_size.get_range()
# tesla.battary_size.describe_battery()


# from random import randint
#
#
# class Die():
#     sides = 6
#
#     def roll_die(self):
#         for i in range(10):
#             print(randint(1, self.sides))
#
#
# ver = Die()
# 6 гранный кубик
# ver.roll_die()

# кубик с 10 гранью
# ver.side = 10
# ver.roll_die()

# ver.sides = 20
# ver.roll_die()

# from random import choice, sample
#
# lottery = ('5', '9', '1', '4', '8', '2', '3', '0', '7', '6', 'a', 'd', 't', 'o', 'q')
# win_lottery = []
# for i in range(4):
#     win_lottery.append(choice(lottery))
#
# print(f'Эта комбинация являяется победительным: {win_lottery}')
#
# number_combinations = 0
# while True:
#     win_lottery != sample(lottery, 4)
#     number_combinations += 1
#     if win_lottery == sample(lottery, 4):
#         print("You win!")
#         print("The winning combination was: {}".format(number_combinations))
#         break
