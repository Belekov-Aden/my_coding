# delattr - setattr - getattr - getattribute -  ########################################################
# class Some:
#     mincord = 10
#     maxcord = 20
#
#     def __delattr__(self, item):
#         print('Удален артибут ' + item)
#         object.__delattr__(self, item)
#
#     # def __getattr__(self, item):
#     #     return 'Нету такого артибута!'
#
#     def __setattr__(self, key, value):
#         if key == 'zz':
#             raise ValueError('Доступ Запрещен')
#
#         object.__setattr__(self, key, value)
#
#     def __getattribute__(self, item):
#         if item == 'mincord':
#             raise ValueError('Доступ Запрещен')
#         return object.__getattribute__(self, item)


# a = Some()
# setattr(a, 'name', 'Aden')
# print(getattr(a, 'maxcord'))

# a.zz = 20
# print(a.__dict__)
# print(a.__dict__)
# print(getattr(a, 'z'))
# del a.zz
# print(a.__dict__)
## delattr - setattr - getattr - getattribute -  ########################################################
#
### __rerp__            __call__            __str___  ###
# class A:
#     def __init__(self):
#         self.__chet = 0
#
#     def __call__(self, *args, **kwargs):
#         print('HI')
#         self.__chet += 1
#         return self.__chet
#
#     def __repr__(self):
#         return f'it`s our class {self.__class__}'
#
#     #
#     def __str__(self):
#         return 'it is string'
#
#
# num = A()
# num()  # call
# print(num())  # call
# print(num)  # __str__
# print(repr(num))  # __repr__
#
# class Cleaner:
#     def __init__(self, symvol):
#         self.__symvol = symvol
#
#     def __call__(self, *args, **kwargs):
#         if not isinstance(args[0], str):
#             raise TypeError('Will be only strings')
#         return ''.join(char for char in args[0] if char not in self.__symvol)
#
#
# text = Cleaner("1")
#
# print(text('ПРивет 1111 11апваоопва 11'))
### __rerp__            __call__            __str___  ###


### @classmethod @staticmathod @property ###
# class CallPhone:
#     def __init__(self, brand, number):
#         self.__brand = brand
#         self.__number = number
#
#     def get_number(self):
#         return self.__number
#
#     @staticmethod
#     def call():
#         return 911
#
#     @classmethod
#     def mobile(cls, num):
#         _num = cls('Apple', num)
#         print('apple created')
#         return _num
#
#
# phone = CallPhone('Apple', 14)
# print(phone.mobile(1))
# # print(phone.get_number())
# # print(phone.call())
#
#
# from datetime import datetime as dt
#
#
# class Player:
#     __LVL, __HEALTH = 1, 100
#     __slots__ = ['__lvl', '__health', '__born']
#
#     def __init__(self):
#         self.__lvl = Player.__LVL
#         self.__health = Player.__HEALTH
#         self.__born = dt.now()
#
#     @property
#     def lvl(self):
#         return self.__lvl, f'{dt.now() - self.__born}'
#
#     @lvl.setter
#     def lvl(self, num):
#         self.__lvl += num
#         if self.__lvl >= 100: self.__lvl = 100
#
#     @classmethod
#     def set_new_player(cls, lvl=1):
#
#         cls.__LVL = Player.__cheking(lvl)
#
#     @staticmethod
#     def __cheking(value):
#         if isinstance(value, int):
#             return value
#         raise TypeError('Must be int')
#
#
# x = Player()
# print(x.lvl)
#
# y = Player()
# print(y.lvl)
#
# Player.set_new_player(10)
# e = Player()
# print(e.lvl)
#
# Player.set_new_player()
# t = Player()
# print(t.lvl)
#
# class Time:
#     __day = 86400  # число в секундах
#
#     def __init__(self, seconds: int):
#         if not isinstance(seconds, int):
#             raise TypeError('Type only int')
#         self.seconds = seconds % self.__day  # 00: 00 : 00
#
#     def chech_time(self):
#         s = self.seconds % 60
#         m = (self.seconds // 60) % 60
#         h = (self.seconds // 3600) % 24
#         return f'{self.__formatter(h)}:{self.__formatter(m)}:{self.__formatter(s)}'
#
#     @classmethod
#     def __formatter(cls, x):
#         return str(x).rjust(2, '0')
#
#     def __add__(self, other):
#         return Time(self.seconds + other)
#
#     def __sub__(self, other):
#         return Time(self.seconds - other)
#
#     def __radd__(self, other):
#         return Time(self.seconds + other)
#
#
# x = Time(60)
# x += 1000
# x -= 1000
# print(x.chech_time())
#
### @classmethod @staticmathod @property ###
# class Point:
#
#     def __init__(self, *args):
#         self.__cooper = args
#
#     def __len__(self):
#         return len(self.__cooper)
#
#     def __abs__(self):
#         return list(map(abs, self.__cooper))
#
#
# a = Point(-1, -35, -353, -24)
# print(abs(a))

# МНОЖЕСТВЕННОЕ НАСЛЕДОВАНИЕ ########################################################
# class Dog:
#
#     def bark(self):
#         print('Gav Gav')
#
#     def eat(self):
#         print('Хочу кости')

# class Cat:
#     def meow(self):
#         print('Мяу мяу')
#
#     def eat(self):
#         print('Хочу кушать ксс')
#
#
# class Cat_Dog(Cat, Dog):
#     def eat(self):
#         print('ktps')
#         super().eat()  # делегирование
#         Dog.eat(self)
#
#
# ktps = Cat_Dog()
# ktps.eat()
# # МНОЖЕСТВЕННОЕ НАСЛЕДОВАНИЕ ########################################################
