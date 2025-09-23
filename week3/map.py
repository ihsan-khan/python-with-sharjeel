# square of numbers
numbers = [1,2,3,4]
def square_func(x):
    return x**2

squared = list(map(square_func, numbers))
print(squared)

# double of numbers
def double(number):
    return number * 2

doubled = list(map(double, numbers))
print(doubled)

# add two lists
def add(x, y):
    return x + y

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

added = list(map(add, numbers1, numbers2))
print(added)

#map with built-in functions
name = ['alice', 'bob', 'charlie']
capitalized = list(map(str.capitalize, name))
print(capitalized)

# convert list of strings to list of integers
str_numbers = ['1', '2', '3', '4']
int_numbers = list(map(int, str_numbers))
print(int_numbers)

# transformation with custom function
def custom_transform(name):
    return {
        'name': name.upper(),
        'length': len(name),
        'first_letter': name[0]
    }
person = ['alice', 'bob', 'charlie']
transformed = list(map(custom_transform, person))
print(transformed)
