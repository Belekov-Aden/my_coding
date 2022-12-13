# # 2
# Furniture:
# Тип дома, общая площадь и перечень наименований мебели В новом доме совсем нет мебели.
# Мебель имеет название и площадь, из которых Спальня: 4 квадратных метра Гардероб: 2 квадратных метра Стол: 1,5 квадратных метра.
# Добавьте в дом три вышеупомянутых предмета мебели.
# При печати дома требуются следующие данные: тип дома, общая площадь, оставшаяся площадь, список названий мебели.
from typing import Union


class Room():

    def __init__(self, typehouse: str, squarehouse: Union[int, float]):
        self.typehouse = typehouse
        self.squarehouse = squarehouse
        self.furnitur = {}

    def get(self):
        s = 0
        for i in self.furnitur.values():
            s += i
        return f'Type House:{self.typehouse}\nSquare House:{self.squarehouse}\nWith furniture:{self.squarehouse - s}\nNames furnitue: {self.furnitur.keys()}'

    def add(self, furniture: str, square: Union[int, float]):
        self.furnitur[furniture] = square


kitchen = Room('Kitchen', 50)

kitchen.add('Спальня', 4)
kitchen.add('гардероб', 2)
kitchen.add('стол', 1.5)

print(kitchen.get())
