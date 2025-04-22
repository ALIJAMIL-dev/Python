sayilar = []

for i in range(5):
    sayilar.append(i * 2)

print(sayilar)

sayilar2 = [i * 2 for i in range(5)]

print(sayilar2)

Company = "Btk Akademi"

for i in Company:
    print(i.upper())

result = [i.upper() for i in Company]
# i = 0
# cnt = []
# while i < 101:
#     print(i)
#     cnt.append(i)
#     i += 1
# cnt = [i for i in range(101)]
# print(cnt)
print(result)

