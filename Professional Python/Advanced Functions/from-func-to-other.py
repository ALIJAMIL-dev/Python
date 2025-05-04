# Exponential function that calculates the power of a base number
def usAlma(taban):  # The outer function receives the base number
    def inner(us):  # The inner function receives the exponent
        return taban ** us  # Returns the base raised to the power of the exponent
    return inner  # Returns the inner function, creating a closure

# Example usage:
# sonuc = usAlma(2)(3)  # Here 2 is the base and 3 is the exponent: 2^3 = 8
# fn = usAlma(2)  # Creates the base function with base 2
# sonuc = fn(4)  # Now we use fn with exponent 4: 2^4 = 16

# Function that returns the access right based on role
def yetki_sorgulama(sayfa):  # Takes a page as an argument
    def inner(role):  # The inner function takes the role of the user
        if role == "Admin":  # If the role is "Admin"
            return f"{role} rolü {sayfa} sayfasına ulaşabilir."  # Admin can access the page
        else:
            return f"{role} rolü {sayfa} sayfasına ulaşamaz."  # Non-admin cannot access the page
    return inner  # Returns the inner function

# Example usage:
# yetki = yetki_sorgulama("Ürün güncelleme")  # Creates the function to check access for the page "Product Update"
# sonuc = yetki("User")  # Checks if "User" can access the page. Result: "User rolü Ürün güncelleme sayfasına ulaşamaz."

# Function that selects a mathematical operation (addition or multiplication)
def islem(islem_adi):  # Takes the operation name (addition or multiplication)
    def toplam(*args):  # Defines a function for summing the arguments
        toplam = 0
        for i in args:
            toplam += i
        return toplam

    def carpim(*args):  # Defines a function for multiplying the arguments
        carpim = 1
        for i in args:
            carpim *= i
        return carpim
    
    if islem_adi == "toplama":  # If the operation is "toplama" (addition), return the addition function
        return toplam
    else:  # Otherwise, return the multiplication function
        return carpim

# Example usage:
toplama = islem("toplama")  # Select the addition operation
carpma = islem("carpma")  # Select the multiplication operation

sonuc = toplama(10, 20)  # Adds 10 and 20, result: 30
sonuc = carpma(10, 20)  # Multiplies 10 and 20, result: 200

print(sonuc)  # Output the result (200 from the multiplication)
