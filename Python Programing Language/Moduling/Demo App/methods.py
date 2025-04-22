# methods.py

from db import products

def addProduct(name, price):
    products.append({"name": name, "price": price})

def updateProduct(index, new_name, new_price):
    if 0 <= index < len(products):
        products[index]["name"] = new_name
        products[index]["price"] = new_price
    else:
        print("Invalid index.")

def getProducts():
    return products
