numbers = [1, 3, 5, 4, 32, 56]

result = sum(numbers)          # Sum of all numbers
result = sum(numbers, 15)      # Sum of all numbers + 15

products = [
    {"title": "iphone 15", "price": 60000},
    {"title": "iphone 16", "price": 70000},
    {"title": "iphone 17", "price": 80000},
    {"title": "iphone 17", "price": 0},
]

# Calculate the total price of all products
total_price = sum([product["price"] for product in products])

# Count the number of products with a price greater than 0
product_count = len([product for product in products if product["price"] > 0])

# Calculate the average price
result = total_price / product_count

# Rounding examples
result = round(5.3)            # Rounds to 5
result = round(5.6)            # Rounds to 6
result = round(5.5)            # Rounds to 6 (Python rounds .5 to the nearest even number)
result = round(1.325233, 2)    # Rounds to 1.33
result = round(1.325253, 4)    # Rounds to 1.3253

print(result)
