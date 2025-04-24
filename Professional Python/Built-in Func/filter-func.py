nums = [1,3,5,-4,-3]

def is_negative(num):
    if num < 0:
        return True
    else:
        return False
    
result = list(filter(lambda num: num < 0, nums))
result = list(filter(lambda x: x % 2 == 1, nums))

nams = ['Ali', 'Veli', 'Ayse', 'Fatma', 'Zeynep']
result = list(filter(lambda name: name[0] == "a", nams))

result = list(map(lambda name: name.upper(), nams))
