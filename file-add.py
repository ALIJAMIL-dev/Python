# with open('file-write.txt', 'a', encoding="utf-8") as f:
#     f.seek(0) # In A mode, seek() dose work for it always start at the end of the file
#     f.write('Hello, World!\n')
with open('file-write.txt', 'r+', encoding="utf-8") as f:
    # f.seek(0) # In R+ mode, seek() dose work for it always start at the beginning of the file
    f.read()
    f.write('min, World!\n')