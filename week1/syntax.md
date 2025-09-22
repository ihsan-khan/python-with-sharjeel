### Python syntax

Understanding the rules and structures that define how you write valid Python code. Python is famous for its clean, readable syntax, often described as "executable pseudocode."

### The Golden Rule: Whitespace and Indentation

This is the most defining feature of Python syntax. Unlike most languages that use braces `{}` to define code blocks, Python uses **indentation**.

*   **What it means:** The amount of whitespace (spaces or tabs) at the beginning of a line defines its grouping.
*   **The standard:** **4 spaces** per indentation level is the standard defined in PEP 8 (Python's style guide). Never mix tabs and spaces.
*   **Consequences:** Improper indentation will cause an `IndentationError`.

**Example:**
```python
# Correct Indentation
if True:
    print("Hello")     # This is inside the if-block
    print("World")     # This is also inside the if-block
print("The End")       # This is outside the if-block

# Incorrect Indentation (Will cause an error)
if True:
print("Hello")   # IndentationError: expected an indented block
```

---

### 1. Comments

Comments are for developers and are ignored by the Python interpreter.

*   **Single-line:** Start with a `#`
    ```python
    # This is a comment
    result = 10 + 5  # This is an inline comment
    ```
*   **Multi-line (Docstrings):** Use triple quotes `"""` or `'''`. While not technically comments, they are used to document modules, functions, classes, and methods. They are stored as the object's `__doc__` attribute.
    ```python
    def my_function():
        """
        This is a docstring.
        It explains what this function does.
        """
        return None
    ```

---

### 2. Variables and Assignment

*   **Assignment:** Use the equals sign `=`.
    ```python
    name = "Alice"  # Assign the string "Alice" to the variable 'name'
    ```
*   **Dynamic Typing:** No need to declare a variable's type.
    ```python
    x = 10    # x is an integer
    x = "hi"  # Now x is a string
    ```
*   **Multiple Assignment:**
    ```python
    a, b, c = 1, 2, 3      # Assign 1 to a, 2 to b, 3 to c
    x = y = z = 0          # Assign 0 to all three variables
    ```

---

### 3. Basic Data Types and Literals

| Type | Example Literals | Notes |
| :--- | :--- | :--- |
| **Integer (`int`)** | `42`, `-10`, `0` | Whole numbers. |
| **Float (`float`)** | `3.14`, `-0.5`, `2.0` | Numbers with a decimal point. |
| **String (`str`)** | `'hello'`, `"world"`, `"""multi-line"""` | Text. Can use single or double quotes. |
| **Boolean (`bool`)** | `True`, `False` | Must be capitalized. |
| **NoneType** | `None` | Represents the absence of a value. |

---

### 4. Operators

*   **Arithmetic:** `+` (addition), `-` (subtraction), `*` (multiplication), `/` (division), `//` (floor division), `%` (modulo), `**` (exponentiation)
*   **Comparison:** `==` (equal), `!=` (not equal), `>` (greater than), `<` (less than), `>=` (greater than or equal), `<=` (less than or equal)
*   **Logical:** `and`, `or`, `not`
*   **Assignment:** `=`, `+=`, `-=`, `*=`, `/=`, etc. (`x += 1` is shorthand for `x = x + 1`)
*   **Identity:** `is`, `is not` (checks if two variables point to the same object in memory)
*   **Membership:** `in`, `not in` (checks if a value is present in a sequence like a list or string)

---

### 5. Control Flow Statements

#### `if`, `elif`, `else`
```python
age = 20
if age < 18:
    print("Minor")
elif age >= 18 and age < 65:
    print("Adult")
else:
    print("Senior")
# Output: Adult
```

#### `for` loop
Used for iterating over sequences (lists, tuples, strings, dictionaries, etc.).
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:  # fruit is the loop variable
    print(f"I like {fruit}")

# Iterating a number of times with range()
for i in range(5): # i will be 0, 1, 2, 3, 4
    print(i)
```

#### `while` loop
Repeats as long as a condition is `True`.
```python
count = 5
while count > 0:
    print(count)
    count -= 1  # Decrement count. Crucial to avoid an infinite loop!
print("Blastoff!")
```

#### `break`, `continue`, `pass`
*   `break`: Exit the loop immediately.
*   `continue`: Skip the rest of the current iteration and move to the next one.
*   `pass`: A null operation; a placeholder for when syntax requires a statement but you don't want to do anything.
```python
for num in range(10):
    if num == 2:
        continue  # Skip printing 2
    if num == 7:
        break     # Stop the loop entirely at 7
    print(num)
else:
    # The else clause runs only if the loop did NOT break
    print("Loop completed normally!")
```

---

### 6. Function Definition (`def`)

Functions are defined using the `def` keyword.
```python
def greet(name, greeting="Hello"): # 'greeting' has a default value
    """This function greets a person."""
    return f"{greeting}, {name}!"

# Calling the function
message = greet("Alice", "Hi")
print(message) # Output: Hi, Alice!

# Calling with keyword arguments (order doesn't matter)
message = greet(greeting="Hey", name="Bob")
```

---

### 7. Compound Data Structures

#### List (`list`)
```python
my_list = [1, 2, "three", 4.0]  # Ordered, mutable (changeable) sequence
my_list.append(5)    # Add an item to the end
print(my_list[2])    # Access by index: Output "three"
```

#### Tuple (`tuple`)
```python
my_tuple = (1, 2, "three") # Ordered, immutable (unchangeable) sequence
# my_tuple[0] = 10        # This would cause a TypeError
```

#### Dictionary (`dict`)
```python
my_dict = {"name": "Alice", "age": 30} # Unordered collection of key-value pairs
print(my_dict["name"])                  # Access value by key: Output "Alice"
my_dict["job"] = "Developer"           # Add a new key-value pair
```

#### Set (`set`)
```python
my_set = {"apple", "banana", "cherry"} # Unordered collection of unique items
my_set.add("apple")  # Won't add a duplicate
print(my_set)        # Output: {'apple', 'banana', 'cherry'} (order may vary)
```

---

### 8. Error Handling (`try`, `except`)

```python
try:
    numerator = 10
    denominator = 0
    result = numerator / denominator  # This will cause a ZeroDivisionError
except ZeroDivisionError:
    print("Error: You can't divide by zero!")
except Exception as e: # Catch any other exception
    print(f"An unexpected error occurred: {e}")
else:
    print("This runs only if no exception was raised.")
finally:
    print("This 'cleanup' code always runs, no matter what.")
```

---

### 9. Importing Modules (`import`)

To use code from other files or built-in libraries.
```python
import math                         # Import the whole module
print(math.sqrt(16))                # Use its functions with dot notation

from datetime import datetime       # Import a specific thing from a module
now = datetime.now()                # Use it directly without dot notation

import json as js                   # Import a module with an alias
data = js.loads('{"key": "value"}')

from collections import *           # Import everything (generally discouraged)
```

### 10. The `class` Syntax (Object-Oriented Programming)

```python
class Dog:  # Define a class
    # Class Attribute (shared by all instances)
    species = "Canis familiaris"

    # The initializer (constructor) method
    def __init__(self, name, age):
        # Instance Attributes (unique to each instance)
        self.name = name
        self.age = age

    # Instance Method
    def bark(self):
        return f"{self.name} says woof!"

# Creating an instance of the Dog class
my_dog = Dog("Rex", 5)
print(my_dog.bark())  # Output: Rex says woof!
```

### Key Principles of Python Syntax

1.  **Readability Counts:** The syntax is designed to be clear and English-like.
2.  **Explicit is Better than Implicit:** Code should be obvious and not rely on hidden tricks.
3.  **Simple is Better than Complex:** The most straightforward way to do something is usually the right one.

This covers the vast majority of Python syntax you will encounter daily. The best way to learn it is to write code and see how the interpreter responds to it.