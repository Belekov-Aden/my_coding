class Abonent():
    surname = None
    name = None
    full_name = None
    age = None
    address = None
    credit = None
    credit_card = None

    def __init__(self):
        ...

    def person(self, surname, name, full_name, age):
        self.full_name = full_name
        self.name = name
        self.surname = surname
        self.age = age

    def card(self, credit_card, card, address):
        self.credit = card
        self.credit_card = credit_card
        self.address = address

    def get_info(self):
        return f'{self.surname} {self.name} {self.full_name} {self.age}\n{self.address} {self.credit_card} {self.credit}'


a = Abonent()
a.person('Belekov', 'Aden', 'Azamatovich', 17)
a.card(43546467435435, 637, 'Скурудина 6А')
print(a.get_info())
