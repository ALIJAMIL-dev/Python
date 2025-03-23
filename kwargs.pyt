# Variable numbers of arguments: kwargs

def display_user(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

display_user(name='John', age=30, city='New York')