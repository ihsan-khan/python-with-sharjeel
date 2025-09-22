## What is a Lambda Function?

A **lambda function** is a small, anonymous function defined using the `lambda` keyword. Unlike regular functions defined with `def`, lambda functions are:
- Anonymous (no name)
- Typically single-line
- Limited to a single expression
- Often used for short, simple operations

## Basic Syntax

```python
lambda arguments: expression
```

## Simple Examples

### Basic Lambda Functions
```python
# Equivalent regular function
def square(x):
    return x * x

# Lambda equivalent
square_lambda = lambda x: x * x

print(square(5))         # Output: 25
print(square_lambda(5))  # Output: 25

# Lambda function that adds two numbers
add = lambda a, b: a + b
print(add(10, 20))  # Output: 30

# Lambda with no arguments
greet = lambda: "Hello, World!"
print(greet())  # Output: Hello, World!

# Lambda with multiple arguments
multiply = lambda x, y, z: x * y * z
print(multiply(2, 3, 4))  # Output: 24
```

## Lambda Functions with Built-in Functions

### 1. Using with `map()`
```python
# Square all numbers in a list
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]

# Convert strings to uppercase
names = ['alice', 'bob', 'charlie']
upper_names

# Lambda Functions in Python - Complete Guide

## What is a Lambda Function?

A **lambda function** is a small, anonymous function defined using the `lambda` keyword. Unlike regular functions defined with `def`, lambda functions are:
- Anonymous (no name)
- Typically single-line
- Limited to a single expression
- Often used for short, simple operations

## Basic Syntax

```python
lambda arguments: expression
```

## Simple Examples

### Basic Lambda Functions
```python
# Equivalent regular function
def square(x):
    return x * x

# Lambda equivalent
square_lambda = lambda x: x * x

print(square(5))         # Output: 25
print(square_lambda(5))  # Output: 25

# Lambda function that adds two numbers
add = lambda a, b: a + b
print(add(10, 20))  # Output: 30

# Lambda with no arguments
greet = lambda: "Hello, World!"
print(greet())  # Output: Hello, World!

# Lambda with multiple arguments
multiply = lambda x, y, z: x * y * z
print(multiply(2, 3, 4))  # Output: 24
```

## Lambda Functions with Built-in Functions

### 1. Using with `map()`
```python
# Square all numbers in a list
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]

# Convert strings to uppercase
names = ['alice', 'bob', 'charlie']
upper_names = list(map(lambda name: name.upper(), names))
print(upper_names)  # Output: ['ALICE', 'BOB', 'CHARLIE']

# Multiple iterables with map
list1 = [1, 2, 3]
list2 = [10, 20, 30]
result = list(map(lambda x, y: x + y, list1, list2))
print(result)  # Output: [11, 22, 33]
```

### 2. Using with `filter()`
```python
# Filter even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8, 10]

# Filter strings longer than 5 characters
words = ['apple', 'banana', 'cat', 'dog', 'elephant']
long_words = list(filter(lambda word: len(word) > 5, words))
print(long_words)  # Output: ['banana', 'elephant']

# Filter positive numbers
mixed_numbers = [-5, 2, -3, 8, -1, 10, 0]
positive = list(filter(lambda x: x > 0, mixed_numbers))
print(positive)  # Output: [2, 8, 10]
```

### 3. Using with `reduce()`
```python
from functools import reduce

# Sum of all numbers
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
print(total)  # Output: 15

# Find maximum number
max_num = reduce(lambda x, y: x if x > y else y, numbers)
print(max_num)  # Output: 5

# String concatenation
words = ['Python', ' is', ' awesome!']
sentence = reduce(lambda x, y: x + y, words)
print(sentence)  # Output: Python is awesome!
```

### 4. Using with `sorted()`
```python
# Sort by string length
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
sorted_by_length = sorted(fruits, key=lambda x: len(x))
print(sorted_by_length)  # Output: ['date', 'apple', 'banana', 'cherry', 'elderberry']

# Sort by last character
sorted_by_last_char = sorted(fruits, key=lambda x: x[-1])
print(sorted_by_last_char)  # Output: ['banana', 'apple', 'date', 'cherry', 'elderberry']

# Complex sorting with dictionaries
students = [
    {'name': 'Alice', 'age': 25, 'grade': 85},
    {'name': 'Bob', 'age': 22, 'grade': 92},
    {'name': 'Charlie', 'age': 23, 'grade': 78}
]

# Sort by grade
sorted_by_grade = sorted(students, key=lambda x: x['grade'])
print([s['name'] for s in sorted_by_grade])  # Output: ['Charlie', 'Alice', 'Bob']

# Sort by age then grade
sorted_complex = sorted(students, key=lambda x: (x['age'], x['grade']))
print([(s['name'], s['age'], s['grade']) for s in sorted_complex])
# Output: [('Bob', 22, 92), ('Charlie', 23, 78), ('Alice', 25, 85)]
```

## Advanced Lambda Examples

### 1. Conditional Logic in Lambda
```python
# Lambda with conditional (ternary operator)
check_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check_even(4))  # Output: Even
print(check_even(7))  # Output: Odd

# Multiple conditions
grade_check = lambda score: "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"
print(grade_check(95))  # Output: A
print(grade_check(75))  # Output: C
print(grade_check(60))  # Output: F
```

### 2. Nested Lambda Functions
```python
# Lambda returning another lambda
power_function = lambda exponent: lambda base: base ** exponent

# Create specific power functions
square = power_function(2)
cube = power_function(3)

print(square(5))  # Output: 25
print(cube(3))    # Output: 27

# Another example: calculator functions
calculator = {
    'add': lambda x, y: x + y,
    'subtract': lambda x, y: x - y,
    'multiply': lambda x, y: x * y,
    'divide': lambda x, y: x / y if y != 0 else "Error"
}

print(calculator['add'](10, 5))       # Output: 15
print(calculator['multiply'](4, 5))   # Output: 20
print(calculator['divide'](10, 0))    # Output: Error
```

### 3. Lambda with Default Arguments
```python
# Lambda with default parameters
greet = lambda name, greeting="Hello": f"{greeting}, {name}!"
print(greet("Alice"))              # Output: Hello, Alice!
print(greet("Bob", "Hi"))          # Output: Hi, Bob!

# Multiple default parameters
calculate = lambda x, y=1, z=1: x * y * z
print(calculate(5))        # Output: 5
print(calculate(5, 2))     # Output: 10
print(calculate(5, 2, 3))  # Output: 30
```

### 4. Lambda with *args and **kwargs
```python
# Lambda with variable arguments
sum_all = lambda *args: sum(args)
print(sum_all(1, 2, 3))        # Output: 6
print(sum_all(1, 2, 3, 4, 5))  # Output: 15

# Lambda with keyword arguments
create_person = lambda **kwargs: kwargs
person = create_person(name="Alice", age=25, city="NY")
print(person)  # Output: {'name': 'Alice', 'age': 25, 'city': 'NY'}

# Combined usage
flexible_lambda = lambda x, *args, **kwargs: {
    'x': x,
    'args': args,
    'kwargs': kwargs
}
result = flexible_lambda(10, 20, 30, name="Alice", age=25)
print(result)
# Output: {'x': 10, 'args': (20, 30), 'kwargs': {'name': 'Alice', 'age': 25}}
```

## Practical Real-World Examples

### Example 1: Data Processing
```python
# Process employee data
employees = [
    {'name': 'Alice', 'salary': 50000, 'department': 'IT'},
    {'name': 'Bob', 'salary': 60000, 'department': 'HR'},
    {'name': 'Charlie', 'salary': 55000, 'department': 'IT'},
    {'name': 'Diana', 'salary': 70000, 'department': 'Finance'}
]

# Filter IT department employees
it_employees = list(filter(lambda emp: emp['department'] == 'IT', employees))
print([emp['name'] for emp in it_employees])  # Output: ['Alice', 'Charlie']

# Increase salary by 10% for IT department
updated_salaries = list(map(
    lambda emp: {**emp, 'salary': round(emp['salary'] * 1.1)} 
    if emp['department'] == 'IT' else emp, 
    employees
))
for emp in updated_salaries:
    print(f"{emp['name']}: ${emp['salary']}")
```

### Example 2: Event Handling (GUI applications)
```python
# Simulating button click events
class Button:
    def __init__(self, name):
        self.name = name
        self.click_handlers = []
    
    def on_click(self, handler):
        self.click_handlers.append(handler)
    
    def click(self):
        for handler in self.click_handlers:
            handler(self.name)

# Create buttons
button1 = Button("Submit")
button2 = Button("Cancel")

# Add lambda handlers
button1.on_click(lambda name: print(f"{name} button clicked!"))
button2.on_click(lambda name: print(f"{name} action cancelled"))

# Simulate clicks
button1.click()  # Output: Submit button clicked!
button2.click()  # Output: Cancel action cancelled
```

### Example 3: Mathematical Operations
```python
# Mathematical function composition
def compose(f, g):
    return lambda x: f(g(x))

# Define mathematical functions as lambdas
square = lambda x: x**2
increment = lambda x: x + 1
double = lambda x: x * 2

# Compose functions
square_after_increment = compose(square, increment)
increment_after_square = compose(increment, square)

print(square_after_increment(5))  # Output: 36 ( (5+1)^2 )
print(increment_after_square(5))  # Output: 26 ( (5^2) + 1 )

# Triple composition
triple_operation = compose(double, compose(increment, square))
print(triple_operation(4))  # Output: 34 ( 2 * ((4^2) + 1) )
```

### Example 4: Sorting Complex Data Structures
```python
# Sort list of tuples
students = [('Alice', 85, 'A'), ('Bob', 92, 'A'), ('Charlie', 78, 'B')]

# Sort by grade (third element)
sorted_by_grade = sorted(students, key=lambda x: x[2])
print(sorted_by_grade)
# Output: [('Alice', 85, 'A'), ('Bob', 92, 'A'), ('Charlie', 78, 'B')]

# Sort by score descending
sorted_by_score = sorted(students, key=lambda x: x[1], reverse=True)
print(sorted_by_score)
# Output: [('Bob', 92, 'A'), ('Alice', 85, 'A'), ('Charlie', 78, 'B')]

# Sort files by extension
files = ['document.pdf', 'image.jpg', 'script.py', 'data.csv', 'readme.txt']
sorted_files = sorted(files, key=lambda x: x.split('.')[-1])
print(sorted_files)
# Output: ['data.csv', 'image.jpg', 'document.pdf', 'script.py', 'readme.txt']
```

## Lambda vs Regular Functions: Key Differences

```python
# Regular function
def regular_multiply(x, y):
    """Multiply two numbers and return result"""
    return x * y

# Lambda function
lambda_multiply = lambda x, y: x * y

# Comparison
print(regular_multiply(5, 3))   # Output: 15
print(lambda_multiply(5, 3))    # Output: 15

# Differences:
# 1. Name
print(regular_multiply.__name__)  # Output: regular_multiply
print(lambda_multiply.__name__)   # Output: <lambda>

# 2. Documentation
print(regular_multiply.__doc__)   # Output: Multiply two numbers and return result

# 3. Complexity - Lambda limited to single expression
def complex_operation(x, y):
    result = x * y
    if result > 100:
        return "Large"
    else:
        return "Small"

# This would be difficult/impossible with lambda alone
```

## Best Practices and Limitations

### When to Use Lambda:
1. **Short, simple operations**
2. **Functions used only once**
3. **As arguments to higher-order functions**
4. **When you need a quick throwaway function**

### When to Avoid Lambda:
1. **Complex logic requiring multiple statements**
2. **Functions that need documentation**
3. **Functions that will be reused**
4. **When it reduces readability**

```python
# Good use of lambda
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))

# Poor use of lambda (better as regular function)
# Complex logic that should be a named function
complex_lambda = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero" if x == 0 else "Unknown"

# Better as:
def classify_number(x):
    if x > 0:
        return "Positive"
    elif x < 0:
        return "Negative"
    elif x == 0:
        return "Zero"
    else:
        return "Unknown"
```

Lambda functions are powerful tools for writing concise, functional-style code in Python. They shine when used appropriately with functions like `map()`, `filter()`, and `sorted()`, but should be used judiciously to maintain code readability.