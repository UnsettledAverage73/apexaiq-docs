# Python Basics

# What is Python 

Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python’s elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms.

The Python interpreter is easily extended with new functions and data types implemented in C or C++ (or other languages callable from C). 

Python is also suitable as an extension language for customizable applications.


## Syntax

Python's syntax is designed to be readable and straightforward. It uses indentation to define code blocks, unlike other languages that might use curly braces.

### Indentation

Indentation is crucial in Python. A consistent level of indentation (usually 4 spaces) indicates a block of code.

```python
if True:
    print("This code is inside the if block.")
    print("This is also part of the if block.")
else:
    print("This code is inside the else block.")
```

### Comments

Comments are used to explain code and are ignored by the Python interpreter.

```python
# This is a single-line comment

x = 10  # This comment explains the purpose of x

"""
This is a multi-line comment (docstring).
It can span multiple lines.
"""
```

## Variables

Variables are used to store data values. Python is dynamically typed, meaning you don't need to declare the variable type explicitly.

### Declaring Variables

```python
name = "Alice"
age = 30
is_student = True
```

### Variable Naming Rules

*   Must start with a letter or an underscore.
*   Cannot start with a number.
*   Can only contain alpha-numeric characters and underscores (A-z, 0-9, and _).
*   Variable names are case-sensitive (age, Age, and AGE are three different variables).

## Datatypes

Python has several built-in data types:

### 1. Integers (`int`)

Whole numbers, positive or negative, without decimals.

```python
x = 10
y = -5
```

### 2. Floating-Point Numbers (`float`)

Numbers with a decimal point, positive or negative.

```python
price = 19.99
temperature = -3.5
```

### 3. Strings (`str`)

Sequences of characters, enclosed in single or double quotes.

```python
message = "Hello, World!"
char = 'A'
```

### 4. Lists (`list`)

Ordered, changeable, and allow duplicate members. Enclosed in square brackets.

```python
my_list = [1, 2, "three", 4.0]
```

### 5. Tuples (`tuple`)

Ordered, unchangeable, and allow duplicate members. Enclosed in parentheses.

```python
my_tuple = (1, 2, "three", 4.0)
```

### 6. Dictionaries (`dict`)

Unordered, changeable, and indexed. Stored as key-value pairs. Enclosed in curly braces.

```python
my_dict = {
    "name": "Bob",
    "age": 25,
    "city": "New York"
}
```

### 7. Sets (`set`)

Unordered, unchangeable (but you can add/remove items), and do not allow duplicate members. Enclosed in curly braces.

```python
my_set = {1, 2, 3, 3, 4}  # Will be {1, 2, 3, 4}
```
