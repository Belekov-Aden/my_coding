# # 3
# Students room:
# Реализуйте студенческую комнату с помощью ООП:

# Copy:
# Steve = Student("Steven Schultz", 23, "English")
# Johnny = Student("Jonathan Rosenberg", 24, "Biology")
# Penny = Student("Penelope Meramveliotakis", 21, "Physics")
# print(Steve)
# <name: Steven Schultz, age: 23, major: English>
# print(Johnny)
# <name: Jonathan Rosenberg, age: 24, major: Biology>

class Student():

    def __init__(self, name: str, age: int, lessons: str):
        self.name = name
        self.age = age
        self.lesson = lessons

    def __repr__(self):
        return f'<name : {self.name}, age: {self.age}, major; {self.lesson}>'


Steve = Student("Steven Schultz", 23, "English")
Johnny = Student("Jonathan Rosenberg", 24, "Biology")
Penny = Student("Penelope Meramveliotakis", 21, "Physics")
print(Steve)
print(Johnny)
