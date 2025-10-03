# Python Data Types: Mutable vs Immutable

## Overview

In Python, data types are classified as either **mutable** or **immutable** based on whether their values can be changed after creation.

- **Mutable**: Can be modified after creation
- **Immutable**: Cannot be modified after creation

## Immutable Data Types

### 1. Integers
```python
# Integers are immutable
x = 10
print(f"Original x: {x}, id: {id(x)}")

x = 20  # This creates a new object, doesn't modify the original
print(f"New x: {x}, id: {id(x)}")  # Different ID

# Proof of immutability
a = 5
b = 5
print(f"a id: {id(a)}, b id: {id(b)}")  # Same ID due to interning
print(f"a is b: {a is b}")  # True
```

### 2. Floats
```python
# Floats are immutable
pi = 3.14
print(f"Original pi: {pi}, id: {id(pi)}")

pi = 3.14159  # Creates new object
print(f"New pi: {pi}, id: {id(pi)}")  # Different ID
```

### 3. Strings
```python
# Strings are immutable
name = "Alice"
print(f"Original name: {name}, id: {id(name)}")

# This creates a new string
name = name + " Smith"
print(f"New name: {name}, id: {id(name)}")  # Different ID

# String methods return new strings
text = "hello"
upper_text = text.upper()
print(f"text: {text}, id: {id(text)}")
print(f"upper_text: {upper_text}, id: {id(upper_text)}")  # Different ID

# This would cause an error:
# text[0] = 'H'  # TypeError: 'str' object does not support item assignment
```

### 4. Tuples
```python
# Tuples are immutable
coordinates = (10, 20)
print(f"Original coordinates: {coordinates}, id: {id(coordinates)}")

# This creates a new tuple
coordinates = (10, 30)
print(f"New coordinates: {coordinates}, id: {id(coordinates)}")  # Different ID

# This would cause an error:
# coordinates[0] = 15  # TypeError: 'tuple' object does not support item assignment

# However, tuples can contain mutable objects
mixed_tuple = ([1, 2], [3, 4])
print(f"Mixed tuple: {mixed_tuple}")
mixed_tuple[0].append(3)  # This works!
print(f"Modified mixed tuple: {mixed_tuple}")
```

### 5. Booleans
```python
# Booleans are immutable
flag = True
print(f"Original flag: {flag}, id: {id(flag)}")

flag = False  # Creates new object
print(f"New flag: {flag}, id: {id(flag)}")  # Different ID
```

### 6. Frozensets
```python
# Frozensets are immutable versions of sets
frozen_set = frozenset([1, 2, 3, 4])
print(f"Frozen set: {frozen_set}")

# This would cause an error:
# frozen_set.add(5)  # AttributeError: 'frozenset' object has no attribute 'add'
```

## Mutable Data Types

### 1. Lists
```python
# Lists are mutable
numbers = [1, 2, 3]
print(f"Original numbers: {numbers}, id: {id(numbers)}")

# Modify in place
numbers.append(4)
numbers[0] = 10
print(f"Modified numbers: {numbers}, id: {id(numbers)}")  # Same ID!

# Slicing creates new lists
new_numbers = numbers[:]
print(f"new_numbers id: {id(new_numbers)}")  # Different ID
```

### 2. Dictionaries
```python
# Dictionaries are mutable
person = {"name": "Alice", "age": 25}
print(f"Original person: {person}, id: {id(person)}")

# Modify in place
person["age"] = 26
person["city"] = "New York"
print(f"Modified person: {person}, id: {id(person)}")  # Same ID!

# Delete items
del person["city"]
print(f"After deletion: {person}, id: {id(person)}")  # Still same ID
```

### 3. Sets
```python
# Sets are mutable
unique_numbers = {1, 2, 3}
print(f"Original set: {unique_numbers}, id: {id(unique_numbers)}")

# Modify in place
unique_numbers.add(4)
unique_numbers.remove(2)
print(f"Modified set: {unique_numbers}, id: {id(unique_numbers)}")  # Same ID!
```

### 4. Bytearrays
```python
# Bytearrays are mutable
data = bytearray(b'hello')
print(f"Original data: {data}, id: {id(data)}")

# Modify in place
data[0] = 72  # Change 'h' to 'H'
print(f"Modified data: {data}, id: {id(data)}")  # Same ID!
```

## Key Differences and Implications

### 1. Assignment Behavior
```python
# Immutable - creates copies automatically
a = 10
b = a  # Both point to same object
print(f"a is b: {a is b}")  # True

b = 20  # b now points to different object
print(f"a: {a}, b: {b}")  # a unchanged

# Mutable - both variables reference same object
list1 = [1, 2, 3]
list2 = list1  # Both reference same list
print(f"list1 is list2: {list1 is list2}")  # True

list2.append(4)  # Modifies the shared list
print(f"list1: {list1}")  # [1, 2, 3, 4] - also changed!
print(f"list2: {list2}")  # [1, 2, 3, 4]
```

### 2. Function Arguments
```python
def modify_immutable(x):
    x = x + 10  # Creates new object
    return x

def modify_mutable(lst):
    lst.append(100)  # Modifies original object

# With immutable
num = 5
result = modify_immutable(num)
print(f"num: {num}")  # 5 - unchanged
print(f"result: {result}")  # 15

# With mutable
my_list = [1, 2, 3]
modify_mutable(my_list)
print(f"my_list: {my_list}")  # [1, 2, 3, 100] - modified!
```

### 3. Copying Objects
```python
import copy

# Shallow vs Deep Copy with mutable objects
original = [[1, 2], [3, 4]]

# Shallow copy
shallow = copy.copy(original)
shallow[0].append(5)  # Affects both!
print(f"Original: {original}")  # [[1, 2, 5], [3, 4]]
print(f"Shallow: {shallow}")    # [[1, 2, 5], [3, 4]]

# Deep copy
original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)
deep[0].append(5)  # Only affects deep copy
print(f"Original: {original}")  # [[1, 2], [3, 4]]
print(f"Deep: {deep}")          # [[1, 2, 5], [3, 4]]
```

## Practical Examples

### 1. Caching with Immutable Keys
```python
# Dictionaries can use immutable types as keys
cache = {}

def expensive_operation(x, y):
    key = (x, y)  # Tuple (immutable) as key
    if key not in cache:
        # Simulate expensive computation
        result = x * y + x + y
        cache[key] = result
    return cache[key]

print(expensive_operation(3, 4))  # Computed
print(expensive_operation(3, 4))  # From cache
```

### 2. Default Arguments Pitfall
```python
# Common mistake with mutable default arguments
def bad_append(item, lst=[]):  # Default list created once!
    lst.append(item)
    return lst

print(bad_append(1))  # [1]
print(bad_append(2))  # [1, 2] - unexpected!

# Correct approach
def good_append(item, lst=None):
    if lst is None:
        lst = []  # New list each time
    lst.append(item)
    return lst

print(good_append(1))  # [1]
print(good_append(2))  # [2] - as expected
```

## Summary Table

| Data Type | Mutable | Example |
|-----------|---------|---------|
| int | ❌ Immutable | `x = 5` |
| float | ❌ Immutable | `y = 3.14` |
| str | ❌ Immutable | `s = "hello"` |
| tuple | ❌ Immutable | `t = (1, 2)` |
| bool | ❌ Immutable | `flag = True` |
| frozenset | ❌ Immutable | `fs = frozenset([1,2,3])` |
| list | ✅ Mutable | `lst = [1, 2, 3]` |
| dict | ✅ Mutable | `d = {"a": 1}` |
| set | ✅ Mutable | `s = {1, 2, 3}` |
| bytearray | ✅ Mutable | `ba = bytearray(b'data')` |

## Key Takeaways

1. **Immutable objects** are safer in concurrent programming and can be used as dictionary keys
2. **Mutable objects** are more memory efficient for frequent modifications
3. Understanding mutability helps avoid bugs with shared references
4. Always be careful with default mutable arguments in functions
5. Use appropriate copying techniques (`copy()`, `deepcopy()`) when needed
