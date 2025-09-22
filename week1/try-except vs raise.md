# Difference Between `try-except` and `raise`

## 🎯 Simple Analogy

- **`raise`** = **Throwing** a ball (creating an error)
- **`try-except`** = **Catching** a ball (handling an error)

---

## `raise` - Creating Errors

### What it does:
**Creates and throws an error** to stop the program

```python
# Example: Creating an error
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")  # THROW error
    return age

# This will STOP the program with an error
check_age(-5)  # 💥 ValueError: Age cannot be negative!
```

### When to use `raise`:
- When you want to **create** an error
- When something is wrong and you want to **stop** execution
- To enforce rules in your code

---

## `try-except` - Handling Errors

### What it does:
**Catches and handles errors** so the program can continue

```python
# Example: Handling an error
try:
    age = check_age(-5)  # This would cause error
except ValueError as e:  # CATCH error
    print(f"Oops! {e}")  # Handle it gracefully
    age = 0  # Set default value

print(f"Age: {age}")  # Program continues!
# Output: "Oops! Age cannot be negative!" then "Age: 0"
```

### When to use `try-except`:
- When you want to **handle** errors gracefully
- To prevent your program from crashing
- When you expect something might fail

---

## Key Differences

| | `raise` | `try-except` |
| :--- | :--- | :--- |
| **Purpose** | Create errors | Handle errors |
| **Effect** | Stops execution | Prevents crashing |
| **Action** | Throw/Generate error | Catch/Process error |
| **Use Case** | "This is wrong!" | "If something goes wrong..." |

---

## How They Work Together

```python
def transfer_money(amount):
    if amount <= 0:
        raise ValueError("Amount must be positive!")  # THROW error
    # Process transfer...

# Later in code:
try:
    transfer_money(-100)  # This will cause error
except ValueError as e:  # CATCH error
    print(f"Transfer failed: {e}")  # Handle gracefully
    # Maybe ask user to enter amount again
```

### Flow:
1. `raise` creates the error → **"I'm throwing a problem!"**
2. `try-except` catches it → **"I'll handle this problem!"**

---

## Real-World Examples

### Example 1: `raise` (Creating Error)
```python
def set_temperature(temp):
    if temp < -273.15:  # Absolute zero
        raise ValueError("Temperature cannot be below absolute zero!")
    # Set temperature...
```

### Example 2: `try-except` (Handling Error)
```python
try:
    set_temperature(-300)  # This will cause error
except ValueError as e:
    print(f"Error: {e}")
    # Maybe set to minimum allowed temperature
```

### Example 3: Both Together
```python
def calculate_square_root(number):
    if number < 0:
        raise ValueError("Cannot calculate square root of negative number!")
    return number ** 0.5

# Usage:
try:
    result = calculate_square_root(-9)
except ValueError as e:
    print(f"Math error: {e}")
    result = 0  # Default value
```

---

## Quick Guide

### Use `raise` when:
- You need to **enforce rules** in your code
- Something is **fundamentally wrong**
- You want to **stop execution** with a clear error message

### Use `try-except` when:
- You want to **prevent crashes**
- You need to **handle errors gracefully**
- You're doing something that **might fail** (file operations, user input, etc.)

---

## Remember This:
- **`raise`** = **R**aise = **R**eport a problem! 🚨
- **`try-except`** = **T**ry = **T**rap errors! 🕸️

They work together to make your code robust and user-friendly! 🚀