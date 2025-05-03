class Human:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        print("Human class has been instantiated.")

    def introduce(self):
        print(self.first_name, self.last_name, self.age)

class Pupil(Human):
    def __init__(self, first_name, last_name, age, student_id):
        super().__init__(first_name, last_name, age)
        self.student_id = student_id
        print("Pupil class has been instantiated.")

    def study(self):
        print(f"{self.first_name} is studying.")

    def introduce(self):
        print(self.first_name, self.last_name, self.age, self.student_id)

class Instructor(Human):
    def __init__(self, first_name, last_name, age, subject):
        super().__init__(first_name, last_name, age)
        self.subject = subject
        print("Instructor class has been instantiated.")

    def teach(self):
        print(f"{self.first_name} is teaching {self.subject}.")

# Example usage
person1 = Human("John", "Smith", 40)
person1.introduce()

student1 = Pupil("Emily", "Johnson", 7, 105)
student1.introduce()
# student1.study()
# print(student1.student_id)

teacher1 = Instructor("Michael", "Brown", 35, "Physics")
teacher1.introduce()
# print(teacher1.subject)
# teacher1.teach()
