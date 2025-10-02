# Programming Assignment: Do testing using pytest (optional)

`pytest` is a popular and powerful Python testing framework that makes it easy to write simple yet comprehensive tests. It automatically discovers tests, provides detailed failure information, and supports advanced features like fixtures, parametrization, and plugins. This assignment will guide you through writing and running basic unit tests using `pytest`.

## Assignment Objective

1.  **Install `pytest`**.
2.  Create a simple Python module with a few functions to be tested.
3.  Write corresponding unit tests for these functions using `pytest`.
4.  Run the tests and interpret the results.

## Prerequisites

*   Python installed (preferably in a virtual environment).

## 1. Installation

First, install `pytest` in your virtual environment:

```bash
pip install pytest
```

## 2. Create the Code to be Tested

Let's create a simple Python file named `my_math.py` with some basic mathematical functions:

```python
# V2-PyAssignment/my_math.py

def add(a, b):
    """Adds two numbers."""
    return a + b

def subtract(a, b):
    """Subtracts two numbers."""
    return a - b

def multiply(a, b):
    """Multiplies two numbers."""
    return a * b

def divide(a, b):
    """Divides two numbers. Raises ValueError if divisor is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def power(base, exponent):
    """Calculates base raised to the power of exponent."""
    return base ** exponent
```

## 3. Write Unit Tests using `pytest`

Create a test file for `my_math.py`. `pytest` automatically discovers files named `test_*.py` or `*_test.py`. Let's name our test file `test_my_math.py` in the same directory:

```python
# V2-PyAssignment/test_my_math.py

import pytest
from my_math import add, subtract, multiply, divide, power


def test_add():
    """Test cases for the add function."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(100, 200) == 300
    assert add(2.5, 3.5) == 6.0

def test_subtract():
    """Test cases for the subtract function."""
    assert subtract(5, 2) == 3
    assert subtract(10, 15) == -5
    assert subtract(0, 0) == 0
    assert subtract(7.5, 2.5) == 5.0

def test_multiply():
    """Test cases for the multiply function."""
    assert multiply(2, 4) == 8
    assert multiply(-3, 5) == -15
    assert multiply(0, 100) == 0
    assert multiply(2.5, 2) == 5.0

def test_divide_positive_numbers():
    """Test division with positive numbers."""
    assert divide(10, 2) == 5.0
    assert divide(7, 2) == 3.5

def test_divide_by_one():
    """Test division by 1."""
    assert divide(5, 1) == 5.0

def test_divide_by_zero_raises_error():
    """Test that dividing by zero raises a ValueError."""
    with pytest.raises(ValueError):
        divide(10, 0)

def test_power():
    """Test cases for the power function."""
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(10, 1) == 10
    assert power(2, -1) == 0.5
    assert power(4, 0.5) == 2.0 # Square root
```

### Explanation of `pytest` features used:

*   **Test Discovery**: `pytest` automatically finds test functions (starting with `test_`) in files named `test_*.py` or `*_test.py`.
*   **Assertions**: Standard Python `assert` statements are used to check conditions. If an assertion fails, `pytest` provides detailed information.
*   **`pytest.raises()`**: This context manager is used to test that a specific exception is raised when expected. If the specified exception is not raised within the `with` block, the test will fail.

## 4. Run the Tests

Navigate to the `V2-PyAssignment` directory in your terminal and run `pytest`:

```bash
(venv) /path/to/V2-PyAssignment$ pytest
```

### Expected Output (if all tests pass):

```
============================= test session starts ==============================
platform linux -- Python 3.8.10, pytest-7.x.x, pluggy-1.x.x
rootdir: /path/to/V2-PyAssignment
collected 7 items                                                              

V2-PyAssignment/test_my_math.py .......                                  [100%]

============================== 7 passed in 0.xxs ===============================
```

If there were any failures, `pytest` would output detailed traceback information, making it easy to identify and fix the issues.

## Advanced `pytest` Features (Optional Exploration)

*   **Fixtures**: Functions that run before (and optionally after) test functions to provide setup/teardown code. Declared with `@pytest.fixture`.
*   **Parametrization**: Run the same test function multiple times with different sets of arguments using `@pytest.mark.parametrize`.
*   **Skipping Tests**: Use `@pytest.mark.skip` or `@pytest.mark.skipif` to conditionally skip tests.
*   **XFAIL (Expected to Fail)**: Use `@pytest.mark.xfail` for tests that are expected to fail but shouldn't break the test suite.
*   **Plugins**: `pytest` has a rich ecosystem of plugins for various purposes (e.g., `pytest-cov` for coverage reports).

By incorporating `pytest` into your development workflow, you can ensure the quality and correctness of your Python code through automated testing.
