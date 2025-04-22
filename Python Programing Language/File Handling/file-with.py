# with open("file-read.txt", "r") as file:
#     print(file.read())
#     print(file.tell())
try:
    with open("file-read.txt", "r") as file:
        for i in file:
            print(i, end="")
except FileNotFoundError:
    print("File not found")