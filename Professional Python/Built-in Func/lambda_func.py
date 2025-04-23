# (lambda argument: expression)(argument)

def getSquare(a):
    return a ** 2

result = (lambda a: a ** 2 )

result(6)

print(result)

# Lambda simple using examples:

valueMeansYou = lambda fucnk: print(fucnk + "func")

print(valueMeansYou("hello"))