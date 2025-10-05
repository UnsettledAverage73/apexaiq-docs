# List and Dictionary Comprehensions

Comprehensions in Python provide a concise and elegant way to create new sequences (like lists, dictionaries, and sets) using an existing sequence. They are often more readable and efficient than traditional loops.

## List Comprehensions

List comprehensions offer a shorter syntax when you want to create a new list based on the values of an existing list or any other iterable.

### Basic Syntax

```python
new_list = [expression for item in iterable if condition]
```

*   `expression`: The operation to perform on each item.
*   `item`: The variable representing each item in the iterable.
*   `iterable`: The sequence (e.g., list, tuple, string, range) to iterate over.
*   `condition` (optional): A filter that determines if an item should be included.

### Example 1: Basic List Comprehension

Create a list of squares of numbers from 0 to 4.

```python
squares = [x**2 for x in range(5)]
print(squares) # Output: [0, 1, 4, 9, 16]
```

**Equivalent `for` loop:**

```python
squares_loop = []
for x in range(5):
    squares_loop.append(x**2)
print(squares_loop) # Output: [0, 1, 4, 9, 16]
```

### Example 2: List Comprehension with a Condition

Create a list of even numbers from 0 to 9.

```python
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers) # Output: [0, 2, 4, 6, 8]
```

### Example 3: Nested List Comprehension

Create a flattened list from a list of lists.

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [num for row in matrix for num in row]
print(flattened_list) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## Dictionary Comprehensions

Dictionary comprehensions provide a concise way to create dictionaries. They allow you to transform key-value pairs from an existing dictionary or create new ones from other iterables.

### Basic Syntax

<!-- -->
```python
new_dict = {key_expression: value_expression for item in iterable if condition}
```

*   `key_expression`: The expression for the new dictionary's key.
*   `value_expression`: The expression for the new dictionary's value.
*   `item`: The variable representing each item in the iterable.
*   `iterable`: The sequence to iterate over.
*   `condition` (optional): A filter that determines if an item should be included.

### Example 1: Basic Dictionary Comprehension

Create a dictionary where keys are numbers and values are their squares.

```python
squares_dict = {x: x**2 for x in range(5)}
print(squares_dict) # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

**Equivalent `for` loop:**

```python
squares_dict_loop = {}
for x in range(5):
    squares_dict_loop[x] = x**2
print(squares_dict_loop) # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

### Example 2: Dictionary Comprehension with Condition

Create a dictionary with only even numbers and their squares.

```python
even_squares_dict = {x: x**2 for x in range(10) if x % 2 == 0}
print(even_squares_dict) # Output: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
```

### Example 3: Creating a dictionary from two lists

```python
keys = ['a', 'b', 'c']
values = [1, 2, 3]

# Using zip() with dictionary comprehension
combined_dict = {k: v for k, v in zip(keys, values)}
print(combined_dict) # Output: {'a': 1, 'b': 2, 'c': 3}
```

## Set Comprehensions

Set comprehensions are similar to list comprehensions but return a set (which means only unique elements and no specific order).

### Syntax

```python
new_set = {expression for item in iterable if condition}
```

### Example

```python
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_squares = {x**2 for x in numbers if x > 2}
print(unique_squares) # Output: {9, 16, 25} (order may vary)
```
