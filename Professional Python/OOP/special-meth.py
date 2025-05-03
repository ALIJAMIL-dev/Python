liste = [1, 2, 3]

print(len(liste))  # Output: 3

# number = 10
# print(len(number))  # Would raise TypeError

s = "Hello BTK Academy"

print(len(s))  # Output: number of characters in the string

class Movie:
    def __init__(self, title, director, year, duration):
        self.title = title
        self.director = director
        self.year = year
        self.duration = duration

    def __repr__(self):
        return f"{self.title}, directed by {self.director}, released in {self.year}."
    
    def __len__(self):
        return self.duration    
    
    def __del__(self):
        print("Movie deleted.")

m = Movie("Inception", "Christopher Nolan", "2010", 120)

print(m.__repr__())  # Calls custom string representation
print(len(m))        # Calls custom length (duration)

del m  # Triggers __del__
