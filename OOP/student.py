class Student:

    def __init__(self, name, lastname, departamnet, year):
        self.name = name
        self.lastname = lastname
        self.departament = departamnet
        self.year = year

    def get_student_info(self):
        return f'{self.name.title()} {self.lastname.title()} поступил в {self.year} г. на факультет {self.departament}'


p = Student('Aden', 'belekov', 'МПТ', 2022)
print(p.get_student_info())

d = Student('Semen', 'Shant', 'isp-05', 2022)
print(d.get_student_info())
