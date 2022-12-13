

name = ['Aden','Aiz','Wolf', 'Terix', 'Name', 'Surname']


print(f'Ваш список \nname:{name}')
try:
    sdvig_items = int(input('Для сдвига элемента: '))

except ValueError:
    print('Введите только цифру!')



def request_num(num):
    def chech_l(chos):
        if num > 0:
            chos1 = chos[num:] + chos[:num]
            print(chos1)

        elif num < 0:
            chos1 = chos[num:] + chos[:num]
            print(chos1)

        elif num == 0:
            print(chos)

    chech_l(name)

request_num(sdvig_items)



