
p_bank = int(input('Скольно хотите накопить?: '))
money = 0
while True:
    money_get = int(input('Взнос: '))
    money += money_get

    if money >= p_bank:
        print(f'Вы успешно наполнили {money}')
        break
