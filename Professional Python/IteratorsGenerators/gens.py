def counter(max_value):
    number = 1
    while number <= max_value:
        yield number
        number += 1

generator = counter(20)

# print(generator)
# print(dir(generator))

# print(next(generator))
# print(next(generator))
# print(next(generator))

# for i in generator:
#     print(i)

# result = list(generator)

generator_expression = (i for i in range(1, 20))

print(next(generator_expression))
print(next(generator_expression))
