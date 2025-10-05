# Types of Testing

Software testing is a crucial part of the development lifecycle, ensuring that applications function correctly, meet requirements, and are free of defects. There are various types of testing, each with a specific focus and methodology.

## Main Categories of Testing

### 1. Unit Testing

*   **Definition**: Tests individual components or units of a software to determine if they are fit for use. A "unit" is the smallest testable part of an application, such as a function, method, or class.
*   **Purpose**: To validate that each unit of the software performs as designed. It helps isolate issues to specific code segments.
*   **When to use**: Performed by developers during the coding phase. It is often automated and run frequently.
*   **Tools (Python)**: `unittest`, `pytest`.

### Example (using `pytest`)

Let's say we have a simple function `calculator.py`:

```python
# calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

And a test file `test_calculator.py`:

```python
# test_calculator.py
from calculator import add, subtract

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2
    assert subtract(10, 0) == 10
```

### 2. Integration Testing

*   **Definition**: Tests the interaction between different units or components of a software system. It ensures that integrated modules work together correctly.
*   **Purpose**: To expose defects in the interfaces and interactions between integrated components.
*   **When to use**: After unit testing, before system testing.

### Example

Testing how a user authentication module interacts with a database module.

```python
# auth.py
<!-- -->
class AuthService:
    def __init__(self, db_service):
        self.db_service = db_service

    def login(self, username, password):
        user = self.db_service.get_user(username)
        if user and user.password == password:
            return True
        return False

# db.py
class DatabaseService:
    def get_user(self, username):
        # Simulate database lookup
        users = {"admin": User("admin", "pass123"), "guest": User("guest", "guestpass")}
        return users.get(username)

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

# test_integration.py
from unittest.mock import MagicMock
from auth import AuthService
from db import DatabaseService, User

def test_auth_service_login_success():
    mock_db = MagicMock(spec=DatabaseService)
    mock_db.get_user.return_value = User("testuser", "testpass")

    auth_service = AuthService(mock_db)
    assert auth_service.login("testuser", "testpass") is True

def test_auth_service_login_failure_wrong_password():
    mock_db = MagicMock(spec=DatabaseService)
    mock_db.get_user.return_value = User("testuser", "testpass")

    auth_service = AuthService(mock_db)
    assert auth_service.login("testuser", "wrongpass") is False
```

### 3. System Testing

*   **Definition**: Tests a complete and integrated software system to evaluate the system's compliance with its specified requirements. It's a black-box testing type, meaning the internal structure or design of the software is not considered.
*   **Purpose**: To verify that the entire system meets functional and non-functional requirements (e.g., security, performance, usability).
*   **When to use**: After integration testing, before acceptance testing.

### Example

Testing a complete e-commerce application, including user registration, product browsing, adding to cart, checkout, and payment processing.

### 4. Acceptance Testing (UAT - User Acceptance Testing)

*   **Definition**: A formal testing process where the end-users or clients verify if the system meets their business requirements and is acceptable for delivery. It's often the final phase of testing.
*   **Purpose**: To gain confidence that the system is ready for deployment and usage in the real world.
*   **When to use**: After system testing.

### 5. Functional Testing

*   **Definition**: Focuses on testing the functionalities of the software, verifying that each function of the software operates in conformance with the product requirements.
*   **Includes**: Unit testing, integration testing, system testing, and acceptance testing often have a functional component.

### 6. Non-Functional Testing

*   **Definition**: Focuses on testing non-functional aspects of the software, such as performance, reliability, usability, security, and scalability.
*   **Types**: Performance Testing, Load Testing, Stress Testing, Security Testing, Usability Testing, Compatibility Testing, etc.

### Other Important Types of Testing

*   **Regression Testing**: Rerunning previously executed tests to ensure that changes (bug fixes, new features) have not introduced new defects or re-introduced old ones.
*   **Smoke Testing**: Preliminary tests to reveal simple failures severe enough to reject a prospective software release. It's a quick run-through to ensure the most critical functions work.
*   **Sanity Testing**: A subset of regression testing performed after receiving a software build, with minor changes in code or functionality, to ascertain that the bugs have been fixed and no further issues are introduced due to these changes.
*   **Black-Box Testing**: Testing without knowledge of the internal workings of the application. The tester is only aware of what the software is supposed to do (requirements).
*   **White-Box Testing**: Testing with knowledge of the internal workings of the application. The tester has access to the source code and can examine its structure.
*   **Grey-Box Testing**: A combination of black-box and white-box testing, where the tester has partial knowledge of the internal structure.

Understanding these different types of testing helps in designing a comprehensive testing strategy for any software project.
