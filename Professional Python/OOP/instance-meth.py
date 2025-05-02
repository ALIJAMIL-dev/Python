# Class
class CartItem:
    # Constructor
    def __init__(self, name, price, pcs):
        # The Instance attributes
        self.name = name 
        self.price = price
        self.pcs = pcs
    # Instance Methods:
    def calculateTotal(self):
        return self.price * self.pcs
    
    def applyDiscount(self, rate):
        self.price = self.price * rate



# Instance


item1 = CartItem("PhoneI", 1200, 2)
item2 = CartItem("PC", 1999, 1)

item1.applyDiscount(0.9)
item2.applyDiscount(0.7)

print(item1.calculateTotal())
print(item2.calculateTotal())

