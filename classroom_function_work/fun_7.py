
from termcolor import colored

numbers = [
    1, 2, 3, -1, -2, -3, 64, 23, -68, 0.76, -3, -133, -666, -1, -0.53245,
]


def choose_numbers_plus_and_minus(num):
    plus = []
    minus = []
    for i in num:
        if i > 0:
            plus.append(i)
        else:
            minus.append(i)

    print(colored(f'Положительные числа {plus}', 'green'))
    print(colored(f'Отрицательные числа {minus}', 'blue'))


choose_numbers_plus_and_minus(numbers)