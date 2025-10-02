# Iterators and Generators

Iterators and generators are powerful features in Python that allow you to work with streams of data efficiently, especially when dealing with large datasets. They provide a memory-efficient way to handle data by producing items one at a time, rather than loading all items into memory at once.

## Iterators

An iterator is an object that can be iterated upon, meaning that you can traverse through all its values. In Python, an object is an iterator if it implements the iterator protocol, which consists of the `__iter__()` and `__next__()` methods.

*   The `__iter__()` method returns the iterator object itself.
*   The `__next__()` method returns the next item from the sequence. If there are no more items, it raises a `StopIteration` exception.

Many built-in types in Python, like lists, tuples, strings, and dictionaries, are iterable. When you use a `for` loop, Python implicitly creates an iterator object.

### Example: Using an Iterator Directly

```python
my_list = [1, 2, 3, 4]
my_iterator = iter(my_list) # Get an iterator from an iterable

print(next(my_iterator)) # Output: 1
print(next(my_iterator)) # Output: 2
print(my_iterator.__next__()) # Output: 3 (alternative way to call next)
print(next(my_iterator)) # Output: 4

# next(my_iterator) # This would raise StopIteration
```

### Creating a Custom Iterator

You can create your own iterator by defining a class with `__iter__` and `__next__` methods.

```python
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 5:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

my_class = MyNumbers()
my_iter = iter(my_class)

for x in my_iter:
    print(x)
# Output:
# 1
# 2
# 3
# 4
# 5
```

## Generators

Generators are a simpler and more elegant way to create iterators. They are functions that return an iterator (an object that can be iterated upon) when called. Generators are defined using the `yield` keyword instead of `return`.

When a generator function is called, it returns an iterator but doesn't start execution immediately. Instead, it pauses its execution until `next()` is called on the iterator. When `yield` is encountered, the value is returned, and the function's state is saved. The next time `next()` is called, execution resumes from where it left off.

### Example: Basic Generator

```python
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator() # Calling the generator function returns a generator object (iterator)

print(next(gen)) # Output: 1
print(next(gen)) # Output: 2
print(next(gen)) # Output: 3
# print(next(gen)) # This would raise StopIteration
```

### Example: Generator with a Loop (Fibonacci Sequence)

Generators are particularly useful for sequences that are either infinite or very large.

```python
def fibonacci_generator(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

fib_gen = fibonacci_generator(7)

for num in fib_gen:
    print(num)
# Output:
# 0
# 1
# 1
# 2
# 3
# 5
# 8
```

## Generator Expressions

Similar to list comprehensions, generator expressions provide a concise way to create generators. They use parentheses `()` instead of square brackets `[]`.

### Syntax

```python
my_generator = (expression for item in iterable if condition)
```

### Example

```python
squares_generator = (x**2 for x in range(5))

print(next(squares_generator)) # Output: 0
print(next(squares_generator)) # Output: 1

for sq in squares_generator:
    print(sq) # Output: 4, 9, 16 (continues from where next() left off)
```

## Advantages of Generators and Iterators

*   **Memory Efficiency**: They produce items one by one, consuming much less memory compared to functions that return entire lists.
*   **Performance**: For very large or infinite sequences, generators can provide better performance because they don't build the entire sequence in memory.
*   **Lazy Evaluation**: Values are generated only when requested, which can save computation time if not all values are needed.
*   **Clean Code**: Generators often lead to more readable and elegant code for sequence generation.
