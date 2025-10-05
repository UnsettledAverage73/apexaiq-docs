# Conditional Statements

Conditional statements in Python allow you to execute different blocks of code based on whether a condition is true or false. The primary conditional statements are `if`, `elif` (else if), and `else`.

## The `if` Statement

The `if` statement is used to test a condition. If the condition is true, the indented block of code following the `if` statement is executed.

### Syntax

```python
if condition:
    # code to execute if condition is true
    statement1
    statement2
```

### Example

```python
x = 10

if x > 5:
    print("x is greater than 5")
```

## The `else` Statement

The `else` statement is used to define a block of code that will be executed if the `if` condition is false.

### Syntax

```python
if condition:
    # code to execute if condition is true
    statement1
else:
    # code to execute if condition is false
    statement2
```

### Example

```python
x = 3

if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")
```

## The `elif` Statement

The `elif` (short for "else if") statement allows you to check multiple conditions sequentially. If the `if` condition is false, Python checks the `elif` condition, and so on. The first `elif` condition that evaluates to true will have its code block executed.

### Syntax

```python
if condition1:
    # code to execute if condition1 is true
    statement1
elif condition2:
    # code to execute if condition1 is false AND condition2 is true
    statement2
else:
    # code to execute if all previous conditions are false
    statement3
```

### Example

```python
{/*
score = 75

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")
*/}
```

## Nested `if` Statements

You can also have `if` statements inside other `if` statements, which is called nesting.

### Example

```python
y = 15

if y > 10:
    print("y is above 10")
    if y > 20:
        print("y is also above 20")
    else:
        print("y is not above 20")
else:
    print("y is 10 or less")
```
