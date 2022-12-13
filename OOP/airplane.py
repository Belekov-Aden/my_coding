class Airplane():

    def __init__(self, make, model, year, max_speed, odomoter):
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.odometer = odomoter
        self.is_flying = False

    def take_off(self):
        self.is_flying = True
        return f'Взлет {self.__dict__}'

    def fly(self, r):
        self.odometer += r
        return f'Летать {self.__dict__}'

    def land(self):
        self.is_flying = False
        return f'Приземление {self.__dict__}'


a = Airplane('Japan', 199, 2000, 300, 30_000)
print(a.take_off())
print(a.fly(20))
print(a.land())
