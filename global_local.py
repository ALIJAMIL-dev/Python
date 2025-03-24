# local scope
# global scope

# x = "global"

# def foo():
#     x = "local"
#     print("x inside:", x)

# foo()
# print("x outside:", x)

name = "John"

def change_name(newname):
    global name
    name = newname
    print(name)

change_name("Bob")
print(name)