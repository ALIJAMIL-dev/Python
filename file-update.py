# with open("file.txt", "a", encoding="utf-8") as file:
#     file.write("6-Bugatti")

# with open("file.txt", "r+", encoding="utf-8") as file:
#     anything = file.read()
#     anything = "1-Toyota\n" + anything
#     file.seek(0)
#     file.write(anything)

with open("file.txt", "r+", encoding="utf-8") as file:
    anything = file.readlines()
    anything.insert(2, "3-Honda\n")
    file.seek(0)
    # for i in anything:
    #     file.write(i)
    file.writelines(anything)
with open("file.txt", "r", encoding="utf-8") as file:
    print(file.read())