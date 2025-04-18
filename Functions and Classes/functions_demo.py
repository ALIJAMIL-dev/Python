# Printer of a word a certain number of times
def howMany(theWord, HowTimes):
    for i in range(HowTimes):
        print(theWord)
print(howMany("hello", 3))

# Calculator of the area and perimeter of a rectangle
def calculateRectangle(width, height):
    def areaRectangle(width, height):
        return width * height
    def perimeterRectangle(width, height):
        return 2 * (width + height)
    return f"Area: {areaRectangle(width, height)}, Perimeter: {perimeterRectangle(width, height)}"
print(calculateRectangle(3, 4))

# Heads or tails game
def headsOrTails():
    import random
    if random.randint(0, 1) == 0:
        return "heads"
    else:
        return "tails"
print(headsOrTails())

# Prime number finder between inputted numbers
def primeNumbers(firstNumber, secondNumber):
    for num in range(firstNumber, secondNumber + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)
print(primeNumbers(10, 20))

# A function that returns a list of divisors of a given number.
def divisorsOfNumber(number):
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    return divisors
print(divisorsOfNumber(10))