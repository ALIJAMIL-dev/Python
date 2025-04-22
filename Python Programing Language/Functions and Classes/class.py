class Product:
    # Attributes & Properties
    def __init__(self, name, price, isActive=True):
        self.name = name
        self.price = price
        self.isActive = isActive
    
    # Instance Method
    def get_product(self):
        return f"Product: {self.name}, Price: {self.kdv_price}, Active: {self.isActive}"
    
    def kdv_price(self):
        return self.price * 1.18

# Instance & Object

product1 = Product("Lenovo V15 G4 IRU", 360, True)
product2 = Product("Dell Inspiron 3515", 450, True)
product3 = Product("Acer Aspire 5", 500, True)
product4 = Product("Asus Vivobook 15", 550, True)
product5 = Product("Samsung S25 Ultra+", 700, True)

products = [product1, product2, product3, product4, product5]

#for i in products:
#    if i.isActive:
#        print("Product: {self.name}, Price: {self.price}, Active: {self.isActive}")

for i in products:
    if i.isActive:
        print(i.get_product())