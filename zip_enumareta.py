# Description: This file demonstrates the use of the zip() and enumerate() functions in Python.
# Enumerate
# The enumerate() function adds a counter to an iterable and returns it as an enumerate object.
# The enumerate object is an iterator that returns tuples containing the index and the values of the iterable.
# The syntax of the enumerate() function is as follows:
# enumerate(iterable, start)
# The start parameter is optional and its default value is 0.
# The following example demonstrates the use of the enumerate() function:

values = ['Opel', 'Audi', 'BMW', 'Mercedes']

for i, value in enumerate(values, 1):
    print(f'{i}: {value}')

# Output:
# 1: opel
# 2: audi
# 3: bmw
# 4: mercedes

# Zip
# The zip() function takes two or more iterables and returns a zip object that is an iterator of tuples.
# Each tuple contains elements from each iterable. The zip object is an iterator, so it can be used only once.
# To convert the zip object into a list, use the list() function.   
# The zip() function stops when the shortest input iterable is exhausted.

# The syntax of the zip() function is as follows:
# zip(iterable1, iterable2, ...)
# The following example demonstrates the use of the zip() function:

names = ['Alice', 'Bob', 'Charlie']
ages = [24, 25, 26]
countries = ['Turkey', 'Syria', 'Kingdom of Saudi Arabia']

for name, age, country in zip(names, ages, countries):
    print(f'{name} is {age} years old and lives in {country}.')

