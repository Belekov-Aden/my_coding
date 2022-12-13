from random import randrange, randint


class Person:
    def __init__(self, c):
        self.id = randint(0, 100)


class Heroes(Person):
    level = 1

    def level_up(self):
        self.level += 1
        print('герой с id ' + str(self.id) + ' достиг второго уровня')


class Soldiers(Person):  #
    def __init__(self, r=[], b=[]):
        Person.__init__(self, c=1)
        random_number = randrange(-1, 2, 2)
        red_army = r
        blue_army = b

        if random_number > 0:
            self.command = 'blue'
            blue_army.append(self)
        elif random_number < 0:
            self.command = 'red'
            red_army.append(self)

        print('blue army soldiers: {0} units, red army soldiers: {1} units'.format(len(blue_army), len(red_army)))

        if len(blue_army) > len(red_army):
            print(1)
        elif len(blue_army) < len(red_army):
            print(2)

    def __str__(self):
        return 'test'


hero_blue = Heroes('Aden')
hero_red = Heroes('Dastan')

soldier1 = Soldiers()
soldier2 = Soldiers()
soldier3 = Soldiers()
soldier4 = Soldiers()
soldier5 = Soldiers()
soldier6 = Soldiers()
soldier7 = Soldiers()
soldier8 = Soldiers()
soldier9 = Soldiers()
