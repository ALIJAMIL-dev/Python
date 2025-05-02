numbers = [1, 4, 6, 32, 23, 12]
letters = ['a', 'c', 'v', 'z']
names = ['ahmet', 'ali', 'sena', 'yiğit']

result = min(numbers)  # Smallest number
result = max(numbers)  # Largest number
result = min(letters)  # Alphabetically first letter
result = max(letters)  # Alphabetically last letter
result = min(names)    # Alphabetically first name
result = max(names)    # Alphabetically last name

# Find the minimum length among names
result = min([len(name) for name in names])
# Find the maximum length among names
result = max([len(name) for name in names])

# Find the name with the maximum length
result = max(names, key=lambda name: len(name))
# Find the name with the minimum length
result = min(names, key=lambda name: len(name))

products = [
    {"title": "samsung s23", "price": 70000},
    {"title": "samsung s24", "price": 80000},
    {"title": "samsung s25", "price": 90000}
]

# Find the product with the minimum price
result = min(products, key=lambda product: product["price"])
# Find the title of the product with the maximum price
result = max(products, key=lambda product: product["price"])["title"]

max_price = 0

# Find the maximum price manually
for product in products:
    if product["price"] > max_price:
        max_price = product["price"]

print(max_price)
print(result)
