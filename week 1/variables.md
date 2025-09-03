# Variables in Python

Variables are fundamental building blocks in Python programming. They act as named containers that store data values in memory.

## What is a Variable?

A variable is a symbolic name that refers to a value stored in computer memory. Think of it as a labeled box where you can store information.

```python
# Simple variable assignment
name = "Alice"
age = 25
height = 5.8
is_student = True
```

## Variable Naming Rules

Python has specific rules for naming variables:

- Must start with a letter (a-z, A-Z) or underscore (_)
- Can contain letters, numbers, and underscores
- Cannot contain spaces or special characters
- Are case-sensitive (`age` ≠ `Age` ≠ `AGE`)
- Cannot use Python keywords (reserved words)

```python
# Valid variable names
first_name = "John"
_last_name = "Doe"
age2 = 30
MAX_VALUE = 100

# Invalid variable names
2nd_name = "Smith"  # Cannot start with number
my-variable = 10    # Cannot use hyphens
class = "Math"      # Cannot use keyword
```

## Variable Assignment

### Single Assignment
```python
x = 10
message = "Hello, World!"
```

### Multiple Assignment
```python
# Assign multiple variables in one line
a, b, c = 1, 2, 3

# Assign same value to multiple variables
x = y = z = 0
```

## Dynamic Typing

Python is dynamically typed, meaning you don't need to declare variable types explicitly:

```python
# Variable can change type
var = 10        # Now it's an integer
print(type(var))  # <class 'int'>

var = "Hello"   # Now it's a string
print(type(var))  # <class 'str'>

var = 3.14      # Now it's a float
print(type(var))  # <class 'float'>
```

## Data Types in Variables

Variables can hold different data types:

```python
# Integer
count = 10

# Float
price = 19.99

# String
name = "Alice"

# Boolean
is_active = True

# List
numbers = [1, 2, 3, 4, 5]

# Tuple
coordinates = (10, 20)

# Dictionary
person = {"name": "Bob", "age": 25}

# Set
unique_numbers = {1, 2, 3, 4}
```

## Variable Scope

Variables have different scopes depending on where they're defined:

### Global Scope
```python
global_var = "I'm global"

def my_function():
    print(global_var)  # Accessible

my_function()
```

### Local Scope
```python
def my_function():
    local_var = "I'm local"
    print(local_var)  # Accessible

my_function()
# print(local_var)  # Error: not accessible outside function
```

### Using `global` keyword
```python
x = 10

def modify_global():
    global x
    x = 20

modify_global()
print(x)  # Output: 20
```

## Best Practices

1. **Use descriptive names**: `student_count` instead of `sc`
2. **Follow naming conventions**:
   - snake_case for variables and functions
   - UPPERCASE for constants
   - CamelCase for classes

```python
# Good practices
student_count = 100
MAX_STUDENTS = 150
class StudentRecord: pass

# Avoid
sc = 100  # Not descriptive
```

3. **Initialize variables before use**
4. **Avoid using built-in function names as variables**

## Memory Management

Python handles memory management automatically:
- Variables are references to objects
- Memory is allocated when variables are created
- Garbage collection frees memory when variables are no longer referenced

```python
# Both variables point to the same object
a = [1, 2, 3]
b = a
b.append(4)
print(a)  # [1, 2, 3, 4] - both variables affected

# Create a copy to avoid this
c = a.copy()
c.append(5)
print(a)  # [1, 2, 3, 4] - original unchanged
```

## Type Hints (Python 3.5+)

While Python is dynamically typed, you can add type hints for better code clarity:

```python
def greet(name: str, age: int) -> str:
    return f"Hello {name}, you are {age} years old"

# Variables with type hints
count: int = 10
price: float = 19.99
names: list[str] = ["Alice", "Bob"]
```