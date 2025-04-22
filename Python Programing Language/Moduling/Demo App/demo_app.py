# demo_app.py

from methods import addProduct, updateProduct, getProducts

# Add a new product
addProduct("iPhone 15", 60000)

# Update the product
updateProduct(0, "iPhone 15 Pro", 80000)

# List all products
print(getProducts())
