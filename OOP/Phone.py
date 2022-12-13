class Phone():
    ''''Static attribute'''
    number = 1
    model = 'Apple'
    weight = 45

    ''''Конструктор __init__'''

    def __init__(self, number, model, weight):
        self.number = number
        self.model = model
        self.weight = weight

    def sendMessage(self, phone_number):
        return f'{phone_number} отправил сообщение!'


apple = Phone(7, 'Apple', 45)
samsung = Phone(9, 'Samsung', 40)
mi = Phone(2, 'Redmi S2', 35)

print(Phone.__dict__)

print(apple.sendMessage('+996706100450'))
