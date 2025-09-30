# Dictionary vs JSON - Structural Differences

## 🎯 **Main Structural Differences:**

### 1. **QUOTES:**
```python
# Dictionary - Can use single OR double quotes
person_dict = {
    'name': 'Alice',     # ✅ Single quotes work
    "age": 25,           # ✅ Double quotes work
    'city': "London"     # ✅ Mix them if you want
}

# JSON - MUST use DOUBLE quotes only
person_json = '''
{
    "name": "Alice",     # ✅ Double quotes ONLY
    "age": 25,           # ✅ Double quotes ONLY
    "city": "London"     # ✅ Double quotes ONLY
}
'''
# 'name': 'Alice'        # ❌ Single quotes don't work in JSON
```

### 2. **BOOLEANS:**
```python
# Dictionary - Python booleans
person_dict = {
    "is_student": True,    # ✅ Capital T (Python)
    "is_employed": False   # ✅ Capital F (Python)
}

# JSON - Lowercase booleans  
person_json = '''
{
    "is_student": true,    # ✅ lowercase true (JSON)
    "is_employed": false   # ✅ lowercase false (JSON)
}
'''
```

### 3. **NULL/NONE:**
```python
# Dictionary - Python's None
person_dict = {
    "middle_name": None,    # ✅ None (Python)
    "nickname": None
}

# JSON - null
person_json = '''
{
    "middle_name": null,    # ✅ null (JSON)
    "nickname": null
}
'''
```

### 4. **TRAILING COMMAS:**
```python
# Dictionary - Trailing comma OK
person_dict = {
    "name": "Alice",
    "age": 25,           # ✅ Extra comma allowed
}

# JSON - No trailing commas
person_json = '''
{
    "name": "Alice",
    "age": 25            # ❌ No comma after last item
}
'''
```

---

## 📋 **Quick Structure Comparison Table:**

| Feature | Dictionary | JSON |
|---------|------------|------|
| **Quotes** | Single or Double | Double ONLY |
| **True/False** | `True`, `False` | `true`, `false` |
| **None** | `None` | `null` |
| **Trailing Comma** | Allowed | Not allowed |
| **Comments** | No comments | No comments |
| **Type** | Python `dict` | String |

---

## 🔍 **Visual Examples:**

### **Dictionary Structure:**
```python
# ✅ VALID Dictionary
person_dict = {
    'name': "Alice",
    'age': 25,
    'is_student': True,
    'pets': None,
}  # ← Extra comma OK!
```

### **JSON Structure:**
```python
# ✅ VALID JSON
person_json = '''{
    "name": "Alice",
    "age": 25,
    "is_student": true,
    "pets": null
}'''  # ← No extra comma!
```

### **❌ INVALID JSON (but valid dictionary):**
```python
invalid_json = '''{
    'name': 'Alice',      # ❌ Single quotes
    "age": 25,
    "is_student": True,   # ❌ Capital True
    "pets": None,         # ❌ None instead of null
}'''                      # ❌ Extra comma
```

---

## 🎯 **Key Structural Rule:**

**Dictionary** = **Python rules**  
**JSON** = **JavaScript rules** (but everyone uses it)

Remember: **JSON is more strict!** 🔒