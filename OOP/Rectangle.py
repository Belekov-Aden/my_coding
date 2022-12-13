class rectangle():
    ''' Прямоугольник '''

    def __init__(self, sh, d):
        self.dlina = d
        self.shirina = sh

    def perimetr(self):
        return f'{2 * (self.dlina + self.shirina)}'

    def ploshad(self):
        return f'Площадь данного прямоугольника равняется {self.shirina * self.dlina}'

    def new_info(self, sh, d):
        self.dlina = d
        self.shirina = sh

    def pechat(self):
        return f'Прямоугольник ширина {self.shirina} длина {self.dlina}'


sd = rectangle(4, 6)
print(sd.perimetr())
print(sd.ploshad())
sd.new_info(5, 4)
print(sd.pechat())
print(sd.ploshad())
