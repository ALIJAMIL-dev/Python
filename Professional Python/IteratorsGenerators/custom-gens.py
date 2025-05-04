class MyNumbers:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        # This makes the class itself an iterator
        return self

    def __next__(self):
        # This defines what happens on each next() call
        if self.start <= self.stop:
            x = self.start
            self.start += 1
            return x
        else:
            raise StopIteration  # Stops the iteration when done

# Create an iterator from the MyNumbers class
iterator = iter(MyNumbers(20, 30))

# Loop manually through the iterator using next()
while True:
    try:
        print(next(iterator))
    except StopIteration:
        break

# You could also write:
# for i in MyNumbers(20, 30):
#     print(i)
