# Decorators

Decorators in Python are a powerful and elegant way to modify or enhance the behavior of functions or methods. They allow you to wrap a function with another function, adding functionality before or after the wrapped function executes, without permanently altering its code.

## What is a Decorator?

A decorator is essentially a function that takes another function as an argument, adds some functionality, and returns a new function (or the modified original function).

## Basic Decorator Structure

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

**Output:**
```
Something is happening before the function is called.
Hello!
Something is happening after the function is called.
```

### Explanation

1.  **`my_decorator(func)`**: This is the decorator function. It takes another function (`func`) as an argument.
2.  **`wrapper(\*args, \*\*kwargs)`**: This is an inner function defined inside `my_decorator`. It\'s the one that will actually replace the original `say_hello` function. It uses `*args` and `**kwargs` to accept any number of positional and keyword arguments, making the decorator flexible.
3.  **`result = func(*args, **kwargs)`**: The original function (`func`) is called inside the `wrapper`, and its return value is stored.
4.  **`return wrapper`**: The decorator returns the `wrapper` function.
5.  **`@my_decorator`**: This is the syntactic sugar for applying a decorator. It\'s equivalent to `say_hello = my_decorator(say_hello)`.

## Decorators with Arguments

To pass arguments to a decorator, you need an extra layer of nesting.

```python
def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")

greet("Alice")
```

**Output:**
```
Hello Alice
Hello Alice
Hello Alice
```

### Explanation

1.  **`repeat(num_times)`**: This outer function takes the decorator arguments (`num_times`). It returns the actual decorator function (`decorator_repeat`).
2.  **`decorator_repeat(func)`**: This is the decorator, similar to `my_decorator` in the previous example. It takes the function to be decorated (`greet`).
3.  **`wrapper`**: This inner function executes the original function `num_times`.

## Real-world Use Cases for Decorators

*   **Logging**: Logging function calls, arguments, and return values.
*   **Timing**: Measuring the execution time of functions.
*   **Authentication/Authorization**: Restricting access to functions based on user roles.
*   **Caching**: Storing results of expensive function calls.
*   **Input Validation**: Validating arguments passed to a function.
*   **Rate Limiting**: Limiting how often a function can be called.

## Example: Timing a Function

```python
import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.4f} seconds to execute.")
        return result
    return wrapper

@timing_decorator
def long_running_function(n):
    sum_val = 0
    for i in range(n):
        sum_val += i
    return sum_val

long_running_function(1000000)
# Example Output:
# Function long_running_function took 0.0381 seconds to execute.
```