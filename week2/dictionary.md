## What is a Dictionary?

A dictionary in Python is a **collection of key-value pairs**. It's like a real-life dictionary where you look up a word (key) to find its definition (value).

## Key Characteristics:
- **Unordered** (in Python 3.6 and earlier, ordered in 3.7+)
- **Mutable** (can be changed)
- **No duplicate keys** allowed
- Keys must be **immutable** (strings, numbers, tuples)

## Creating a Dictionary

### Method 1: Using curly braces `{}`
```python
# Empty dictionary
my_dict = {}

# Dictionary with items
student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science",
    "gpa": 3.8
}
```

### Method 2: Using `dict()` constructor
```python
# From key-value pairs
student = dict(name="Bob", age=21, major="Mathematics")

# From list of tuples
student = dict([("name", "Charlie"), ("age", 22), ("major", "Physics")])
```

## Accessing Values

```python
student = {"name": "Alice", "age": 20, "major": "CS"}

# Using square brackets
print(student["name"])  # Output: Alice

# Using get() method (safer - returns None if key doesn't exist)
print(student.get("age"))  # Output: 20
print(student.get("grade"))  # Output: None
print(student.get("grade", "Not available"))  # Output: Not available
```

## Adding and Modifying Items

```python
student = {"name": "Alice", "age": 20}

# Adding new key-value pair
student["major"] = "Computer Science"

# Modifying existing value
student["age"] = 21

print(student)  # Output: {'name': 'Alice', 'age': 21, 'major': 'Computer Science'}
```

## Removing Items

```python
student = {"name": "Alice", "age": 20, "major": "CS"}

# Using del keyword
del student["age"]

# Using pop() method (returns the value)
major = student.pop("major")
print(major)  # Output: CS

# Using popitem() (removes last inserted item in Python 3.7+)
last_item = student.popitem()
print(last_item)  # Output: ('name', 'Alice')

# Clear all items
student.clear()
```

## Dictionary Methods

```python
person = {"name": "John", "age": 30, "city": "New York"}

# Get all keys
print(person.keys())  # Output: dict_keys(['name', 'age', 'city'])

# Get all values
print(person.values())  # Output: dict_values(['John', 30, 'New York'])

# Get all key-value pairs
print(person.items())  # Output: dict_items([('name', 'John'), ('age', 30), ('city', 'New York')])

# Check if key exists
print("age" in person)  # Output: True
print("country" in person)  # Output: False

# Update dictionary with another dictionary
person.update({"country": "USA", "age": 31})
print(person)  # Output: {'name': 'John', 'age': 31, 'city': 'New York', 'country': 'USA'}
```

## Iterating Through a Dictionary

```python
student = {"name": "Alice", "age": 20, "major": "CS"}

# Iterate through keys
for key in student:
    print(key, student[key])

# Iterate through key-value pairs
for key, value in student.items():
    print(f"{key}: {value}")
```

## Dictionary Comprehensions

```python
# Create dictionary with squares
squares = {x: x**2 for x in range(1, 6)}
print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Create dictionary from two lists
keys = ['a', 'b', 'c']
values = [1, 2, 3]
mapped_dict = {k: v for k, v in zip(keys, values)}
print(mapped_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}
```

## Nested Dictionaries

```python
# Dictionary containing other dictionaries
school = {
    "student1": {"name": "Alice", "age": 20},
    "student2": {"name": "Bob", "age": 21},
    "student3": {"name": "Charlie", "age": 22}
}

# Access nested values
print(school["student1"]["name"])  # Output: Alice

# Add new nested dictionary
school["student4"] = {"name": "Diana", "age": 19}
```

## Real-World Example

```python
# Phone book application
phone_book = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9012"
}

def add_contact(name, number):
    phone_book[name] = number
    print(f"Added {name}: {number}")

def find_contact(name):
    return phone_book.get(name, "Contact not found")

def show_all_contacts():
    for name, number in phone_book.items():
        print(f"{name}: {number}")

# Usage
add_contact("Diana", "555-3456")
print(find_contact("Alice"))  # Output: 555-1234
show_all_contacts()
```

## Common Use Cases:
- Storing configuration settings
- Counting occurrences of items
- Mapping relationships between data
- JSON data representation
- Caching/memoization

Dictionaries are extremely versatile and efficient for lookups, making them one of Python's most powerful data structures!