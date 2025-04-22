# Variable number of arguments
def add(*args: int) -> int:
    print(args)
    print(type(args))
    result = 0
    for i in args:
        result += i
    return result

# numbers = (10,20,30,40,50)
# def plus(numbers):
#     result1 = 0

#     for i in numbers:
#         result1 += i
    
#     return result1

# result2 = plus(numbers)
# print(result2)

result3 = add(10,20,30,40,50,60)
print(result3)
