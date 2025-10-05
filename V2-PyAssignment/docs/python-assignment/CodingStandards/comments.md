# Comments

Comments are an essential part of writing understandable and maintainable code. In Python, comments are ignored by the interpreter but serve as valuable notes for developers, explaining the purpose, logic, or functionality of the code.

## Types of Comments

Python supports single-line comments and, by convention, multi-line strings can be used as comments (though they are technically docstrings when placed in specific locations).

### 1. Single-Line Comments

Single-line comments start with a hash symbol (`#`) and extend to the end of the physical line. They are typically used for short explanations or to temporarily disable a line of code.

### Examples

```python
# This is a full-line comment explaining the next line of code
radius = 5  # Initialize the radius variable

# Calculate the area of a circle
area = 3.14159 * radius**2

print(area)

# print("This line is commented out and will not execute.")
```

### 2. Multi-Line Comments (Block Comments)

Python does not have a dedicated syntax for multi-line comments like some other languages (e.g., `/* ... */` in C++ or Java). However, multi-line strings (strings enclosed in triple quotes `"""` or `'''`) can be used as block comments if they are not assigned to a variable or used as a docstring.

While technically processed as string literals, when they are not part of an assignment or function/class definition, they are effectively ignored by the interpreter and serve as comments.

### Example

```python
"""
This is a multi-line string.
When not assigned to a variable or used as a docstring,
Python treats it as a block comment.
It can be useful for explaining complex blocks of code.
"""

def multiply(a, b):
    <!-- -->
    '''
    This is also a multi-line string.
    If placed here, it would be a docstring for the function.
    But outside of a definition, it can act as a comment.
    '''
    return a * b

result = multiply(4, 5)
print(result)
```

## When to Use Comments

*   **Explain complex logic**: When the code itself isn't immediately obvious.
*   **Clarify intent**: What a particular piece of code is trying to achieve.
*   **Warning/TODOs**: Mark areas that need attention or have potential issues.
*   **Code out temporarily**: To disable code during development or debugging.

## Best Practices for Comments

*   **Be concise**: Don't write lengthy essays if a few words suffice.
*   **Be clear and unambiguous**: Ensure the comment accurately reflects the code.
*   **Avoid redundant comments**: Don't state the obvious (e.g., `# x = 10` followed by `# assign 10 to x`). Good code is often self-documenting.
*   **Keep comments up-to-date**: Outdated comments can be more harmful than no comments.
*   **Focus on *why* not *what***: Explain the reasoning behind a decision, not just what the code does (which should be evident from the code itself).
*   **Use docstrings for public APIs**: For modules, classes, functions, and methods, use docstrings for formal documentation.

## Example of Good vs. Bad Comments

```python
# Bad Comment: Redundant, explains the obvious
x = 10 # assign 10 to x

# Good Comment: Explains intent/reasoning
def calculate_discount(price, quantity):
    # Apply a 10% discount for bulk orders over 100 units
    if quantity > 100:
        return price * quantity * 0.90
    return price * quantity

# Bad Comment: Outdated or misleading
# This function used to support negative numbers, but it was removed.
# (Code below doesn't handle negative numbers now)
def process_positive_numbers(numbers):
    return [n for n in numbers if n > 0]
```
