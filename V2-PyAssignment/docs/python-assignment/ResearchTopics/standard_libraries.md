# Standard Libraries

Python's standard library is a vast collection of modules that provide a wide range of functionalities, saving developers from writing code for common tasks from scratch. These modules are readily available with every Python installation.

## Key Standard Libraries

Here are some commonly used standard libraries:

### 1. `os` Module: Operating System Interface

The `os` module provides a way of using operating system dependent functionality like reading or writing to a file system. It allows you to interact with the operating system, performing tasks such as file and directory manipulation, environment variable access, and process management.

### Common `os` Functions:

*   **`os.getcwd()`**: Get the current working directory.
*   **`os.chdir(path)`**: Change the current working directory.
*   **`os.listdir(path)`**: List contents of a directory.
*   **`os.mkdir(path)`**: Create a directory.
*   **`os.remove(path)`**: Remove (delete) a file.
*   **`os.rename(src, dst)`**: Rename a file or directory.
*   **`os.path`**: A sub-module for path manipulations (e.g., `os.path.join()`, `os.path.exists()`).

```python
import os

print(f"Current directory: {os.getcwd()}")

# Create a new directory
```python
try:
    os.mkdir("my_new_dir")
    print("Directory 'my_new_dir' created.")
except FileExistsError:
    print("Directory 'my_new_dir' already exists.")
```

# List contents of a directory
```python
print(f"Contents of current directory: {os.listdir('.')}")
```

# Join paths safely
file_path = os.path.join(os.getcwd(), "my_new_dir", "my_file.txt")
print(f"Example file path: {file_path}")
```

### 2. `sys` Module: System-specific Parameters and Functions

The `sys` module provides access to system-specific parameters and functions, such as command-line arguments, Python version, and recursion limit.

### Common `sys` Functions/Attributes:

*   **`sys.argv`**: A list of command-line arguments.
*   **`sys.version`**: A string containing the Python interpreter's version information.
*   **`sys.platform`**: A string indicating the operating system platform.
*   **`sys.exit(code)`**: Exit the Python interpreter.

```python
import sys

print(f"Python Version: {sys.version.splitlines()[0]}")
print(f"Operating System: {sys.platform}")
print(f"Command Line Arguments: {sys.argv}")

# To exit the script:
# sys.exit(0)
```

### 3. `math` Module: Mathematical Functions

The `math` module provides access to mathematical functions defined by the C standard.

### Common `math` Functions:

*   **`math.sqrt(x)`**: Returns the square root of x.
*   **`math.pi`**: The mathematical constant pi.
*   **`math.ceil(x)`**: Returns the smallest integer greater than or equal to x.
*   **`math.floor(x)`**: Returns the largest integer less than or equal to x.
*   **`math.sin(x)`, `math.cos(x)`, `math.tan(x)`**: Trigonometric functions.

```python
import math

print(f"Value of Pi: {math.pi}")
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Ceiling of 4.3: {math.ceil(4.3)}")
print(f"Floor of 4.8: {math.floor(4.8)}")
```

### 4. `datetime` Module: Date and Time Handling

The `datetime` module supplies classes for working with dates and times in both simple and complex ways.

### Common `datetime` Classes/Functions:

*   **`datetime.date`**: Represents a date (year, month, day).
*   **`datetime.time`**: Represents a time (hour, minute, second, microsecond).
*   **`datetime.datetime`**: Represents both a date and a time.
*   **`datetime.timedelta`**: Represents a duration, the difference between two `date`, `time`, or `datetime` instances.

```python
import datetime

# Current date and time
now = datetime.datetime.now()
print(f"Current datetime: {now}")

# Specific date
today = datetime.date.today()
print(f"Today's date: {today}")

# Formatting dates
print(f"Formatted date: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# Date arithmetic
one_week_later = now + datetime.timedelta(weeks=1)
print(f"One week later: {one_week_later}")
```

### 5. `random` Module: Generate Pseudo-random Numbers

The `random` module implements pseudo-random number generators for various distributions.

### Common `random` Functions:

*   **`random.random()`**: Returns a random float `x` such that `0.0 <= x < 1.0`.
*   **`random.randint(a, b)`**: Returns a random integer `N` such that `a <= N <= b`.
*   **`random.choice(seq)`**: Returns a random element from a non-empty sequence.
*   **`random.shuffle(x)`**: Shuffles a sequence in place.

```python
import random

print(f"Random float: {random.random()}")
print(f"Random integer between 1 and 10: {random.randint(1, 10)}")

my_list = ['apple', 'banana', 'cherry']
print(f"Random choice from list: {random.choice(my_list)}")

random.shuffle(my_list)
print(f"Shuffled list: {my_list}")
```

### 6. `json` Module: JSON encoder and decoder

The `json` module provides functions for working with JSON (JavaScript Object Notation) data, which is commonly used for data interchange on the web.

### Common `json` Functions:

*   **`json.dumps(obj)`**: Serialize `obj` to a JSON formatted `str`.
*   **`json.loads(s)`**: Deserialize `s` (a `str`, `bytes` or `bytearray` instance containing a JSON document) to a Python object.

```python
import json

# Python dictionary
data = {
    "name": "John Doe",
    "age": 30,
    "isStudent": False,
    "courses": [{"title": "Math"}, {"title": "Science"}]
}

# Convert Python dict to JSON string
json_string = json.dumps(data, indent=4)
print("\nPython dictionary converted to JSON string:")
print(json_string)

# Convert JSON string back to Python dict
parsed_data = json.loads(json_string)
print("\nJSON string converted back to Python dictionary:")
print(parsed_data["name"])
```
