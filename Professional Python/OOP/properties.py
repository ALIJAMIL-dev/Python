class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price  # Protected attribute

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value > 0:
            self._price = value
        else:
            print("Price must be positive.")

# Usage example
p = Product("iPhone 16", 80000)

print(p.price)
p.price = -90000  # This will trigger the setter and print a warning
print(p.price)

# Old style (getter/setter methods):
# p.set_price(70000)
# print(p.get_price())  => now replaced with p.price and p.price = 70000
# print(p.name, p.price)
