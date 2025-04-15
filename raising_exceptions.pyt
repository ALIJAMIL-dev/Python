# Raising Exceptions Demo:
# This a App or Demo of Raising Exceptions in Python. Let's Code:
def divide_numbers(num1, num2):
    """Divides two numbers and raises an exception if the second number is zero."""
    if num2 == 0:
        raise ValueError("Cannot divide by zero.")
    return num1 / num2
# More examples:
try:
    result = divide_numbers(10, 0)
except ValueError as e:
    print(f"Error: {e} and the result is 5")
