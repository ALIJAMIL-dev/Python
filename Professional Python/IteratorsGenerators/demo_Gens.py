# Function that generates the square of every number from 1 to ∞

def generate_squares():
    number = 0
    while True:
        yield number ** 2
        number += 1

# generator = generate_squares()

# print(next(generator))
# print(next(generator))
# print(next(generator))

# for i in generator:
#     print(i)

# Fibonacci sequence using a regular function
def fibonacci_list(limit):
    numbers = []
    a, b = 0, 1

    while len(numbers) <= limit:
        numbers.append(b)
        a, b = b, a + b

    return numbers

# print(fibonacci_list(9000))

# Fibonacci sequence using a generator
def fibonacci_generator(limit):
    a, b = 0, 1
    count = 0
    while count <= limit:
        a, b = b, a + b
        yield b
        count += 1

# for num in fibonacci_generator(9000):
#     print(num)

# Memory usage comparison
import sys

list_example = [i for i in range(10000)]
print(sys.getsizeof(list_example))  # List size in memory

generator_example = (i for i in range(10000))
print(sys.getsizeof(generator_example))  # Generator size in memory

# Performance comparison between list and generator
import time

list_start_time = time.time()
sum([i for i in range(9000000)])
list_duration = time.time() - list_start_time

gen_start_time = time.time()
sum((i for i in range(9000000)))
gen_duration = time.time() - gen_start_time

print(list_duration)
print(gen_duration)
