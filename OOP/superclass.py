class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        return f'Person name: {self.name.title()}\nPerson age:{self.age}\n'


class Student(Person):
    def __init__(self, name, age):
        super(Student, self).__init__(name, age)

    def displayStudent(self):
        return f'Student name:{self.name}\nStudent age:{self.age}\n'


Aden = Person('Aden', 17)
print(Aden.display())

werba = Student('Abadc', 21)
print(werba.displayStudent())
