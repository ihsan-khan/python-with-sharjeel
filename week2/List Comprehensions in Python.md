# List Comprehensions in Python

List comprehensions provide a concise way to create lists in Python. They are more compact and faster than traditional for loops.

## Basic Syntax

```python
[expression for item in iterable]
```

## 1. Basic Examples

### Simple Transformation
```python
# Traditional for loop
numbers = [1, 2, 3, 4, 5]
squares = []
for num in numbers:
    squares.append(num ** 2)

# List comprehension (same result)
squares = [num ** 2 for num in numbers]
# Result: [1, 4, 9, 16, 25]
```

### String Manipulation
```python
words = ["hello", "world", "python"]
capitalized = [word.upper() for word in words]
# Result: ['HELLO', 'WORLD', 'PYTHON']
```

## 2. List Comprehension with Condition

### Syntax with Condition
```python
[expression for item in iterable if condition]
```

### Examples with Conditions
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Even numbers only
evens = [num for num in numbers if num % 2 == 0]
# Result: [2, 4, 6, 8, 10]

# Numbers greater than 5
greater_than_5 = [num for num in numbers if num > 5]
# Result: [6, 7, 8, 9, 10]
```

## 3. If-Else in List Comprehension

### Syntax with If-Else
```python
[expression_if_true if condition else expression_if_false for item in iterable]
```

### Examples with If-Else
```python
numbers = [1, 2, 3, 4, 5]

# Mark even/odd
even_odd = ["even" if num % 2 == 0 else "odd" for num in numbers]
# Result: ['odd', 'even', 'odd', 'even', 'odd']

# Square even numbers, cube odd numbers
transformed = [num ** 2 if num % 2 == 0 else num ** 3 for num in numbers]
# Result: [1, 4, 27, 16, 125]
```

## 4. Nested List Comprehensions

### Nested Loops
```python
# Traditional nested loops
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = []
for row in matrix:
    for num in row:
        flattened.append(num)

# List comprehension
flattened = [num for row in matrix for num in row]
# Result: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### 2D Matrix Operations
```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Transpose matrix
transposed = [[row[i] for row in matrix] for i in range(3)]
# Result: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# Sum of each row
row_sums = [sum(row) for row in matrix]
# Result: [6, 15, 24]
```

## 5. Practical Examples

### Example 1: Data Cleaning
```python
# Remove empty strings and strip whitespace
data = ["  apple  ", "", "banana", "  ", "cherry"]
cleaned = [item.strip() for item in data if item.strip()]
# Result: ['apple', 'banana', 'cherry']
```

### Example 2: Price Calculations
```python
prices = [100, 200, 300, 400, 500]
discounted_prices = [price * 0.9 for price in prices if price > 200]
# Result: [270.0, 360.0, 450.0] (10% discount on prices > 200)
```

### Example 3: String Processing
```python
sentences = ["Hello world", "Python is great", "List comprehensions rock"]
word_lengths = [[len(word) for word in sentence.split()] for sentence in sentences]
# Result: [[5, 5], [6, 2, 5], [4, 14, 4]]
```

## 6. Multiple Conditions

### Using Multiple If Conditions
```python
numbers = range(1, 21)

# Numbers divisible by 2 and 3
result = [num for num in numbers if num % 2 == 0 if num % 3 == 0]
# Result: [6, 12, 18]

# Equivalent to:
result = [num for num in numbers if num % 2 == 0 and num % 3 == 0]
```

### Complex Conditions
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Numbers that are even or divisible by 3, but not both
result = [num for num in numbers if (num % 2 == 0 or num % 3 == 0) and not (num % 2 == 0 and num % 3 == 0)]
# Result: [2, 3, 4, 8, 9, 10, 14, 15]
```

## 7. Dictionary and Set Comprehensions

### Dictionary Comprehension
```python
names = ["Alice", "Bob", "Charlie"]
name_lengths = {name: len(name) for name in names}
# Result: {'Alice': 5, 'Bob': 3, 'Charlie': 7}
```

### Set Comprehension
```python
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique_squares = {num ** 2 for num in numbers}
# Result: {16, 1, 4, 9}
```

## 8. Performance Benefits

List comprehensions are generally faster than equivalent for loops:

```python
import timeit

# For loop version
def for_loop():
    result = []
    for i in range(10000):
        result.append(i * 2)
    return result

# List comprehension version
def list_comp():
    return [i * 2 for i in range(10000)]

# Timing comparison
time_for = timeit.timeit(for_loop, number=1000)
time_comp = timeit.timeit(list_comp, number=1000)

print(f"For loop: {time_for:.4f} seconds")
print(f"List comprehension: {time_comp:.4f} seconds")
```

## 9. When to Use List Comprehensions

### Good Use Cases:
- Simple transformations and filtering
- Creating new lists from existing iterables
- Readable one-liners for simple operations

### Avoid When:
- The logic is too complex (becomes hard to read)
- You need multiple statements in the loop
- You need to handle exceptions within the comprehension

## 10. Advanced Examples

### Example 1: Nested List with Conditions
```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Get elements greater than 4 from all rows
result = [num for row in matrix for num in row if num > 4]
# Result: [5, 6, 7, 8, 9]
```

### Example 2: Multiple Iterables
```python
# Cartesian product
colors = ["red", "green", "blue"]
sizes = ["S", "M", "L"]

combinations = [(color, size) for color in colors for size in sizes]
# Result: [('red', 'S'), ('red', 'M'), ('red', 'L'), 
#          ('green', 'S'), ('green', 'M'), ('green', 'L'),
#          ('blue', 'S'), ('blue', 'M'), ('blue', 'L')]
```

### Example 3: File Operations
```python
# Read lines from file and process
lines = [line.strip().upper() for line in open('file.txt') if line.strip()]
```

## Key Advantages:

1. **Concise**: Less code than equivalent for loops
2. **Readable**: Once familiar, easier to understand
3. **Faster**: Generally better performance
4. **Pythonic**: Considered good Python style

## Remember:
- Keep comprehensions readable
- Avoid nesting too deeply
- Use traditional loops for complex logic
- List comprehensions create new lists (they don't modify the original)

