# mumbers = [1,2,3,4,5,6,7,8,9,10]
# square = []

# for i in mumbers:
#     square.append(i**2)

# print(square)

nums = [1,2,3,4,5,6,7,8,9,10]

# def square(num):
#     return num**2

result = map(lambda num: num**2, nums)
print(list(result))
print(result)