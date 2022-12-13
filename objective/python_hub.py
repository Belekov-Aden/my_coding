# Задание 4:
        # Напишите программу, которая запрашивает у пользователя шесть вещественных чисел.
        # На экран выводит минимальное и максимальное из них, округленные до двух знаков после запятой.
        # Выполните задание без использования встроенных функций min() и max().
####################################################################
#1 Первый метод при помощи reduce (Aden)
#from functools import reduce

float_num = [float(input('введите вещественные числа: '))for num in range(6)]
#А это 2 метод через списки
float_num = [round(v,2) for v in float_num]
float_num = list(float_num)
print(float_num)
float_num.sort()

print(f'Наибольшее число: {float_num[-1]}\n'
      f'А самое наименьшее число: {float_num[0]}')

#print(reduce(max, float_num))
#print(reduce(min, float_num))


# Задание 5: (Aden)
        # Напишите программу которая принимает число любой длины и вытаскивает из него самое большое и самое маленькое число.
####################################################################
num_inp = input('Введите число: ')
num_new = list(num_inp)
print(f'Самое большое это - {max(num_new)}\n\
И самое наименьшее - {min(num_new)}')


# Задание 6: (Aden)
#     Функция
#     Напишите функцию, которая берет текст, и возвращает строковое значение, состоящее из заглавных букв.
#     Используйте текст, данный выше (The Zen of Python).
#     Подсказка: используйте метод строчных значений, который проверяет, “заглавность” буквы.
##################################################################

text = """
The Zen of Python, by Tim PetersBeautiful is better than ugly.Explicit is better than implicit.
Simple is better than complex.Complex is better than complicated.
Flat is better than nested.Sparse is better than dense.
Readability counts.Special cases aren't special enough to break the rules.Although practicality beats purity.
Errors should never pass silently.Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one--and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea --let's do more of those!
"""

def check_text(str):
    x = text.replace('PetersBeautiful', 'Peters Beautiful')
    text_list = list(x.replace('.', '\n').split())
    print(text_list)
    for i in text_list:
        if i == i.title():
            print(i)



check_text(str)




# Задание 7:
#     Чтение из файла.
#     Создайте файл с текстом The Zen of Python.
#     Напишите функцию, которая считайте его и возвратит список из слов, которые начинаются на букву “c” или “C”.
#     Подсказка: используйте метод строчных значений, который проверяет, начинается ли слово на переданную букву.
####################################################################

f = open('The Zen of Python.txt', 'w')
f.write('''The Zen of Python, by Tim PetersBeautiful is better than ugly.Explicit is better than implicit.
Simple is better than complex.Complex is better than complicated.
Flat is better than nested.Sparse is better than dense.
Readability counts.Special cases aren't special enough to break the rules.Although practicality beats purity.
Errors should never pass silently.Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one--and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea --let's do more of those!''')
f.close()


f = open("The Zen of Python.txt", "r")
text_list = list(f.read().replace('.', '\n').split())
print(text_list)

word_s = []

for i in text_list:
    if i.startswith('s') or i.startswith('S'):
        word_s.append(i)

print(f'This list have only "s" and "S" {word_s}')
f.close()

# Задание 10:
#     Фильтрация с помощью filter(). Необходимо написать функцию, и передать ее filter(),
#     чтобы получить список только тех слов из текста text (см. выше “The Zen of Python”), что содержат букву ‘p’.
#     Подсказка: необходимо заменить \n на пробел.

#     То есть, это нужно проделать еще до фильтрации.
#     Функция, которая будет передана в filter() должна возвращать True, если в слове есть буква ‘p’.
#####################################################################

f = open('The Zen of Python.txt', 'r+')

text_read = f.read().replace('\n', ' ').split()
text_read = list(text_read)


def filter_text_r(text_read):
    if 'p' in text_read or 'P' in text_read:
        return True
    else:
        False

our_filter = filter(filter_text_r, text_read)

print(list(our_filter))


#only_r = []
#for i in text_read:
    #if 'r' in i or 'R' in i:
        #only_r.append(i)
#print(only_r)

f.close()


# Задание 12:
#     Аналог шифра цезаря ". Программа должна запрашивать элементы
#     списка через пробел. После чего пользователь должен ввести значение
#     для сдвига элементов списка. Значение может быть как положительным,
#     так и отрицательным. Если значение положительное, элементы списка
#     должны сдвигаться вправо, если отрицательное - влево. Результат
#     необходимо вывести на экран:

#     Пример:
#     [1, 2, 3, 4, 5], сдвиг 2
#     [3, 4, 5, 1, 2]
#####################################################################

numbers = [1, 2, 3, 4, 5]
print(numbers)

def request_num(num):
    if num > 0:
        numbers_1 = numbers[num:] + numbers[:num]
        print(numbers_1)
    elif num < 0:
        numbers_1 = numbers[num:] + numbers[:num]
        print(numbers_1)


request_num(3)