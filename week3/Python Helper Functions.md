# Python Helper Functions: Map, Filter, Reduce, and More -

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

# Python Helper Functions: Map, Filter, Reduce, and More - Detailed Guide (Without Lambda Functions)

## 1. `map()` Function

### Purpose:
Applies a function to all items in an input list (or any iterable) and returns an iterator.

### Syntax:
```python
map(function, iterable, ...)
```

### Examples (Without Lambda):
```python
# Basic map example with regular functions
numbers = [1, 2, 3, 4, 5]

# Using regular function for squaring
def square(x):
    return x ** 2

squared = map(square, numbers)
print(list(squared))  # Output: [1, 4, 9, 16, 25]

# Using regular function for doubling
def double(x):
    return x * 2

doubled = map(double, numbers)
print(list(doubled))  # Output: [2, 4, 6, 8, 10]

# Map with multiple iterables using regular function
def add_numbers(x, y):
    return x + y

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(add_numbers, numbers1, numbers2)
print(list(result))  # Output: [5, 7, 9]

# Map with strings using built-in methods
names = ['alice', 'bob', 'charlie']
capitalized = map(str.capitalize, names)
print(list(capitalized))  # Output: ['Alice', 'Bob', 'Charlie']

# Map with built-in functions
strings = ['1', '2', '3']
numbers = map(int, strings)
print(list(numbers))  # Output: [1, 2, 3]

# Complex transformation with custom function
def process_person(name):
    return {
        'name': name.upper(),
        'length': len(name),
        'first_letter': name[0]
    }

people = ['alice', 'bob', 'charlie']
processed = map(process_person, people)
print(list(processed))
```

## 2. `filter()` Function

### Purpose:
Filters elements from an iterable based on a function that returns True or False.

### Syntax:
```python
filter(function, iterable)
```

### Examples (Without Lambda):
```python
# Basic filter example with regular functions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers with regular function
def is_even(x):
    return x % 2 == 0

even_numbers = filter(is_even, numbers)
print(list(even_numbers))  # Output: [2, 4, 6, 8, 10]

# Filter positive numbers
def is_positive(x):
    return x > 0

mixed_numbers = [-5, 2, -3, 8, -1, 10]
positive_numbers = filter(is_positive, mixed_numbers)
print(list(positive_numbers))  # Output: [2, 8, 10]

# Filter with None (removes falsy values)
data = [0, 1, False, True, '', 'hello', None, [], [1, 2]]
truthy_values = filter(None, data)
print(list(truthy_values))  # Output: [1, True, 'hello', [1, 2]]

# Filter strings by length with regular function
def is_long_word(word):
    return len(word) > 5

words = ['apple', 'banana', 'cherry', 'date', 'elderberry']
long_words = filter(is_long_word, words)
print(list(long_words))  # Output: ['banana', 'cherry', 'elderberry']

# Complex filtering with custom function
def is_valid_email(email):
    return '@' in email and '.' in email and len(email) > 5

emails = ['test@example.com', 'invalid', 'user@domain', 'another@test.org']
valid_emails = filter(is_valid_email, emails)
print(list(valid_emails))  # Output: ['test@example.com', 'another@test.org']
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

### Examples (Without Lambda):
```python
from functools import reduce

# Sum of all numbers with regular function
def add(x, y):
    return x + y

numbers = [1, 2, 3, 4, 5]
total = reduce(add, numbers)
print(total)  # Output: 15

# Product of all numbers
def multiply(x, y):
    return x * y

product = reduce(multiply, numbers)
print(product)  # Output: 120

# Find maximum number
def find_max(x, y):
    if x > y:
        return x
    return y

max_num = reduce(find_max, numbers)
print(max_num)  # Output: 5

# String concatenation
def concatenate(x, y):
    return x + y

words = ['Hello', ' ', 'World', '!']
sentence = reduce(concatenate, words)
print(sentence)  # Output: Hello World!

# With initial value
def add_with_initial(x, y):
    return x + y

numbers = [1, 2, 3]
result = reduce(add_with_initial, numbers, 10)
print(result)  # Output: 16 (10 + 1 + 2 + 3)

# Complex reduction - flatten nested lists
def flatten_list(result, current):
    if isinstance(current, list):
        return result + current
    return result + [current]

nested_data = [1, [2, 3], 4, [5, 6, 7]]
flattened = reduce(flatten_list, nested_data, [])
print(flattened)  # Output: [1, 2, 3, 4, 5, 6, 7]
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

# Processing zipped data with regular functions
def create_person_info(data):
    name, age, city = data
    return f"{name} is {age} years old and lives in {city}"

people_data = zip(names, ages, cities)
person_descriptions = map(create_person_info, people_data)
print(list(person_descriptions))
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

# Using enumerate with custom processing function
def process_with_index(index, value):
    return f"Item {index}: {value} (length: {len(value)})"

fruits = ['apple', 'banana', 'cherry']
processed_fruits = [process_with_index(i, f) for i, f in enumerate(fruits)]
print(processed_fruits)
```

## 6. `sorted()` Function

### Purpose:
Returns a new sorted list from the items in iterable.

### Syntax:
```python
sorted(iterable, key=None, reverse=False)
```

### Examples (Without Lambda):
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

# Sorting with key function (using regular functions instead of lambda)
def get_length(word):
    return len(word)

words = ['apple', 'banana', 'cherry', 'date']
sorted_by_length = sorted(words, key=get_length)
print(sorted_by_length)  # Output: ['date', 'apple', 'banana', 'cherry']

# Sorting complex objects with custom key functions
def get_grade(student):
    return student['grade']

def get_name(student):
    return student['name']

students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob', 'grade': 92},
    {'name': 'Charlie', 'grade': 78}
]

# Sort by grade
sorted_by_grade = sorted(students, key=get_grade)
print("Sorted by grade:", sorted_by_grade)

# Sort by name
sorted_by_name = sorted(students, key=get_name)
print("Sorted by name:", sorted_by_name)

# Complex sorting with multiple criteria
def sort_by_grade_then_name(student):
    return (-student['grade'], student['name'])  # Negative for descending grade

complex_sorted = sorted(students, key=sort_by_grade_then_name)
print("Complex sort:", complex_sorted)
```

## 7. `any()` and `all()` Functions

### `any()`:
Returns True if any element of the iterable is true.

### `all()`:
Returns True if all elements of the iterable are true.

### Examples (Without Lambda):
```python
# any() examples with generator expressions
numbers = [0, False, 1, 0]  # Contains at least one truthy value
print(any(numbers))  # Output: True

numbers = [0, False, '', []]  # All falsy values
print(any(numbers))  # Output: False

# Check if any number is even using custom function
def is_even(x):
    return x % 2 == 0

numbers = [1, 3, 5, 7, 8]
print(any(is_even(x) for x in numbers))  # Output: True

# all() examples
numbers = [1, 2, 3, 4]  # All truthy values
print(all(numbers))  # Output: True

numbers = [1, 2, 0, 4]  # Contains falsy value (0)
print(all(numbers))  # Output: False

# Check if all numbers are positive using custom function
def is_positive(x):
    return x > 0

numbers = [1, 2, 3, 4, 5]
print(all(is_positive(x) for x in numbers))  # Output: True

numbers = [1, 2, -3, 4, 5]
print(all(is_positive(x) for x in numbers))  # Output: False

# Complex validation with custom functions
def is_valid_email(email):
    return '@' in email and '.' in email and len(email) > 5

emails = ['test@example.com', 'user@domain.org']
print(all(is_valid_email(email) for email in emails))  # Output: True

emails = ['test@example.com', 'invalid']
print(all(is_valid_email(email) for email in emails))  # Output: False
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

# Processing reversed data with custom functions
def process_reversed_data(data):
    reversed_data = list(reversed(data))
    result = []
    for i, item in enumerate(reversed_data):
        result.append(f"Position {i}: {item}")
    return result

numbers = [10, 20, 30, 40]
processed = process_reversed_data(numbers)
print(processed)  # Output: ['Position 0: 40', 'Position 1: 30', 'Position 2: 20', 'Position 3: 10']
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

# With key function (using regular functions instead of lambda)
def get_length(word):
    return len(word)

words = ['apple', 'banana', 'cherry', 'date']
print(min(words, key=get_length))  # Output: 'date'
print(max(words, key=get_length))  # Output: 'banana'

# Complex objects with custom key functions
def get_price(product):
    return product['price']

products = [
    {'name': 'apple', 'price': 1.5},
    {'name': 'banana', 'price': 0.5},
    {'name': 'cherry', 'price': 3.0}
]

cheapest = min(products, key=get_price)
most_expensive = max(products, key=get_price)
print(f"Cheapest: {cheapest['name']} at ${cheapest['price']}")
print(f"Most expensive: {most_expensive['name']} at ${most_expensive['price']}")
```

## Practical Combinations and Real-world Examples (Without Lambda)

### Example 1: Data Processing Pipeline
```python
# Process student data with regular functions
students = [
    {'name': 'Alice', 'scores': [85, 92, 78]},
    {'name': 'Bob', 'scores': [88, 79, 91]},
    {'name': 'Charlie', 'scores': [92, 95, 89]}
]

def calculate_average(scores):
    return sum(scores) / len(scores)

def add_average_score(student):
    return {
        'name': student['name'],
        'scores': student['scores'],
        'average': calculate_average(student['scores'])
    }

def is_top_performer(student):
    return student['average'] > 85

def get_average_score(student):
    return student['average']

def process_students(students):
    # Add average score to each student
    students_with_avg = map(add_average_score, students)
    
    # Filter students with average > 85
    top_students = filter(is_top_performer, students_with_avg)
    
    # Sort by average score (descending)
    sorted_students = sorted(top_students, key=get_average_score, reverse=True)
    
    return list(sorted_students)

result = process_students(students)
for student in result:
    print(f"{student['name']}: {student['average']:.2f}")
```

### Example 2: Text Processing
```python
text = "Python is an amazing programming language. Python is versatile and powerful."

def clean_word(word):
    return word.lower().strip('.,!?;')

def is_long_word(word):
    return len(word) > 5

def get_word_length(word):
    return len(word)

# Process text
words = text.split()
cleaned_words = map(clean_word, words)

# Filter words longer than 5 characters
long_words = list(filter(is_long_word, cleaned_words))
print("Long words:", long_words)

# Word frequency using regular functions
def count_words(word_count, word):
    word_count[word] = word_count.get(word, 0) + 1
    return word_count

from functools import reduce
word_count = reduce(count_words, words, {})

# Most common words
def get_count(item):
    return item[1]

common_words = sorted(word_count.items(), key=get_count, reverse=True)[:3]
print("Most common words:", common_words)
```

### Example 3: Matrix Operations
```python
# Transpose a matrix using zip
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def transpose_matrix(matrix):
    return list(zip(*matrix))

transposed = transpose_matrix(matrix)
print("Original:", matrix)
print("Transposed:", transposed)

# Element-wise sum of matrices
def sum_rows(rows):
    row1, row2 = rows
    return [sum(pair) for pair in zip(row1, row2)]

matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]

result = list(map(sum_rows, zip(matrix1, matrix2)))
print("Matrix sum:", result)
```

### Example 4: Inventory Management System
```python
# Inventory management using helper functions
inventory = [
    {'name': 'laptop', 'category': 'electronics', 'price': 999, 'stock': 5},
    {'name': 'book', 'category': 'education', 'price': 25, 'stock': 100},
    {'name': 'phone', 'category': 'electronics', 'price': 699, 'stock': 15},
    {'name': 'pen', 'category': 'office', 'price': 2, 'stock': 200}
]

def is_electronics(item):
    return item['category'] == 'electronics'

def get_price(item):
    return item['price']

def get_stock_value(item):
    return item['price'] * item['stock']

def format_inventory_item(item):
    return f"{item['name']}: ${item['price']} (Stock: {item['stock']})"

# Filter electronics items
electronics = list(filter(is_electronics, inventory))
print("Electronics items:")
for item in map(format_inventory_item, electronics):
    print("-", item)

# Sort by price
sorted_by_price = sorted(inventory, key=get_price, reverse=True)
print("\nItems sorted by price (high to low):")
for item in map(format_inventory_item, sorted_by_price):
    print("-", item)

# Calculate total inventory value
def add_values(total, item):
    return total + get_stock_value(item)

total_value = reduce(add_values, inventory, 0)
print(f"\nTotal inventory value: ${total_value}")

# Get items with low stock (less than 20)
def is_low_stock(item):
    return item['stock'] < 20

low_stock_items = list(filter(is_low_stock, inventory))
print("\nLow stock items:")
for item in map(format_inventory_item, low_stock_items):
    print("-", item)
```

## Key Benefits of Using Regular Functions Instead of Lambda:

1. **Better Readability**: Named functions are more descriptive
2. **Reusability**: Functions can be reused elsewhere in code
3. **Better Error Messages**: Named functions provide clearer tracebacks
4. **Testability**: Individual functions can be unit tested
5. **Documentation**: Functions can have docstrings
6. **Debugging**: Easier to debug named functions

This approach makes your code more maintainable and professional, especially in larger projects.