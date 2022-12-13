John = [['algebra', 100], ['biologia', 100], ['fizika', 150]]
Aden = [['algebra', 100], ['biologia', 66], ['fizika', 21]]
A = [['algebra', 32], ['biologia', 93], ['fizika', 24]]

# Сумма среднего значение студентов
s_student = {}


# Получение имен с переменных
def getName(arg1):
    gl = globals().copy()
    for i in gl:
        if gl[i] is arg1:
            return i


def li_in_di(arg):
    csd = []
    # Цикл преоброзование list в dict
    for a in arg:
        lesson_student = a[::2]
        point_student = a[1::2]

        d = dict(zip(lesson_student, point_student))
        csd.append(d)

        for state in csd:
            d.update(state)

    # Счетчик среднего значение
    summ = 0
    for point in d.values():
        summ = (summ + point) / len(d.values())

    s_student[getName(arg)] = summ.__round__(2)

    # вывод данных
    print(f'{getName(arg)}:{d}')
    print(f'{list(d.values())}')
    print(f'Средний балл {summ.__round__(2)}\n')


# Вызвать людей,что-бы увидеть результат
li_in_di(John)
li_in_di(Aden)
li_in_di(A)
print(s_student)
print(f'\nСамое максимальное значение {max(s_student.keys())}: {max(s_student.values())}')
