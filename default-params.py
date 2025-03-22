def greeting(name, msg="Hello,"):
    return f"{msg} {name}"

result = greeting("Ali")
result1 = greeting("Ali", "Hi,")

print(result)
print(result1)