# Object-Oriented Programming (OOP)

Object-Oriented Programming (OOP) is a programming paradigm that organizes software design around data, or objects, rather than functions and logic. Python is a multi-paradigm language that fully supports OOP concepts.

## Key Concepts of OOP

### 1. Classes

A class is a blueprint or a template for creating objects. It defines a set of attributes (data) and methods (functions) that the created objects will have.

### Syntax

```python
class ClassName:
    # Class attributes (shared by all instances)
    class_attribute = "I am a class attribute"

    def __init__(self, param1, param2): # Constructor method
        # Instance attributes (unique to each instance)
        self.param1 = param1
        self.param2 = param2

    def instance_method(self): # Instance method
        return f"Hello from {self.param1} {self.param2}"

    @classmethod
    def class_method(cls): # Class method
        return f"Hello from class: {cls.class_attribute}"

    @staticmethod
    def static_method(arg): # Static method
        return f"Hello from static method with arg: {arg}"
```

### 2. Objects (Instances)

An object is an instance of a class. When a class is defined, no memory is allocated until an object is created from it.

### Example

```python
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"

    def describe(self):
        return f"{self.name} is {self.age} years old."

# Creating objects (instances) of the Dog class
my_dog = Dog("Buddy", 3)
your_dog = Dog("Lucy", 5)

print(my_dog.name)        # Output: Buddy
print(your_dog.age)       # Output: 5
print(my_dog.bark())      # Output: Buddy says Woof!
print(Dog.species)        # Output: Canis familiaris
```

### 3. Encapsulation

Encapsulation is the bundling of data (attributes) and methods (functions) that operate on the data into a single unit, or class. It restricts direct access to some of an object's components, which can prevent accidental modification of data. In Python, encapsulation is achieved through conventions (single underscore for protected, double underscore for private-like attributes) rather than strict access modifiers.

### Example (Convention-based)

```python
class Account:
    def __init__(self, balance):
        self._balance = balance  # Protected attribute (by convention)
        self.__account_number = "12345" # "Private" attribute (name mangling)

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited {amount}. New balance: {self._balance}")
        else:
            print("Deposit amount must be positive.")

my_account = Account(100)
print(my_account.get_balance()) # Output: 100
my_account.deposit(50)          # Output: Deposited 50. New balance: 150

# Accessing protected attribute directly (discouraged but possible)
print(my_account._balance) # Output: 150

# Attempting to access "private" attribute directly (will raise AttributeError)
# print(my_account.__account_number)
# To access: print(my_account._Account__account_number) # Name mangling
```

### 4. Inheritance

Inheritance allows a new class (subclass/derived class) to inherit attributes and methods from an existing class (superclass/base class). This promotes code reusability.

### Example

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return f"{self.name} barks."

class Cat(Animal):
    def speak(self):
        return f"{self.name} meows."

my_dog = Dog("Buddy")
my_cat = Cat("Whiskers")

print(my_dog.speak())   # Output: Buddy barks.
print(my_cat.speak())   # Output: Whiskers meows.
```

### 5. Polymorphism

Polymorphism means "many forms." In OOP, it allows objects of different classes to be treated as objects of a common type (their base class). This is often achieved through method overriding.

### Example

```python
class Bird:
    def intro(self):
        print("There are many types of birds.")

    def flight(self):
        print("Most birds can fly but some cannot.")

class Sparrow(Bird):
    def flight(self):
        print("Sparrows can fly.")

class Ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly.")

bird = Bird()
sparrow = Sparrow()
ostrich = Ostrich()

bird.intro()
bird.flight()

sparrow.intro() # Inherits intro from Bird
sparrow.flight()

ostrich.intro() # Inherits intro from Bird
ostrich.flight()
```

### 6. Abstraction

Abstraction means hiding the complex implementation details and showing only the essential features of an object. In Python, abstract classes and methods can be created using the `abc` (Abstract Base Classes) module.

### Example

```python
from abc import ABC, abstractmethod

class Shape(ABC): # Abstract Base Class
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# shape = Shape() # This would raise a TypeError because Shape is an abstract class

rectangle = Rectangle(10, 5)
print(f"Rectangle area: {rectangle.area()}")         # Output: Rectangle area: 50
print(f"Rectangle perimeter: {rectangle.perimeter()}") # Output: Rectangle perimeter: 30
```
