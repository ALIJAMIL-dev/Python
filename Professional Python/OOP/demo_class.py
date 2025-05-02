class CartItem:
    discount_rate = 0.8
    item_count = 0

    @classmethod
    def display_item_count(cls):
        return f"{cls.item_count} items were created."
    
    @classmethod
    def create_item(cls, data_str):
        name, price, quantity = data_str.split(",")
        return cls(name, float(price), int(quantity))

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        CartItem.item_count += 1
    
    def calculate_total(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * CartItem.discount_rate

class Coupon:
    def __init__(self, code, discount):
        self.code = code
        self.discount = discount

# Create coupons
c1 = Coupon("code1", 0.8)
c2 = Coupon("code2", 0.7)
c3 = Coupon("code3", 0.9)

# Create items
item1 = CartItem("Phone", 50000, 2)
item2 = CartItem("Computer", 70000, 1)
item3 = CartItem("Book", 500, 2)

class ShoppingCart:
    coupon_list = [c1, c2, c3]

    def __init__(self, items):
        self.items = items

    def add_item(self, item):
        self.items.append(item)

    def display_items(self):
        for i in self.items:
            print(f"{i.name} {i.price}")

    def calculate_totals(self):
        return sum([item.calculate_total() for item in self.items])
    
    def remove_item(self, cart_item):
        self.items = [item for item in self.items if item != cart_item]

    def clear(self):
        self.items = []

    @classmethod
    def get_coupons(cls):
        return [coupon.code for coupon in cls.coupon_list]
    
    @classmethod
    def get_coupon(cls, code):
        return next(filter(lambda c: c.code == code, ShoppingCart.coupon_list))
    
    def apply_coupon(self, code):
        if code not in ShoppingCart.get_coupons():
            raise ValueError(f"Invalid coupon code: {code}")
        
        coupon = ShoppingCart.get_coupon(code)

        for index in range(0, len(self.items)):
            self.items[index].price = self.items[index].price * coupon.discount

# Create a shopping cart with two items
sc = ShoppingCart([item1, item2])
sc.add_item(item3)
sc.display_items()

# Print total before coupon
print(sc.calculate_totals())

# Apply coupon
sc.apply_coupon("code2")

# Print total after coupon
print(sc.calculate_totals())
