# def hello(name):
#     return f"hello, {name}"

# # print(hello("Chinar"))
# # print(hello)

# greet = hello

# print(hello)
# print(greet)

# del hello
# print(greet)

# # print(hello("Chinar"))
# print(greet("Chinar"))

def factorial(number):
    if not isinstance(number, int):
        raise TypeError("number must be an int")
    
    if not number >= 0:
        raise ValueError("number must be zero or positive")

    def inner_factorial(number):
        if number <= 1:
            return 1
        
        return number * inner_factorial(number - 1)
    
    return inner_factorial(number)

result = factorial(5)
try:
    result = factorial("4")
    print(result)
except Exception as ex:
    print(ex)
