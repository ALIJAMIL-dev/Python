# for item in liste:
#     if (condition):
#         expression

# [ expression for item in liste if condition ]

sayilar = [3,5,7,6,56,34]
result = []

for sayi in sayilar:
    if(sayi % 2 == 0):
        result.append(sayi)

result = [sayi for sayi in sayilar if sayi % 2 == 0]
result = [sayi if sayi % 2 == 0 else "odd number" for sayi in sayilar]

price = [3000,0,1000,4000,0,5000]
taxes = []

for fiyat in price:
    if(fiyat > 0):
        taxes.append(fiyat * 1.20)

taxes = [fiyat * 1.20 for fiyat in price if fiyat > 0]
taxes = [fiyat if fiyat > 0 else "Taxes not calculated." for fiyat in price]

print(taxes)
