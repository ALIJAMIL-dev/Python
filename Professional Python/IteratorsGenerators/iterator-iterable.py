# Iterable
# Iterator

numbers = [1, 2, 3, 4, 5, 6]

iterator = iter(numbers)

while True:
    try:
        number = next(iterator)
        print(number)
    except StopIteration:
        break

# Example of an error (uncomment to see)
# print(next(iterator))  # Raises StopIteration because it's exhausted

# s = "BTK ACADEMY"
# a = 10

# for i in a:  # Error: int object is not iterable
#     print(i)
