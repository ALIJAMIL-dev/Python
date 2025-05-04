# This is a decorator function that wraps any greeting function
def greeting_decorator(fn):
    def inner(name):
        print("Welcome!")
        fn(name)
        print("See you soon!")
    return inner

# Using the decorator on two different functions
@greeting_decorator
def good_morning(name):
    print(f"Good morning, my name is {name}")

@greeting_decorator
def good_day(name):
    print(f"Good day, my name is {name}")

# Call the decorated functions
good_morning("Ali")
good_day("Sadık")
