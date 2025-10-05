# Python Naming Conventions

Consistent naming conventions are crucial for writing readable, maintainable, and collaborative code. Python follows guidelines primarily outlined in PEP 8 (Python Enhancement Proposal 8), the style guide for Python code. Adhering to these conventions makes your code easier for others (and your future self) to understand.

## General Principles

*   **Readability**: Names should be descriptive and make the purpose of the entity clear.
*   **Consistency**: Follow the same convention throughout your codebase.
*   **Avoid single-letter names** (except in very limited contexts like loop counters `i`, `j`, `k`, or coordinates `x`, `y`, `z`).
*   **Avoid reserved keywords** (e.g., `class`, `def`, `for`, `if`).

## Specific Naming Conventions

### 1. Modules

*   **Convention**: Short, all-lowercase names. Underscores can be used if it improves readability.
*   **Examples**: `mymodule.py`, `my_package.py`

### 2. Packages

*   **Convention**: Short, all-lowercase names. Preferably no underscores, or very few.
*   **Examples**: `mypackage`, `utilities`

### 3. Classes

*   **Convention**: CapWords (CamelCase) convention.
*   **Examples**: `MyClass`, `HttpRequestHandler`, `BankAccount`

### 4. Functions and Methods

*   **Convention**: lowercase with words separated by underscores (snake_case).
*   **Examples**: `my_function`, `calculate_total`, `get_user_data`

### 5. Variables

*   **Convention**: lowercase with words separated by underscores (snake_case).
*   **Examples**: `my_variable`, `total_price`, `user_name`

### 6. Constants

*   **Convention**: All uppercase with words separated by underscores.
*   **Examples**: `MAX_CONNECTIONS`, `PI`, `DATABASE_URL`

### 7. Global Variables

*   **Convention**: Typically treated like constants (all uppercase) or regular variables (snake_case) depending on their immutability and scope. It's generally advised to avoid global variables.

### 8. Instance Attributes

*   **Convention**: Usually `snake_case`.
*   **Protected Attributes**: Start with a single underscore (`_`). This is a convention indicating that the attribute is intended for internal use within the class or its subclasses, but it is still accessible from outside.
    *   **Example**: `_internal_variable`, `_protected_method`
*   **"Private" Attributes**: Start with two leading underscores (`__`). This triggers Python's name mangling, making the attribute less directly accessible from outside the class. It's not truly private but makes accidental access harder.
    *   **Example**: `__private_variable`, `__secret_method`

### 9. Method Arguments

*   **Convention**: 
    *   Instance methods: The first parameter should be `self`.
    *   Class methods: The first parameter should be `cls`.

### 10. Type Variables

*   **Convention**: CapWords (CamelCase) convention, often with `_T` suffix for generic types.
*   **Examples**: `User_T`, `_VT`

## Naming Examples in Code

```python
# Module name: my_utility_module.py

import math

MAX_RETRIES = 5  # Constant

class UserProfile:
    """Represents a user's profile."""

    def __init__(self, username, email):
        self.username = username  # Instance variable
        self.email = email
        self._user_id = self.__generate_user_id() # Protected attribute

    def display_info(self):
        """Displays user information."""
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")

    @classmethod
    def create_guest_profile(cls, guest_id):
        """Creates a guest profile."""
        guest_username = f"guest_{guest_id}"
        guest_email = f"guest{guest_id}@example.com"
        return cls(guest_username, guest_email)

    def __generate_user_id(self): # "Private" method
        # In a real app, this would generate a unique ID
        return f"USER-{random.randint(1000, 9999)}"

def process_data(data_list): # Function
    """Processes a list of data items."""
    processed_items = []
    for item in data_list:
        if item > 0:
            processed_items.append(math.sqrt(item))
    return processed_items


if __name__ == "__main__":
    import random # Import random here for demonstration

    # Using the class
    user1 = UserProfile("alice_smith", "alice@example.com")
    user1.display_info()

    guest_profile = UserProfile.create_guest_profile(123)
    guest_profile.display_info()

    # Using the function
    numbers = [-1, 4, 9, -2, 16]
    results = process_data(numbers)
    print(f"Processed results: {results}")
```
