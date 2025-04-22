from module1 import *
from module2 import *

# Module2 is imported here to use the Calculator class
Calculator = Calculator()
Calculator.greeting("Ali")
Calculator.add(5, 3)
Calculator.subtract(10, 4)
Calculator.multiply(6, 7)
Calculator.divide(20, 5)

# Module1 is imported here to use the variables and functions defined in it
print(num1)
print(nums1)

print(products)
print(products["ProductName"])
print(products["Price"])
print(products["Colors"])

print(add(5, 3))
