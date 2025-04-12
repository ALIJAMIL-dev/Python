x = 10
y = int(input("Enter a number: "))

if y == 0:
    raise ValueError("y cannot be zero")  # Raise a ValueError if y is zero
else:
    result = x / y
    print(f"Result: {result}")