# # 4
# Dollar
# Создайте функцию dollarize (), которая принимает Float и возвращает долларовый формат:

# Copy
# dollarize(123456.78901) -> "$123,456.80"
# dollarize(-123456.7801) -> "-$123,456.78"
# dollarize(1000000) -> "$1,000,000"

# Преобразуйте эту функцию в полезный класс MoneyFmt. MoneyFmt содержит одно значение данных (количество) и 4 метода.
# Copy
#     "init" //конструктор инициализирует значение данных
#     "update" //метод заменяет значение данных новым
#     "repr" //методы возвращают значение с плавающей запятой
#     "str" //метод, реализующий логику метода dollarize ()

# Copy
# //Результат будет выглядеть так:
# import moneyfmt
# cash = moneyfmt.MoneyFmt(12345678.021)
# print(cash) -- returns "$12,345,678.02"
# cash.update(100000.4567)
# print(cash) -- returns "$100,000.46"
# cash.update(-0.3)
# print(cash) -- returns "-$0.30"
# repr(cash) -- returns -0.3

from humanize import intcomma


def dollarize(dollars):
    if dollars < 0:
        return f"-${intcomma(dollars).replace('-', '').replace('.', ',')}"
    else:
        return f'${intcomma(dollars).replace(".", ",")}'


class MoneyFmt():

    def __init__(self, dollars):
        self.dollars = dollars

    def update(self, new):
        self.dollars = new

    def __repr__(self):
        return f'{self.dollars}'

    def __str__(self):
        return dollarize(self.dollars)


cash = MoneyFmt(12345678.021)
print(cash)
cash.update(100000.4567)
print(cash)
cash.update(-0.3)
print(cash)
repr(cash)
