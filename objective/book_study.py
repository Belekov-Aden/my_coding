#4.1 Напишите код для функции sum (см. выше).
#Ответ:
def sum(list):
    if list == [] :
        return 0
    return list[0] + sum(list[1:])

print(sum([1, 2, 3, 4,463,754,436,36,3,46,3,34,6,34,634,6,634,3,6,345,34,6,36,346,43,6,34,6,3]))

#4.2 Напишите рекурсивную функцию для подсчета элементов в списке.
#Ответ:
def count(list):
    if list == []:
        return 0
    return 1 + count(list[1:])

print(count([1, 2, 3, 4,463,754,436,36,3,46,3,34,6,34,634,6,634,3,6,345,34,6,36,346,43,6,34,6,3]))





#4.3 Найдите наибольшее число в списке.
#Ответ:
def max(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max(list[1:])
    return list[0] if list[0] > sub_max else sub_max

print(max([1, 2, 3, 4,463,754,436,36,3,46,3,34,6,34,634,6,100_000]))
