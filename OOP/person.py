class Person:
    fullname = 'Aden'
    age = 17
    address = 'Magadan'

    def talk(self):
        print(f'С вами говорит {self.fullname} {self.age} {self.address}')

    def move(self, place):
        self.address = place
        print(f'Ваш адресc обновился: {self.address}')

    def __init__(self, fullname, address, age=18):
        self.fullname = fullname
        self.address = address
        self.age = age

    def __str__(self):
        return f'Name {self.fullname}\nAge {self.age}\nPlace {self.address}'


aden = Person('Belekov Aden', 'Magadan')
aden.talk()

aden.move('Moscow')
aden.talk()

print(aden)
