from random import randint

random_num = randint(0, 100)
i = 0
while True:
    numbers = int(input('Число: '))
    if numbers == random_num:
        print('You win!')
        break
    if numbers < random_num:
        print('загаданное число больше')
    else:
        print('загаданное число меньше')
    i += 1
    if i == 10:
        print(f'Вы проиграли. Загаданное число {random_num}')
        break
