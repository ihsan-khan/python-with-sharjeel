# Classes and Functions in Python - Detailed Explanation

## Functions in Python

### What is a Function?
A function is a reusable block of code that performs a specific task. It helps in organizing code, reducing repetition, and making programs more modular.

### Function Syntax
```python
def function_name(parameters):
    """docstring - optional documentation"""
    # function body
    return value  # optional
```

### Types of Functions

#### 1. Built-in Functions
```python
# Examples of built-in functions
print("Hello World")
len([1, 2, 3])
max(10, 20, 5)
type("hello")
```

#### 2. User-defined Functions
```python
# Simple function without parameters
def greet():
    return "Hello, World!"

print(greet())  # Output: Hello, World!

# Function with parameters
def add_numbers(a, b):
    """Adds two numbers and returns the result"""
    return a + b

result = add_numbers(5, 3)
print(result)  # Output: 8

# Function with default parameters
def power(base, exponent=2):
    """Calculate power with default exponent of 2"""
    return base ** exponent

print(power(3))     # Output: 9 (3^2)
print(power(3, 3))  # Output: 27 (3^3)

# Function with variable arguments (*args)
def sum_all(*numbers):
    """Sum all provided numbers"""
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_all(1, 2, 3))        # Output: 6
print(sum_all(1, 2, 3, 4, 5))  # Output: 15

# Function with keyword arguments (**kwargs)
def person_info(**info):
    """Display person information"""
    for key, value in info.items():
        print(f"{key}: {value}")

person_info(name="Alice", age=25, city="New York")
```

### Function Scope
```python
global_var = "I'm global"

def scope_demo():
    local_var = "I'm local"
    print(global_var)  # Can access global variables
    print(local_var)   # Can access local variables

scope_demo()
# print(local_var)  # This would cause an error - local_var not accessible outside function
```

### Lambda Functions (Anonymous Functions)
```python
# Regular function
def square(x):
    return x * x

# Equivalent lambda function
square_lambda = lambda x: x * x

print(square(5))         # Output: 25
print(square_lambda(5))  # Output: 25

# Using lambda with map, filter, etc.
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]
```

---

## Classes in Python

### What is a Class?
A class is a blueprint for creating objects. It defines the properties (attributes) and behaviors (methods) that objects of that class will have.

### Class Syntax
```python
class ClassName:
    """Optional class documentation"""
    
    # Class attribute (shared by all instances)
    class_attribute = "I'm a class attribute"
    
    def __init__(self, parameters):
        """Constructor method - initializes instance attributes"""
        self.instance_attribute = parameters
    
    def method_name(self, parameters):
        """Instance method"""
        # method body
```

### Creating a Simple Class
```python
class Dog:
    """A simple Dog class"""
    
    # Class attribute
    species = "Canis familiaris"
    
    def __init__(self, name, age):
        """Initialize dog with name and age"""
        self.name = name    # Instance attribute
        self.age = age      # Instance attribute
    
    def bark(self):
        """Make the dog bark"""
        return f"{self.name} says Woof!"
    
    def describe(self):
        """Describe the dog"""
        return f"{self.name} is {self.age} years old and is a {self.species}"

# Creating objects (instances) of the Dog class
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(dog1.bark())      # Output: Buddy says Woof!
print(dog2.describe())  # Output: Max is 5 years old and is a Canis familiaris
print(Dog.species)      # Output: Canis familiaris (accessing class attribute)
```

### Class Methods and Static Methods
```python
class Calculator:
    """A calculator class demonstrating different method types"""
    
    def __init__(self, value=0):
        self.value = value
    
    # Instance method - operates on instance data
    def add(self, x):
        self.value += x
        return self.value
    
    # Class method - operates on class-level data
    @classmethod
    def from_string(cls, string):
        """Alternative constructor that creates object from string"""
        value = int(string)
        return cls(value)
    
    # Static method - doesn't operate on instance or class data
    @staticmethod
    def multiply(a, b):
        """Multiply two numbers"""
        return a * b

# Using different method types
calc = Calculator(10)
print(calc.add(5))  # Output: 15 (instance method)

calc2 = Calculator.from_string("25")  # Class method as alternative constructor
print(calc2.value)  # Output: 25

result = Calculator.multiply(4, 5)  # Static method
print(result)  # Output: 20
```

### Inheritance
```python
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("Subclass must implement this method")

# Child class inheriting from Animal
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Using inheritance
cat = Cat("Whiskers")
dog = Dog("Buddy")

print(cat.speak())  # Output: Whiskers says Meow!
print(dog.speak())  # Output: Buddy says Woof!
```

### Encapsulation and Properties
```python
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self._account_holder = account_holder  # Protected attribute
        self.__balance = balance               # Private attribute
    
    # Getter property
    @property
    def balance(self):
        return self.__balance
    
    # Setter property with validation
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = amount
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            raise ValueError("Invalid withdrawal amount")

# Using the BankAccount class
account = BankAccount("Alice", 1000)
account.deposit(500)
account.withdraw(200)
print(account.balance)  # Output: 1300

# account.__balance  # This would cause an error - attribute is private
```

### Special Methods (Magic/Dunder Methods)
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __len__(self):
        return int((self.x**2 + self.y**2)**0.5)

v1 = Vector(2, 3)
v2 = Vector(1, 2)
v3 = v1 + v2  # Uses __add__ method

print(v1)        # Output: Vector(2, 3) (uses __str__)
print(v1 + v2)   # Output: Vector(3, 5)
print(v1 == v2)  # Output: False (uses __eq__)
print(len(v1))   # Output: 3 (uses __len__)
```

## Key Differences Between Functions and Classes

| Aspect | Functions | Classes |
|--------|-----------|---------|
| **Purpose** | Perform specific tasks | Create objects with data and behavior |
| **Usage** | Called directly | Instantiated to create objects |
| **Data** | Operate on passed parameters | Encapsulate data within objects |
| **Reusability** | Code reuse through function calls | Blueprint for creating multiple objects |
| **State** | Stateless (generally) | Maintain state through attributes |

## Practical Example Combining Both
```python
# Utility functions
def validate_email(email):
    """Validate email format"""
    return '@' in email and '.' in email

def send_email(to, subject, message):
    """Simulate sending email"""
    print(f"Email sent to {to}: {subject} - {message}")

# Class using the functions
class User:
    def __init__(self, name, email):
        if not validate_email(email):
            raise ValueError("Invalid email format")
        self.name = name
        self.email = email
    
    def send_welcome_email(self):
        subject = "Welcome to our platform!"
        message = f"Hello {self.name}, welcome to our service!"
        send_email(self.email, subject, message)
    
    def __str__(self):
        return f"User: {self.name} ({self.email})"

# Using the class and functions
user = User("John Doe", "john@example.com")
user.send_welcome_email()
print(user)  # Output: User: John Doe (john@example.com)
```

This comprehensive overview covers the fundamental concepts of functions and classes in Python, which are essential for object-oriented programming and code organization.