# Docstrings

Docstrings (documentation strings) are literal strings that occur as the first statement in a module, function, class, or method definition. They are used to document the purpose and usage of the code, making it easier for others to understand and use.

Unlike regular comments, docstrings are accessible at runtime through the `__doc__` attribute of the object and are used by various tools (like help() function, IDEs, and documentation generators).

## Types of Docstrings

PEP 257 outlines conventions for docstrings. Generally, there are two types:

### 1. One-line Docstrings

Used for simple, concise descriptions. The closing quotes are on the same line as the opening quotes.

### Example

```python
def add(a, b):
    """Return the sum of two numbers."""
    return a + b

class MyClass:
    """A simple example class."""
    def __init__(self, value):
        self.value = value
```

### 2. Multi-line Docstrings

Used for more elaborate documentation. The opening quotes are on a line by themselves, followed by the summary, a blank line, a more elaborate description, and finally closing quotes on a line by themselves.

### Example (Numpy Style - common for scientific/data projects)

```python
def complex_calculation(param1, param2, param3=None):
    """
    Performs a complex calculation involving three parameters.

    This function takes two required parameters and one optional parameter
    to perform a series of mathematical operations and return a final result.

    Parameters
    ----------
    param1 : int or float
        The first input parameter.
    param2 : int or float
        The second input parameter.
    param3 : int or float, optional
        The third input parameter. If None, a default value is used.

    Returns
    -------
    float
        The result of the complex calculation.

    Raises
    ------
    ValueError
        If param1 or param2 are negative.

    Examples
    --------
    >>> complex_calculation(10, 5)
    15.0
    >>> complex_calculation(10, 5, param3=2)
    22.0
    """
    if param1 < 0 or param2 < 0:
        raise ValueError("Parameters must be non-negative.")

    result = param1 + param2
    if param3 is not None:
        result += param3 * 2
    return float(result)


class DataProcessor:
    """
    A class to process and manage data.

    This class provides methods to load, transform, and analyze data.
    It supports various data sources and offers flexible processing options.

    Attributes
    ----------
    data : list
        The list of data currently loaded.
    processor_name : str
        The name of the data processor instance.

    Methods
    -------
    load_data(source_path)
        Loads data from the specified source.
    transform_data()
        Applies transformation rules to the loaded data.
    get_summary()
        Returns a summary of the processed data.
    """
    def __init__(self, processor_name):
        self.processor_name = processor_name
        self.data = []

    def load_data(self, source_path):
        """Loads data from the specified source path."""
        print(f"Loading data from {source_path} using {self.processor_name}")
        self.data = [1, 2, 3, 4, 5] # Dummy data

    def transform_data(self):
        """Applies transformation rules to the loaded data."""
        self.data = [x * 10 for x in self.data]
        print(f"Data transformed: {self.data}")

# Accessing docstrings
print(add.__doc__)
print(complex_calculation.__doc__)
print(DataProcessor.__doc__)
print(DataProcessor.load_data.__doc__)
```

## Docstring Formats

While the basic structure is defined, there are several popular formats for multi-line docstrings, each with slightly different conventions for describing parameters, returns, and other sections:

*   **reStructuredText (reST)**: Used by Sphinx, common in many Python projects.
*   **Google Style**: Very readable and often used in Google's open-source projects.
*   **Numpy Style**: An extension of Google style, popular in scientific computing.
*   **Epytext**: Less common now, but still seen.

Choosing a consistent style (like Numpy or Google) and using it throughout your project is more important than the specific style itself. Many IDEs and tools can help generate and validate docstrings in these formats.
