# Functions

Functions are reusable blocks of code that perform a specific task. They help in organizing code, making it more modular, readable, and maintainable.

## Defining a Function

Functions are defined using the `def` keyword, followed by the function name, parentheses `()`, and a colon `:`. The function body is indented.

### Syntax

```python
def function_name(parameters):
    """Docstring: Explain what the function does."""
    # function body
    statement1
    statement2
    return value
```

### Example

```python
def greet(name):
    """This function greets the person passed in as a parameter."""
    print(f"Hello, {name}!")

greet("Alice") # Calling the function
```

## Parameters and Arguments

**Parameters** are the variables listed inside the parentheses in the function definition. **Arguments** are the actual values passed to the function when it is called.

```python
def add_numbers(a, b): # a and b are parameters
    return a + b

<!-- -->
result = add_numbers(5, 3) # 5 and 3 are arguments
print(result) # Output: 8
```

## Return Values

The `return` statement is used to send a value back to the caller of the function. If no `return` statement is used, the function implicitly returns `None`.

```python
def multiply(x, y):
    return x * y

def do_nothing():
    pass # This function implicitly returns None

product = multiply(4, 5)
print(product) # Output: 20
print(do_nothing()) # Output: None
```

## Default Arguments

Default arguments allow you to provide a default value for a parameter. If a value is not provided for that parameter during the function call, the default value is used.

```python
def say_hello(name="Guest"):
    print(f"Hello, {name}!")

say_hello()        # Output: Hello, Guest!
say_hello("Bob")   # Output: Hello, Bob!
```

## Arbitrary Arguments: `*args` (Non-Keyword Arguments)

If you don't know how many arguments will be passed into your function, you can add `*args` (arbitrary arguments) to the parameter list. This will receive a tuple of arguments.

```python
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_all(1, 2, 3))         # Output: 6
print(sum_all(10, 20, 30, 40))  # Output: 100
```

## Arbitrary Keyword Arguments: `**kwargs` (Keyword Arguments)

If you don't know how many keyword arguments will be passed into your function, you can add `**kwargs` (arbitrary keyword arguments) to the parameter list. This will receive a dictionary of arguments.

```python
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Charlie", age=35)
# Output:
# name: Charlie
# age: 35

display_info(city="London", population=8000000, fact="Big Ben")
# Output:
# city: London
# population: 8000000
# fact: Big Ben
```

## Argument Order

The order of arguments in a function definition typically follows:
1.  Positional arguments
2.  Default arguments
3.  `*args`
4.  `**kwargs`

```python
def complex_function(pos1, pos2, def_arg=10, *args, **kwargs):
    print(f"Positional args: {pos1}, {pos2}")
    print(f"Default arg: {def_arg}")
    print(f"Arbitrary positional args (*args): {args}")
    print(f"Arbitrary keyword args (**kwargs): {kwargs}")

complex_function(1, 2, 3, 4, 5, key1="value1", key2="value2")
# Output:
# Positional args: 1, 2
# Default arg: 3
# Arbitrary positional args (*args): (4, 5)
# Arbitrary keyword args (**kwargs): {'key1': 'value1', 'key2': 'value2'}

complex_function(10, 20, keyA="valA")
# Output:
# Positional args: 10, 20
# Default arg: 10
# Arbitrary positional args (*args): ()
# Arbitrary keyword args (**kwargs): {'keyA': 'valA'}
```
