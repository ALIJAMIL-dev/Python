# Decorator that runs a function twice and returns the second result
def double(fn):
    def inner(*args, **kwargs):
        fn(*args, **kwargs)  # First call (for printing/output)
        return fn(*args, **kwargs)  # Second call (return value)
    return inner

@double
def hello():
    print("hello")

@double
def greet(name):
    print("greetings", name)

@double
def good_day():
    return "good day"

# Call the decorated functions
hello()                # Prints "hello" twice
greet("Ali")           # Prints "greetings Ali" twice
print(good_day())      # Prints "good day" once, returns "good day"
