# Банкомат
# Напишите код банкомата, который принимает цифру, выдает деньги с номиналом
# 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 3, 1.

from termcolor import colored, cprint
print('''

------------------------------------------------
\u27805000        \u2784200         \u2788 10  

\u27812000        \u2785100         \u2469 5

\u27821000         \u278650          \u246A 3

\u2783500          \u278720          \u246B 1
-------------------------------------------------

''')

bank_int_input_num = int(input(colored('Введите цифру для вывода средств: ', 'red')))

suum = {
    1: 5000,
    2: 2000,
    3: 1000,
    4:500,
    5: 200,
    6:100,
    7:50,
    8:20,
    9:10,
    10:5,
    11:3,
    12:1
}


def Conclusion_som(money):
    for i in suum.keys():
        if money == i:
            summa = int(input('Введите сколько купюр хотите вывести?: '))

            print(colored(f'Ваша сумма:{suum.get(money) * summa} сомов', 'green'))

Conclusion_som(bank_int_input_num)