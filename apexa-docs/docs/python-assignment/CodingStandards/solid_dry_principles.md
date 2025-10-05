# SOLID and DRY Principles

SOLID and DRY are fundamental principles in software engineering that guide developers in creating maintainable, scalable, and robust applications. Adhering to these principles leads to cleaner code, reduced complexity, and easier collaboration.

## SOLID Principles

SOLID is an acronym for five design principles intended to make software designs more understandable, flexible, and maintainable. These principles were promoted by Robert C. Martin (Uncle Bob).

### 1. Single Responsibility Principle (SRP)

*   **Definition**: A class should have only one reason to change, meaning it should have only one primary responsibility.
*   **Goal**: To prevent classes from becoming overly complex and to promote modularity.
*   **Why**: If a class has multiple responsibilities, a change to one responsibility might inadvertently affect others, leading to bugs and making the code harder to maintain.

### Example

**Bad (Violates SRP):**

```python
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def save_to_database(self):
        print(f"Saving {self.name} to database.")

    def send_email(self, message):
        print(f"Sending email to {self.email}: {message}")
```

**Good (Adheres to SRP):**

```python
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class UserRepository:
    def save(self, user):
        print(f"Saving {user.name} to database.")

class EmailService:
    def send_email(self, user, message):
        print(f"Sending email to {user.email}: {message}")
```

### 2. Open/Closed Principle (OCP)

*   **Definition**: Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification.
*   **Goal**: To allow new functionality to be added without altering existing, tested code.
*   **Why**: Modifying existing code can introduce new bugs into previously stable parts of the system. Extension allows for safer and more flexible additions.

### Example

**Bad (Violates OCP):**

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Circle:
    def __init__(self, radius):
        self.radius = radius

class AreaCalculator:
    def calculate_area(self, shapes):
        total_area = 0
        for shape in shapes:
            if isinstance(shape, Rectangle):
                total_area += shape.width * shape.height
            elif isinstance(shape, Circle):
                total_area += 3.14159 * shape.radius**2
            # If a new shape is added, this method needs modification
        return total_area
```

**Good (Adheres to OCP):**

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius**2

class AreaCalculator:
    def calculate_area(self, shapes):
        total_area = 0
        for shape in shapes:
            total_area += shape.area() # No modification needed for new shapes
        return total_area
```

### 3. Liskov Substitution Principle (LSP)

*   **Definition**: Objects of a superclass should be replaceable with objects of its subclasses without breaking the application.
*   **Goal**: To ensure that inheritance hierarchies are correctly designed and that subclasses can be used interchangeably with their base classes.
*   **Why**: Violating LSP can lead to unexpected behavior and brittle code, where changes in a subclass require changes in the client code that uses the superclass.

### Example

**Bad (Violates LSP):**

```python
class Bird:
    def fly(self):
        return "Flying high."

class Ostrich(Bird):
    def fly(self_):
        raise Exception("Ostriches cannot fly!") # Ostrich cannot substitute Bird for fly()

def make_bird_fly(bird):
    print(bird.fly())

b = Bird()
o = Ostrich()

make_bird_fly(b) # Works
# make_bird_fly(o) # Fails with an exception
```

**Good (Adheres to LSP):**

```python
class Bird:
    pass

class FlyableBird(Bird):
    def fly(self):
        return "Flying high."

class Ostrich(Bird):
    pass # Ostrich doesn't implement fly, so it doesn't violate substitution for flyable birds

def make_flying_bird_fly(bird: FlyableBird):
    print(bird.fly())

f_bird = FlyableBird()
ostrich = Ostrich()

make_flying_bird_fly(f_bird) # Works
# make_flying_bird_fly(ostrich) # Type checker/runtime would prevent this, as Ostrich is not FlyableBird
```

### 4. Interface Segregation Principle (ISP)

*   **Definition**: Clients should not be forced to depend on interfaces they do not use.
*   **Goal**: To create small, cohesive interfaces rather than large, monolithic ones.
*   **Why**: Large interfaces often mean that a class implementing it has to implement methods it doesn't need, or clients have to depend on methods they don't call, leading to unnecessary coupling and maintenance overhead.

### Example

**Bad (Violates ISP):**

```python
class IWorker: # Monolithic interface
    def work(self):
        pass
    def eat(self):
        pass

class HumanWorker(IWorker):
    def work(self):
        print("Human working")
    def eat(self):
        print("Human eating")

class RobotWorker(IWorker):
    def work(self):
        print("Robot working")
    def eat(self):
        # Robots don't eat, but must implement this method
        raise NotImplementedError("Robots don't eat!")
```

**Good (Adheres to ISP):**

```python
class Workable:
    def work(self):
        pass

class Eatable:
    def eat(self):
        pass

class HumanWorker(Workable, Eatable):
    def work(self):
        print("Human working")
    def eat(self):
        print("Human eating")

class RobotWorker(Workable):
    def work(self):
        print("Robot working")
    # RobotWorker only implements interfaces it needs
```

### 5. Dependency Inversion Principle (DIP)

*   **Definition**: High-level modules should not depend on low-level modules. Both should depend on abstractions. Abstractions should not depend on details. Details should depend on abstractions.
*   **Goal**: To reduce coupling between high-level policy and low-level implementation details, making the system more flexible and testable.
*   **Why**: Direct dependencies on concrete implementations make it hard to swap out components or test them independently.

### Example

**Bad (Violates DIP):**

```python
class LightBulb:
    def turn_on(self):
        print("LightBulb: turned on")
    def turn_off(self):
        print("LightBulb: turned off")

class Switch:
    def __init__(self):
        self.bulb = LightBulb() # High-level (Switch) depends on low-level (LightBulb)

    def operate(self):
        # ... logic ...
        self.bulb.turn_on()
```

**Good (Adheres to DIP):**

```python
from abc import ABC, abstractmethod

class Switchable(ABC): # Abstraction
    @abstractmethod
    def turn_on(self):
        pass
    @abstractmethod
    def turn_off(self):
        pass

class LightBulb(Switchable): # Details depend on abstraction
    def turn_on(self):
        print("LightBulb: turned on")
    def turn_off(self):
        print("LightBulb: turned off")

class Fan(Switchable): # Another detail depending on abstraction
    def turn_on(self):
        print("Fan: turned on")
    def turn_off(self):
        print("Fan: turned off")

class Switch: # High-level module depends on abstraction
    def __init__(self, device: Switchable):
        self.device = device

    def operate(self):
        # ... logic ...
        self.device.turn_on()

# Client code
bulb = LightBulb()
fan = Fan()

bulb_switch = Switch(bulb)
fan_switch = Switch(fan)

bulb_switch.operate()
fan_switch.operate()
```

## DRY Principle: Don't Repeat Yourself

*   **Definition**: Every piece of knowledge must have a single, unambiguous, authoritative representation within a system.
*   **Goal**: To avoid duplication of code and functionality.
*   **Why**: Duplicated code leads to maintenance nightmares, as changes in one place require identical changes in multiple places, increasing the risk of inconsistencies and bugs.

### Examples of Violations

*   Copy-pasting code.
*   Writing the same logic in different parts of an application.
*   Hardcoding values that could be configured or fetched from a single source.

### Adhering to DRY

*   **Functions**: Extract common logic into functions.
*   **Classes/Inheritance**: Use classes and inheritance to share behavior.
*   **Modules/Packages**: Organize reusable code into modules.
*   **Configuration Files**: Store settings and constants in central configuration files.
*   **Databases**: Define data schema once.
*   **Templates**: Use templates for repetitive UI elements.

### Example

**Bad (Violates DRY):**

```python
def calculate_tax_state_a(amount):
    # Tax calculation logic for State A
    return amount * 0.05 + 10

def calculate_tax_state_b(amount):
    # Very similar tax calculation logic for State B
    return amount * 0.05 + 12

def calculate_tax_state_c(amount):
    # Almost identical tax calculation logic for State C
    return amount * 0.05 + 8
```

**Good (Adheres to DRY):**

```python
def calculate_tax(amount, tax_rate, fixed_fee):
    return amount * tax_rate + fixed_fee

# Configuration could come from a database, config file, etc.
TAX_RATES = {
    "State A": {"rate": 0.05, "fee": 10},
    "State B": {"rate": 0.05, "fee": 12},
    "State C": {"rate": 0.05, "fee": 8},
}

def get_tax_for_state(state, amount):
    config = TAX_RATES.get(state)
    if config:
        return calculate_tax(amount, config["rate"], config["fee"])
    return amount # No tax if state not found

print(get_tax_for_state("State A", 100)) # Output: 15.0
print(get_tax_for_state("State B", 100)) # Output: 17.0
```

By following SOLID and DRY principles, developers can build software systems that are more robust, adaptable, and easier to evolve over time.
