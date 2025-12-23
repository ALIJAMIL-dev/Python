import datetime
class funWay:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        todaysYear = datetime.datetime.now().year 
        birthYear = todaysYear - self.age
        return f"Hello, my name is {self.name} and I was born in {birthYear}."

soufi = funWay("Ahmad", 12)
flower = funWay("Word", 12)

print(soufi.greet())
print(flower.greet())

def add(a, b):
    return a + b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
result = add(a, b)
print(f"The sum of {a} and {b} is {result}.")
