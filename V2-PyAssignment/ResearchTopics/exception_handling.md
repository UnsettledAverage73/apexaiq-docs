# Exception Handling

Exception handling is a mechanism in Python to deal with runtime errors, also known as exceptions. When an error occurs, Python raises an exception, which can be caught and handled to prevent the program from crashing.

## `try`, `except`, and `finally` Blocks

Python uses `try`, `except`, and `finally` blocks to handle exceptions.

### The `try` Block

The `try` block contains the code that might raise an exception.

### The `except` Block

The `except` block catches and handles the exception. You can specify the type of exception to catch.

### The `finally` Block

The `finally` block is always executed, regardless of whether an exception occurred in the `try` block or not. It's typically used for cleanup operations.

### Syntax

```python
try:
    # Code that might raise an exception
    statement1
except ExceptionType as e:
    # Code to handle the exception
    print(f"An error occurred: {e}")
finally:
    # Code that will always execute
    print("This block always runs.")
```

### Example 1: Basic Exception Handling

```python
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
    print(result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
finally:
    print("Execution completed.")
```

**Output:**
```
Error: Cannot divide by zero!
Execution completed.
```

### Example 2: Catching Multiple Exceptions

You can handle different types of exceptions using multiple `except` blocks.

```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(f"Result: {result}")
except ValueError:
    print("Error: Invalid input. Please enter a number.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
finally:
    print("Operation attempt finished.")
```

**Example Runs:**

1.  **Input: `abc`**
    ```
    Error: Invalid input. Please enter a number.
    Operation attempt finished.
    ```
2.  **Input: `0`**
    ```
    Error: Cannot divide by zero.
    Operation attempt finished.
    ```
3.  **Input: `5`**
    ```
    Result: 2.0
    Operation attempt finished.
    ```

### Example 3: Catching Generic Exceptions

You can catch any exception using `except Exception as e:`.

```python
try:
    file = open("non_existent_file.txt", "r")
    # Some file operations
except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    # Close the file if it was opened, or perform other cleanup
    print("Cleanup complete.")
```

### `else` Block with `try...except`

The `else` block is executed if the code inside the `try` block runs without raising any exceptions.

```python
try:
    numerator = 10
    denominator = 2
    result = numerator / denominator
except ZeroDivisionError:
    print("Error: Division by zero.")
else:
    print(f"Division successful. Result: {result}")
finally:
    print("End of division operation.")
```

**Output:**
```
Division successful. Result: 5.0
End of division operation.
```

If `denominator` was `0`, the output would be:
```
Error: Division by zero.
End of division operation.
```

## Raising Exceptions

You can explicitly raise an exception using the `raise` keyword.

```python
def validate_age(age):
    if not isinstance(age, (int, float)) or age < 0:
        raise ValueError("Age must be a non-negative number.")
    print(f"Age is valid: {age}")

try:
    validate_age(-5)
except ValueError as e:
    print(e) # Output: Age must be a non-negative number.

try:
    validate_age("ten")
except ValueError as e:
    print(e) # Output: Age must be a non-negative number.

try:
    validate_age(30)
except ValueError as e:
    print(e) # This won't be executed
```
