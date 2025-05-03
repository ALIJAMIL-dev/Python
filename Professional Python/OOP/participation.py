class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        print("Sucssefly")

    def intro(self):
        print(self.name, self.surname, self.age)

class Student(Person):
    pass

class Teacher(Person):
    pass

p1 = Person("Ali", "Jamil", 12)
p1.intro()

t1 = Teacher("Cristiano", "Ronaldo", 7)
t1.intro()