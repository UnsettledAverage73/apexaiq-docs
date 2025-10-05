# Loops

Loops are fundamental programming constructs that allow you to execute a block of code repeatedly. Python provides `for` loops for iterating over sequences and `while` loops for repeating as long as a condition is true. Additionally, `break` and `continue` statements offer control over loop execution.

## The `for` Loop

The `for` loop is used for iterating over a sequence (that is, a list, tuple, dictionary, set, or string) or other iterable objects. It executes a block of code for each item in the sequence.

### Syntax

```python
for item in iterable:
    # code to execute for each item
    statement1
```

### Example with a List

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

### Example with `range()`

The `range()` function generates a sequence of numbers, which is commonly used with `for` loops.

```python
for i in range(5):  # Generates numbers from 0 to 4
    print(i)

for i in range(2, 7): # Generates numbers from 2 to 6
    print(i)

for i in range(1, 10, 2): # Generates numbers from 1 to 9 with a step of 2
    print(i)
```

## The `while` Loop

The `while` loop repeatedly executes a block of code as long as a specified condition is true.

### Syntax

```python
while condition:
    # code to execute as long as condition is true
    statement1
    # ensure that the condition eventually becomes false to avoid infinite loops
```

### Example

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

## `break` Statement

The `break` statement is used to exit a loop prematurely, even if the loop's condition has not yet become false or the iterable has not been fully exhausted.

### Example

```python
for i in range(10):
    if i == 5:
        break  # Exit the loop when i is 5
    print(i)
```

## `continue` Statement

The `continue` statement is used to skip the rest of the current iteration of the loop and move to the next iteration.

### Example

```python
for i in range(5):
    if i == 2:
        continue  # Skip printing when i is 2
    print(i)
```

## `else` Clause with Loops

Both `for` and `while` loops can have an optional `else` clause. The `else` block is executed *only if* the loop completes without encountering a `break` statement.

### Example with `for` loop

```python
for i in range(3):
    print(i)
else:
    print("Loop finished without break")

for i in range(3):
    if i == 1:
        break
    print(i)
else:
    print("This will not be printed")
```

### Example with `while` loop

```python
count = 0
while count < 2:
    print(count)
    count += 1
else:
    print("While loop finished without break")
```
