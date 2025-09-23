number = [1,2,3,4]
square = []
for i in number:
    square.append(i*2)
print(square)

# Using map function
def square_func(x):
    return x*2
squared = list(map(square_func, number))
print(squared)

# Using list comprehension
squared = [x*2 for x in number]
print(squared)

# Using lambda function
squared = list(map(lambda x: x*2, number))
print(squared)