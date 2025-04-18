# App: Error Management
liste = ["1","3","5","20b","abc","10a","60"]
# App 1: Find integer values in the list "liste"
for i in liste:
    try:
        print(int(i))
    except ValueError:
        print(f"'{i}' is not a number.")
    
# App 2: Make sure that every input you receive is a number unless the user enters the quit (q) value. Otherwise, write an error message.
while True:
    try:
        sayi = input("Enter a number (q to quit): ")
        if sayi == "q":
            break
        else:
            print(int(sayi))
    except ValueError:
        print(f"'{sayi}' is not a number.")

# App 3: Prepare the get(dict,key) function that takes dictionary and key information as parameters.

urun = {"urunAdi":"Samsung S20"}

# d["fiyat"] => KeyError
# get(urun,"fiyat") => None
# get(urun,"urunAdi") => "Samsung S20"

def get(d, key):
    try:
        return d[key]
    except KeyError:
        return None
