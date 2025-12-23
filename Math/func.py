def func(x):
    """Return x**2 if x is an even integer, otherwise return x+5.

    Raises TypeError if x is not an int.
    """
    if not isinstance(x, int):
        raise TypeError("Error: x must be an integer")

    if x % 2 == 0:
        return x ** 2
    else:
        return x + 5


if __name__ == "__main__":
    try:
        x = int(input("Enter an integer: "))
    except ValueError:
        print("Error: please enter a valid integer.")
    else:
        try:
            result = func(x)
        except TypeError as e:
            print(e)
        else:
            print("Result:", result)