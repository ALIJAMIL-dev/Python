# 1- Create a list of numbers between 1 and 100 that are divisible by 12.

result = [i for i in range(1, 101) if i % 3 == 0 if i % 4 == 0]
# You can also write this as:
# result = [i for i in range(1, 101) if i % 12 == 0]

# 2- Create a list of digits from the given text.
# Example: text = "Hello 12345 World" => ['1','2','3','4','5']

text = "Hello 12345 World"
result = [i for i in text if i.isdigit()]

# 3- For each temperature in the list, write "Freezing Hazard" if it is below 4 degrees.
# temperatures = [20, 15, 0, -5, -2] => [20, 15, "Freezing Hazard", "Freezing Hazard", "Freezing Hazard"]

temperatures = [20, 15, 0, -5, -2]
result = [i if i >= 4 else "Freezing Hazard" for i in temperatures]

# 4- From the lists of students and grades, print a dictionary of students whose grade is more than 50.
# students = ["ali", "ahmet", "canan"]
# grades = [50, 60, 80]
# => {"ahmet": 60, "canan": 80}

students = ["ali", "ahmet", "canan"]
grades = [50, 60, 80]
# Create a list of (student, grade) tuples
pairs = [(students[i], grades[i]) for i in range(len(students))]
# Create a dictionary from the list where grade > 50
result_dict = {key: value for (key, value) in pairs if value > 50}

# 5- Convert a nested for loop into a list comprehension.
# The original loop:
# 0 - 0 - 0
# 0 - 0 - 1
# ...
# 2 - 2 - 2

result = []
for x in range(3):
    for y in range(3):
        for z in range(3):
            result.append((x, y, z))

# The same using list comprehension:
result = [(x, y, z) for x in range(3) for y in range(3) for z in range(3)]
print(result)