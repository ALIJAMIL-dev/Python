# Error Types
# Number of Error Types in Python are as follows:
# ValueError example:
try:
    int("abc")
except ValueError as e:
    print(f"ValueError: {e}")

#ZeroDivisionError example:
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"ZeroDivisionError: {e}")

#TypeError example:
try:
    result = "string" + 10
except TypeError as e:  
    print(f"TypeError: {e}")

#NameError example:
try:
    print(undefined_variable) # type: ignore
except NameError as e:
    print(f"NameError: {e}")

#IndexError example:
try:
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError as e:
    print(f"IndexError: {e}")

#KeyError example:
try:
    my_dict = {"a": 1, "b": 2}
    print(my_dict["c"])
except KeyError as e:
    print(f"KeyError: {e}")

#AttributeError example:
try:
    my_string = "hello"
    print(my_string.non_existent_method())
except AttributeError as e:
    print(f"AttributeError: {e}")

#SyntaxError example:
try:
    eval("x === 10")
except SyntaxError as e:
    print(f"SyntaxError: {e}")
