#Calculator

sign = '1'

while True:
    if sign == '0':
        print('Операция завершена!')
        break
    num_1 = float(input('Число: '))
    num_2 = float(input('Число: '))


    sign = input('Операция: +/-* ** ')
    if sign != '+' and sign != '-' and sign != '*' and sign != '**' and sign != '/' and sign != '0':
        print('Ввод правильной операций')
        print(f'Ваша операция {sign} ')
        break
    else:
        pass

    if sign == '+':
        print('Равно', num_1 + num_2)

    elif sign == '-':
        print('Равно',num_1 - num_2)

    elif sign == '*':
        print('Равно',num_1 * num_2)

    elif sign == '/':
        try:
            if num_2 == 0:
                print('На ноль делить нельзя')
            print('Равно',num_1 / num_2)
        except ZeroDivisionError:
            pass

    elif sign == '**':
        print('Равно',num_1 ** num_2)