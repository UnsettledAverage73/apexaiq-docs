# Loops

Loops are fundamental programming constructs that allow you to execute a block of code repeatedly. Python provides two main types of loops: `for` loops (for iterating over sequences) and `while` loops (for repeating as long as a condition is true).

## 1. `for` Loop

The `for` loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

### Syntax

```python
for item in iterable:
    # code to execute for each item
    statement1
    statement2
```

### Example 1: Iterating over a List

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

**Output:**
```
apple
banana
cherry
```

### Example 2: Iterating with `range()`

The `range()` function is often used to loop a specific number of times.

```python
for i in range(5): # Iterates from 0 to 4
    print(i)
```

**Output:**
```
0
1
2
3
4
```

### Example 3: `for` Loop with `else`

The `else` block in a `for` loop is executed when the loop finishes normally (i.e., not terminated by a `break` statement).

```python
for i in range(3):
    print(i)
else:
    print("Loop finished successfully!")
```

**Output:**
```
0
1
2
Loop finished successfully!
```

## 2. `while` Loop

The `while` loop executes a block of code as long as a specified condition is true.

### Syntax

```python
while condition:
    # code to execute as long as condition is true
    statement1
    statement2
```

### Example 1: Basic `while` Loop

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

**Output:**
```
0
1
2
3
4
```

### Example 2: `while` Loop with `else`

Similar to `for` loops, `while` loops can also have an `else` block that executes when the condition becomes false.

```python
i = 0
while i < 3:
    print(i)
    i += 1
else:
    print("Condition is now false, loop ended.")
```

**Output:**
```
0
1
2
Condition is now false, loop ended.
```

## 3. Loop Control Statements

### a. `break` Statement

The `break` statement is used to exit a loop prematurely.

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

**Output:**
```
0
1
2
3
4
```

### b. `continue` Statement

The `continue` statement skips the rest of the current iteration of the loop and moves to the next iteration.

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

**Output:**
```
0
1
3
4
```

### c. `pass` Statement

The `pass` statement is a null operation; nothing happens when it executes. It can be used as a placeholder where a statement is syntactically required but you don't want any command or code to execute.

```python
for i in range(3):
    if i == 1:
        pass # Do nothing when i is 1
    print(i)
```

**Output:**
```
0
1
2
```