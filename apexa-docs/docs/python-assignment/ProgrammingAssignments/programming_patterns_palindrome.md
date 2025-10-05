# Programming Assignments: Fibonacci, Patterns, Palindrome, etc.

This section provides Python code solutions and explanations for various common programming assignments, including the Fibonacci series, different number and star patterns, and palindrome checks. These exercises help reinforce fundamental programming concepts like loops, conditional statements, and string manipulation.

## 1. Fibonacci Series

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1. (e.g., 0, 1, 1, 2, 3, 5, 8, 13, ...)

### a. Using a Loop

```python
def fibonacci_loop(n):
    """Generates the Fibonacci series up to n terms using a loop."""
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

print("Fibonacci (loop, 10 terms):", fibonacci_loop(10)) # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

### b. Using Recursion

```python
def fibonacci_recursive(n):
    """Returns the nth Fibonacci number using recursion."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_series_recursive(n):
    """Generates the Fibonacci series up to n terms using recursion for each term."""
    series = []
    for i in range(n):
        series.append(fibonacci_recursive(i))
    return series

print("Fibonacci (recursive, 10 terms):", fibonacci_series_recursive(10)) # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

## 2. Different Patterns

These programs demonstrate how to print various patterns using nested loops, which are common exercises for understanding loop control and output formatting.

### a. Right Half Pyramid (Star Pattern)

```python
def right_half_pyramid(n):
    """Prints a right half pyramid pattern of stars."""
    for i in range(1, n + 1):
        print("*" * i)

print("\nRight Half Pyramid (n=5):")
right_half_pyramid(5)
# Output:
# *
# **
# ***
# ****
# *****
```

### b. Inverted Right Half Pyramid (Star Pattern)

```python
def inverted_right_half_pyramid(n):
    """Prints an inverted right half pyramid pattern of stars."""
    for i in range(n, 0, -1):
        print("*" * i)

print("\nInverted Right Half Pyramid (n=5):")
inverted_right_half_pyramid(5)
# Output:
# *****
# ****
# ***
# **
# *
```

### c. Full Pyramid (Star Pattern)

```python
def full_pyramid(n):
    """Prints a full pyramid pattern of stars."""
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)

print("\nFull Pyramid (n=5):")
full_pyramid(5)
# Output:
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
```

### d. Number Pattern (Right Half Pyramid of Numbers)

```python
def number_right_half_pyramid(n):
    """Prints a right half pyramid pattern of numbers."""
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

print("\nNumber Right Half Pyramid (n=5):")
number_right_half_pyramid(5)
# Output:
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 
```

### e. Alphabet Pattern (Right Half Pyramid of Alphabets)

```python
def alphabet_right_half_pyramid(n):
    """Prints a right half pyramid pattern of alphabets."""
    for i in range(1, n + 1):
        for j in range(i):
            print(chr(65 + j), end=" ") # ASCII for 'A' is 65
        print()

print("\nAlphabet Right Half Pyramid (n=5):")
alphabet_right_half_pyramid(5)
# Output:
# A 
# A B 
# A B C 
# A B C D 
# A B C D E 
```

## 3. Palindrome Check

A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (e.g., "madam", "racecar", 121).

### a. For Strings

```python
def is_palindrome_string(s):
    """Checks if a given string is a palindrome (case-insensitive, alphanumeric only)."""
    processed_s = ''.join(char.lower() for char in s if char.isalnum())
    return processed_s == processed_s[::-1]

print("\nPalindrome Check (String):")
print(f"'madam': {is_palindrome_string('madam')}") # Output: True
print(f"'A man, a plan, a canal: Panama': {is_palindrome_string('A man, a plan, a canal: Panama')}") # Output: True
print(f"'hello': {is_palindrome_string('hello')}") # Output: False
print(f"'12321': {is_palindrome_string('12321')}") # Output: True
```

### b. For Numbers

```python
def is_palindrome_number(n):
    """Checks if a given integer is a palindrome."""
    if n < 0: # Negative numbers are not palindromes
        return False
    return str(n) == str(n)[::-1]

print("\nPalindrome Check (Number):")
print(f"121: {is_palindrome_number(121)}")    # Output: True
print(f"-121: {is_palindrome_number(-121)}")   # Output: False
print(f"12345: {is_palindrome_number(12345)}") # Output: False
```

## 4. Factorial Calculation

The factorial of a non-negative integer `n`, denoted by `n!`, is the product of all positive integers less than or equal to `n`.

### a. Using a Loop

```python
def factorial_loop(n):
    """Calculates the factorial of n using a loop."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0:
        return 1
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print("\nFactorial (Loop):")
print(f"Factorial of 5: {factorial_loop(5)}") # Output: 120
print(f"Factorial of 0: {factorial_loop(0)}") # Output: 1
```

### b. Using Recursion

```python
def factorial_recursive(n):
    """Calculates the factorial of n using recursion."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

print("\nFactorial (Recursion):")
print(f"Factorial of 5: {factorial_recursive(5)}") # Output: 120
print(f"Factorial of 0: {factorial_recursive(0)}") # Output: 1
```
