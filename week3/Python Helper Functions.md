# Python Helper Functions: Map, Filter, Reduce, and More - Detailed Guide

## 1. `map()` Function

### Purpose:
Applies a function to all items in an input list (or any iterable) and returns an iterator.

### Syntax:
```python
map(function, iterable, ...)
```

### Examples:
```python
# Basic map example
numbers = [1, 2, 3, 4, 5]

# Using lambda function
squared = map(lambda x: x**2, numbers)
print(list(squared))  # Output: [1, 4, 9, 16, 25]

# Using regular function
def double(x):
    return x * 2

doubled = map(double, numbers)
print(list(doubled))  # Output: [2, 4, 6, 8, 10]

# Map with multiple iterables
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))  # Output: [5, 7, 9]

# Map with strings
names = ['alice', 'bob', 'charlie']
capitalized = map(str.capitalize, names)
print(list(capitalized))  # Output: ['Alice', 'Bob', 'Charlie']

# Map with built-in functions
strings = ['1', '2', '3']
numbers = map(int, strings)
print(list(numbers))  # Output: [1, 2, 3]
```

## 2. `filter()` Function

### Purpose:
Filters elements from an iterable based on a function that returns True or False.

### Syntax:
```python
filter(function, iterable)
```

### Examples:
```python
# Basic filter example
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4, 6, 8, 10]

# Filter with regular function
def is_positive(x):
    return x > 0

mixed_numbers = [-5, 2, -3, 8, -1, 10]
positive_numbers = filter(is_positive, mixed_numbers)
print(list(positive_numbers))  # Output: [2, 8, 10]

# Filter with None (removes falsy values)
data = [0, 1, False, True, '', 'hello', None, [], [1, 2]]
truthy_values = filter(None, data)
print(list(truthy_values))  # Output: [1, True, 'hello', [1, 2]]

# Filter strings
words = ['apple', 'banana', 'cherry', 'date', 'elderberry']
long_words = filter(lambda word: len(word) > 5, words)
print(list(long_words))  # Output: ['banana', 'cherry', 'elderberry']
```

## 3. `reduce()` Function

### Purpose:
Applies a function cumulatively to the items of an iterable, from left to right, to reduce it to a single value.

**Note:** `reduce()` needs to be imported from `functools` module.

### Syntax:
```python
from functools import reduce
reduce(function, iterable[, initializer])
```

### Examples:
```python
from functools import reduce

# Sum of all numbers
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
print(total)  # Output: 15

# Product of all numbers
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120

# Find maximum number
max_num = reduce(lambda x, y: x if x > y else y, numbers)
print(max_num)  # Output: 5

# String concatenation
words = ['Hello', ' ', 'World', '!']
sentence = reduce(lambda x, y: x + y, words)
print(sentence)  # Output: Hello World!

# With initial value
numbers = [1, 2, 3]
result = reduce(lambda x, y: x + y, numbers, 10)
print(result)  # Output: 16 (10 + 1 + 2 + 3)
```

## 4. `zip()` Function

### Purpose:
Combines multiple iterables into a single iterable of tuples.

### Syntax:
```python
zip(iterable1, iterable2, ...)
```

### Examples:
```python
# Basic zip example
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
cities = ['NY', 'LA', 'Chicago']

zipped = zip(names, ages, cities)
print(list(zipped))  # Output: [('Alice', 25, 'NY'), ('Bob', 30, 'LA'), ('Charlie', 35, 'Chicago')]

# Unzipping
data = [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
names, ages = zip(*data)
print(names)  # Output: ('Alice', 'Bob', 'Charlie')
print(ages)   # Output: (25, 30, 35)

# Creating dictionaries from two lists
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'New York']
person_dict = dict(zip(keys, values))
print(person_dict)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Zip with different length iterables (shortest determines length)
list1 = [1, 2, 3]
list2 = ['a', 'b']
result = list(zip(list1, list2))
print(result)  # Output: [(1, 'a'), (2, 'b')]
```

## 5. `enumerate()` Function

### Purpose:
Adds counter to an iterable and returns it as an enumerate object.

### Syntax:
```python
enumerate(iterable, start=0)
```

### Examples:
```python
# Basic enumerate example
fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# Output:
# 0: apple
# 1: banana
# 2: cherry

# With custom start index
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")
# Output:
# 1: apple
# 2: banana
# 3: cherry

# Creating dictionary with index as key
fruit_dict = {index: fruit for index, fruit in enumerate(fruits)}
print(fruit_dict)  # Output: {0: 'apple', 1: 'banana', 2: 'cherry'}

# With strings
word = "Python"
for index, letter in enumerate(word):
    print(f"Position {index}: {letter}")
```

## 6. `sorted()` Function

### Purpose:
Returns a new sorted list from the items in iterable.

### Syntax:
```python
sorted(iterable, key=None, reverse=False)
```

### Examples:
```python
# Basic sorting
numbers = [3, 1, 4, 1, 5, 9, 2]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # Output: [1, 1, 2, 3, 4, 5, 9]

# Sorting strings
words = ['banana', 'apple', 'cherry', 'date']
sorted_words = sorted(words)
print(sorted_words)  # Output: ['apple', 'banana', 'cherry', 'date']

# Reverse sorting
reverse_sorted = sorted(numbers, reverse=True)
print(reverse_sorted)  # Output: [9, 5, 4, 3, 2, 1, 1]

# Sorting with key function
words = ['apple', 'banana', 'cherry', 'date']
sorted_by_length = sorted(words, key=len)
print(sorted_by_length)  # Output: ['date', 'apple', 'banana', 'cherry']

# Sorting complex objects
students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob', 'grade': 92},
    {'name': 'Charlie', 'grade': 78}
]

# Sort by grade
sorted_students = sorted(students, key=lambda x: x['grade'])
print(sorted_students)
# Output: [{'name': 'Charlie', 'grade': 78}, {'name': 'Alice', 'grade': 85}, {'name': 'Bob', 'grade': 92}]
```

## 7. `any()` and `all()` Functions

### `any()`:
Returns True if any element of the iterable is true.

### `all()`:
Returns True if all elements of the iterable are true.

### Examples:
```python
# any() examples
numbers = [0, False, 1, 0]  # Contains at least one truthy value
print(any(numbers))  # Output: True

numbers = [0, False, '', []]  # All falsy values
print(any(numbers))  # Output: False

# Check if any number is even
numbers = [1, 3, 5, 7, 8]
print(any(x % 2 == 0 for x in numbers))  # Output: True

# all() examples
numbers = [1, 2, 3, 4]  # All truthy values
print(all(numbers))  # Output: True

numbers = [1, 2, 0, 4]  # Contains falsy value (0)
print(all(numbers))  # Output: False

# Check if all numbers are positive
numbers = [1, 2, 3, 4, 5]
print(all(x > 0 for x in numbers))  # Output: True

numbers = [1, 2, -3, 4, 5]
print(all(x > 0 for x in numbers))  # Output: False
```

## 8. `reversed()` Function

### Purpose:
Returns a reverse iterator.

### Syntax:
```python
reversed(sequence)
```

### Examples:
```python
# Reversing lists
numbers = [1, 2, 3, 4, 5]
reversed_numbers = list(reversed(numbers))
print(reversed_numbers)  # Output: [5, 4, 3, 2, 1]

# Reversing strings
text = "Hello"
reversed_text = ''.join(reversed(text))
print(reversed_text)  # Output: "olleH"

# Reversing tuples
my_tuple = (1, 2, 3, 4)
reversed_tuple = tuple(reversed(my_tuple))
print(reversed_tuple)  # Output: (4, 3, 2, 1)

# Using with for loop
for num in reversed(numbers):
    print(num, end=' ')  # Output: 5 4 3 2 1
```

## 9. `sum()`, `min()`, `max()` Functions

### Examples:
```python
numbers = [1, 2, 3, 4, 5]

# sum()
total = sum(numbers)
print(total)  # Output: 15

total_with_start = sum(numbers, 10)
print(total_with_start)  # Output: 25

# min() and max()
print(min(numbers))  # Output: 1
print(max(numbers))  # Output: 5

# With key function
words = ['apple', 'banana', 'cherry', 'date']
print(min(words, key=len))  # Output: 'date'
print(max(words, key=len))  # Output: 'banana'
```

## Practical Combinations and Real-world Examples

### Example 1: Data Processing Pipeline
```python
# Process student data
students = [
    {'name': 'Alice', 'scores': [85, 92, 78]},
    {'name': 'Bob', 'scores': [88, 79, 91]},
    {'name': 'Charlie', 'scores': [92, 95, 89]}
]

# Calculate average scores and filter top performers
def process_students(students):
    # Add average score to each student
    students_with_avg = map(lambda s: {
        'name': s['name'],
        'scores': s['scores'],
        'average': sum(s['scores']) / len(s['scores'])
    }, students)
    
    # Filter students with average > 85
    top_students = filter(lambda s: s['average'] > 85, students_with_avg)
    
    # Sort by average score (descending)
    sorted_students = sorted(top_students, key=lambda s: s['average'], reverse=True)
    
    return list(sorted_students)

result = process_students(students)
for student in result:
    print(f"{student['name']}: {student['average']:.2f}")
```

### Example 2: Text Processing
```python
text = "Python is an amazing programming language. Python is versatile and powerful."

# Process text
words = text.lower().replace('.', '').split()

# Word frequency using reduce-like approach (simulated)
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

# Most common words
common_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:3]
print("Most common words:", common_words)

# Filter words longer than 5 characters
long_words = list(filter(lambda word: len(word) > 5, words))
print("Long words:", long_words)
```

### Example 3: Matrix Operations
```python
# Transpose a matrix using zip
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed = list(zip(*matrix))
print("Original:", matrix)
print("Transposed:", transposed)

# Element-wise sum of matrices
matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]

result = [list(map(sum, zip(*rows))) for rows in zip(matrix1, matrix2)]
print("Matrix sum:", result)
```

## Performance Considerations

### Generator Expressions vs List Comprehensions
```python
import time

large_list = list(range(1000000))

# List comprehension (creates entire list in memory)
start = time.time()
squares_list = [x**2 for x in large_list]
end = time.time()
print(f"List comprehension: {end - start:.4f} seconds")

# Generator expression (lazy evaluation)
start = time.time()
squares_gen = (x**2 for x in large_list)
end = time.time()
print(f"Generator expression: {end - start:.4f} seconds")

# Using map (also lazy)
start = time.time()
squares_map = map(lambda x: x**2, large_list)
end = time.time()
print(f"Map function: {end - start:.4f} seconds")
```