class Guns:
    def __init__(self):
        self.shot = 60

    def shot_ret(self):
        self.shot += 25
        print(f'Перезарядка  + 25')


class Soldier(Guns):
    def shot_ak(self):
        self.shot -= 35
        print(f'тиги-тигитиш -35')


class Act_of_Shooting(Soldier):
    def activ(self):
        self.shot_ak()
        self.shot_ret()
        self.shot_ak()
        print(f'В обойме {self.shot}')


n = Act_of_Shooting()

n.activ()
