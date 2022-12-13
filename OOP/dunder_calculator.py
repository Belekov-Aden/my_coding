# Задание такое
# СОЗДАТЬ СОБСТВЕННЫЙ КАЛЬКУЛЯТОР КЛАСС КОТОРЫЙ ПРИНИМАЕТ ДВА АРГУМЕНТА ЧИСЛЕННЫХ
# И ОПЕРАТОР, Т.Е. ТРИ АРГУМЕНТА ДВА ИНТ ОДИН - ( + - / % //)

class Calculator:

    def __init__(self, num1: int, num2: int):
        self.num1 = num1
        self.num2 = num2

    def __add__(self):
        return self.num1 + self.num2

    def __sub__(self):
        return self.num1 - self.num2

    def __mul__(self):
        return self.num1 * self.num2

    def __truediv__(self):
        return self.num1 / self.num2

    def __mod__(self):
        return self.num1 % self.num2

    def __floordiv__(self):
        return self.num1 // self.num2


x = Calculator(4, 5).__add__()
print(x)
