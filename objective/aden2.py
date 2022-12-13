class Cat:
    def __init__(self, name):
        self.name = name
        self._power = 100

    def is_active(self):
        if self._power >= 0:
            return True
        return False

    def play(self, active):
        self._power -= active

    def want_play(self):
        print('Поиграй со мной плиз', self._power)

    def feed(self, active):
        self._power += active

    def want_eat(self):
        print('Покорми меня', self._power)

    def want_sleep(self):
        print(f'{self.name} устал иду спать! ')


class Battle_Cat(Cat):
    def atake_cat(self, active):
        self._power -= active
        print(f'Я укусил твое одну жизнь {self._power}')


if __name__ == '__main__':
    def main():
        cat = Battle_Cat('Карамелька')
        while cat.is_active():
            cat.want_eat()
            cat.feed(int(input()))
            cat.want_play()
            cat.play(int(input()))
            cat.atake_cat(1)

        cat.want_sleep()

main()
