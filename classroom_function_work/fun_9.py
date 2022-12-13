a = int(input("Сумма вклада? "))
years = int(input("На сколько лет хотите сделать вклад? "))

stavka = 10

def bank  (summa, year_sum):
    for i in range(year_sum):
        summa = int(summa + stavka * summa / 100)

        print(f'Вы получаете год {i} в сумме {summa}')

    print(f'На вашем счету {summa} будет')

bank(a, years)
