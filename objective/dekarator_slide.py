#1 Problem function
def main(text_1):
    def put_in(text_2):
        print(text_1, text_2)
    put_in('\nЯ вложенный')

print(main('Я главный'))

#1 Problem function
def main(text_1):
    def put_in():
        print('Я главный')
        text_1()
    return put_in

@main
def putt():
    print('Я вложенный')

putt()

#2 Problem
spisok = {1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six'}
spisok_1 = {'Car':'тойота', 'City':'France'}

def change_dict_on_tuple(*args):
    spisok.update(spisok_1)
    print(tuple(spisok.keys()))
    print(tuple(spisok.values()))


change_dict_on_tuple(spisok, spisok_1)


#3 Problem
def prime(number):
    #n = number
    counter = 0
    for i in range(1, number + 1):
        if number % i == 0:
            counter += 1
    return 'Простое число' if counter == 2 else 'Составное число'

print(prime(5))

