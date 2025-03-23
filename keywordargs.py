# Keyword Arguments
def print_something(firstname: str, lastname: str, age: int) -> str:
    return firstname + ' ' + lastname + ' ' + str(age)

# My Last Name is JAMIL
# My First Name is Ali
# I am 12 years old

result = print_something('Ali', 'JAMIL', 12)
print(result)