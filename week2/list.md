# Python Lists - Complete Guide

Lists are one of Python's most versatile and commonly used data structures. Here's a comprehensive explanation:

## What is a List?
A list is an **ordered, mutable collection** of items that can be of different data types.

```python
# Creating lists
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
```

## 1. Creating Lists

```python
# Empty list
empty_list = []
empty_list = list()

# List with items
fruits = ["apple", "banana", "cherry"]

# Using list constructor
numbers = list((1, 2, 3, 4, 5))  # Note double parentheses
```

## 2. Basic Operations

### Accessing Elements
```python
fruits = ["apple", "banana", "cherry", "date"]

print(fruits[0])    # "apple" - first element
print(fruits[-1])   # "date" - last element
print(fruits[1:3])  # ["banana", "cherry"] - slicing
```

### Modifying Lists
```python
fruits = ["apple", "banana", "cherry"]

fruits[1] = "blueberry"  # Modify element
print(fruits)  # ["apple", "blueberry", "cherry"]
```

## 3. List Methods (Complete List)

### Adding Elements
```python
fruits = ["apple", "banana"]

# append() - Add single element to end
fruits.append("cherry")  # ["apple", "banana", "cherry"]

# extend() - Add multiple elements
fruits.extend(["date", "elderberry"])  # Adds two items

# insert() - Add element at specific position
fruits.insert(1, "blueberry")  # ["apple", "blueberry", "banana", "cherry"]
```

### Removing Elements
```python
fruits = ["apple", "banana", "cherry", "banana"]

# remove() - Remove first occurrence of value
fruits.remove("banana")  # ["apple", "cherry", "banana"]

# pop() - Remove and return element at index (default last)
removed = fruits.pop(1)  # removes "cherry", returns "cherry"

# clear() - Remove all elements
fruits.clear()  # []
```

### Finding Elements
```python
fruits = ["apple", "banana", "cherry"]

# index() - Find index of first occurrence
position = fruits.index("banana")  # Returns 1

# count() - Count occurrences of value
count = fruits.count("apple")  # Returns 1
```

### Sorting and Reversing
```python
numbers = [3, 1, 4, 1, 5, 9, 2]

# sort() - Sort in place (modifies original)
numbers.sort()  # [1, 1, 2, 3, 4, 5, 9]
numbers.sort(reverse=True)  # [9, 5, 4, 3, 2, 1, 1]

# sorted() - Return new sorted list (doesn't modify original)
sorted_numbers = sorted(numbers)  # Original unchanged

# reverse() - Reverse list in place
numbers.reverse()  # [2, 9, 5, 1, 4, 1, 3]
```

### Copying Lists
```python
original = [1, 2, 3]

# copy() - Create shallow copy
new_list = original.copy()  # [1, 2, 3]

# list() constructor - Also creates copy
another_copy = list(original)
```

## 4. List Comprehensions (Powerful Feature!)

```python
# Create list of squares
squares = [x**2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# With condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]
# [0, 4, 16, 36, 64]

# Nested comprehensions
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## 5. Useful Built-in Functions with Lists

```python
numbers = [1, 2, 3, 4, 5]

# len() - Get length
length = len(numbers)  # 5

# min() and max() - Find minimum and maximum
min_val = min(numbers)  # 1
max_val = max(numbers)  # 5

# sum() - Sum all elements
total = sum(numbers)  # 15

# any() and all() - Check conditions
has_positive = any(x > 0 for x in numbers)  # True
all_positive = all(x > 0 for x in numbers)  # True
```

## 6. List Slicing (Advanced)

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[2:6])    # [2, 3, 4, 5] - items 2 to 5
print(numbers[:4])     # [0, 1, 2, 3] - first 4 items
print(numbers[5:])     # [5, 6, 7, 8, 9] - from index 5 to end
print(numbers[::2])    # [0, 2, 4, 6, 8] - every 2nd item
print(numbers[::-1])   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] - reversed
```

## 7. Practical Examples

### Example 1: Shopping Cart
```python
cart = []
cart.append({"item": "book", "price": 15.99})
cart.append({"item": "pen", "price": 1.50})

total = sum(item["price"] for item in cart)
print(f"Total: ${total}")  # Total: $17.49
```

### Example 2: Student Grades
```python
grades = [85, 92, 78, 90, 65]
average = sum(grades) / len(grades)
top_grade = max(grades)
print(f"Average: {average}, Top: {top_grade}")
```

### Example 3: Matrix Operations
```python
# 2D list (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access element
print(matrix[1][2])  # 6 (row 1, column 2)

# Transpose matrix
transposed = [[row[i] for row in matrix] for i in range(3)]
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
```

## 8. Important Characteristics

- **Ordered**: Items maintain their order
- **Mutable**: Can be changed after creation
- **Dynamic**: Can grow and shrink as needed
- **Heterogeneous**: Can contain different data types
- **Indexable**: Access elements by position (0-based)
- **Nestable**: Can contain other lists

## 9. Performance Considerations

- **Append**: O(1) time complexity (fast)
- **Insert**: O(n) time complexity (slow for large lists)
- **Search**: O(n) time complexity (linear search)
- **Sort**: O(n log n) time complexity

## 10. Common Pitfalls

```python
# Shallow copy vs deep copy
original = [[1, 2], [3, 4]]
shallow_copy = original.copy()
shallow_copy[0][0] = 99
print(original)  # [[99, 2], [3, 4]] - original changed!

# Use deepcopy for nested lists
import copy
deep_copy = copy.deepcopy(original)
```

Lists are incredibly versatile and essential for Python programming. They're used in almost every Python application!