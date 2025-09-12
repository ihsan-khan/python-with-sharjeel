# For Loops with Lists in Python

For loops are fundamental for working with lists in Python. Here's a comprehensive guide with examples:

## Basic For Loop Syntax

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# Output:
# apple
# banana
# cherry
```

## 1. Basic Iteration Examples

### Example 1: Simple List Iteration
```python
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number * 2)

# Output: 2, 4, 6, 8, 10
```

### Example 2: List of Strings
```python
colors = ["red", "green", "blue", "yellow"]

for color in colors:
    print(f"I like {color} color!")

# Output:
# I like red color!
# I like green color!
# I like blue color!
# I like yellow color!
```

## 2. Using enumerate() - Get Index and Value

```python
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# Output:
# Index 0: apple
# Index 1: banana
# Index 2: cherry
```

### With Custom Start Index
```python
for index, fruit in enumerate(fruits, start=1):
    print(f"Fruit #{index}: {fruit}")

# Output:
# Fruit #1: apple
# Fruit #2: banana
# Fruit #3: cherry
```

## 3. Modifying List Elements

### Example 1: Capitalize Strings
```python
names = ["alice", "bob", "charlie"]
capitalized_names = []

for name in names:
    capitalized_names.append(name.capitalize())

print(capitalized_names)  # ['Alice', 'Bob', 'Charlie']
```

### Example 2: Double Numbers
```python
numbers = [1, 2, 3, 4, 5]

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2

print(numbers)  # [2, 4, 6, 8, 10]
```

## 4. Filtering Lists

### Example 1: Filter Even Numbers
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)  # [2, 4, 6, 8, 10]
```

### Example 2: Filter Strings by Length
```python
words = ["apple", "bat", "computer", "dog", "elephant"]
long_words = []

for word in words:
    if len(word) > 3:
        long_words.append(word)

print(long_words)  # ['apple', 'computer', 'elephant']
```

## 5. Nested Lists (2D Lists)

### Example 1: Matrix Iteration
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for number in row:
        print(number, end=" ")
    print()  # New line after each row

# Output:
# 1 2 3
# 4 5 6
# 7 8 9
```

### Example 2: Student Grades
```python
students = [
    ["Alice", 85, 92, 78],
    ["Bob", 76, 88, 95],
    ["Charlie", 92, 90, 86]
]

for student in students:
    name = student[0]
    grades = student[1:]
    average = sum(grades) / len(grades)
    print(f"{name}: {average:.1f} average")

# Output:
# Alice: 85.0 average
# Bob: 86.3 average
# Charlie: 89.3 average
```

## 6. Practical Real-World Examples

### Example 1: Shopping Cart Total
```python
cart = [
    {"item": "book", "price": 15.99, "quantity": 2},
    {"item": "pen", "price": 1.50, "quantity": 5},
    {"item": "notebook", "price": 4.99, "quantity": 3}
]

total = 0
for product in cart:
    item_total = product["price"] * product["quantity"]
    total += item_total
    print(f"{product['item']}: ${item_total:.2f}")

print(f"Total: ${total:.2f}")

# Output:
# book: $31.98
# pen: $7.50
# notebook: $14.97
# Total: $54.45
```

### Example 2: Temperature Conversion
```python
celsius_temps = [0, 10, 20, 30, 40]
fahrenheit_temps = []

for temp in celsius_temps:
    fahrenheit = (temp * 9/5) + 32
    fahrenheit_temps.append(fahrenheit)

print("Celsius to Fahrenheit:")
for c, f in zip(celsius_temps, fahrenheit_temps):
    print(f"{c}°C = {f}°F")

# Output:
# Celsius to Fahrenheit:
# 0°C = 32.0°F
# 10°C = 50.0°F
# 20°C = 68.0°F
# 30°C = 86.0°F
# 40°C = 104.0°F
```

## 7. Using zip() for Multiple Lists

```python
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
grades = ["A", "A", "C"]

for name, score, grade in zip(names, scores, grades):
    print(f"{name}: Score={score}, Grade={grade}")

# Output:
# Alice: Score=85, Grade=A
# Bob: Score=92, Grade=A
# Charlie: Score=78, Grade=C
```

## 8. Break and Continue in List Loops

### Example 1: Break - Stop Early
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num > 5:
        break  # Stop when number > 5
    print(num)

# Output: 1, 2, 3, 4, 5
```

### Example 2: Continue - Skip Elements
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num % 2 == 0:  # Skip even numbers
        continue
    print(num)

# Output: 1, 3, 5, 7, 9 (only odd numbers)
```

## 9. List Comprehension vs For Loop

### For Loop (Traditional)
```python
numbers = [1, 2, 3, 4, 5]
squares = []

for num in numbers:
    squares.append(num ** 2)

print(squares)  # [1, 4, 9, 16, 25]
```

### List Comprehension (Compact)
```python
numbers = [1, 2, 3, 4, 5]
squares = [num ** 2 for num in numbers]

print(squares)  # [1, 4, 9, 16, 25]
```

## 10. Error Handling in List Loops

```python
mixed_list = [1, 2, "3", 4, "five", 6]

valid_numbers = []
for item in mixed_list:
    try:
        number = int(item)
        valid_numbers.append(number)
    except ValueError:
        print(f"Skipping invalid value: {item}")

print(valid_numbers)  # [1, 2, 3, 4, 6]

# Output:
# Skipping invalid value: five
```

## Key Points to Remember:

1. **Simple Syntax**: `for item in list:`
2. **Order**: Processes items in the order they appear in the list
3. **Flexible**: Can work with any iterable, not just lists
4. **Readable**: Very clear and easy to understand
5. **Versatile**: Can be used for filtering, transforming, and processing data

For loops are essential for working with lists in Python and are used in almost every Python program!