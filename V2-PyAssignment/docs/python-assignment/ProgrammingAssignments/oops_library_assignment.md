# OOPS - Library Management System Assignment

This assignment focuses on implementing Object-Oriented Programming (OOP) concepts in Python by creating a simple library management system. The system will involve `Book`, `Member`, and `Library` classes to simulate borrowing and returning books and tracking their availability.

## Assignment Objective

Create three Python classes:

1.  **`Book` Class**:
    *   **`__init__(self, title, author, isbn)`**: Initializes `title`, `author`, and `isbn` (International Standard Book Number). The `isbn` should be unique.
    *   **`__str__(self)`**: Returns a string representation of the book.

2.  **`Member` Class**:
    *   **`__init__(self, member_id, name)`**: Initializes `member_id` (unique identifier) and `name`. Also, initialize an empty list `_borrowed_books` to keep track of books borrowed by the member.
    *   **`borrow_book(self, book)`**: Adds a `Book` object to the `_borrowed_books` list if the book is not already borrowed by the member.
    *   **`return_book(self, book)`**: Removes a `Book` object from the `_borrowed_books` list.
    *   **`get_borrowed_books(self)`**: Returns the list of books currently borrowed by the member.
    *   **`__str__(self)`**: Returns a string representation of the member.

3.  **`Library` Class**:
    *   <!-- `__init__(self, name)`: Initializes the `name` of the library. Also, initialize two empty lists: `_books` (to store all `Book` objects in the library) and `_members` (to store all `Member` objects). -->
    *   **`add_book(self, book)`**: Adds a `Book` object to the `_books` list. Ensure no duplicate ISBNs.
    *   **`register_member(self, member)`**: Adds a `Member` object to the `_members` list. Ensure no duplicate member IDs.
    *   **`borrow_book(self, book_isbn, member_id)`**: Handles the logic for a member borrowing a book.
        *   Find the book by ISBN in `_books`. If not found, raise `ValueError`.
        *   Check if the book is available (not currently borrowed by any member). If not available, raise `ValueError`.
        *   Find the member by `member_id` in `_members`. If not found, raise `ValueError`.
        *   Update the `_borrowed_books` for the member.
        *   Mark the book as borrowed (you'll need to add an attribute to the `Book` class, or track it within the `Library` class).
    *   **`return_book(self, book_isbn, member_id)`**: Handles the logic for a member returning a book.
        *   Find the book by ISBN. If not found, raise `ValueError`.
        *   Find the member by `member_id`. If not found, raise `ValueError`.
        *   Check if the book was actually borrowed by *this* member. If not, raise `ValueError`.
        *   Remove the book from the member's `_borrowed_books` list.
        *   Mark the book as available.
    *   **`list_available_books(self)`**: Returns a list of `Book` objects that are currently not borrowed.
    *   **`list_borrowed_books(self)`**: Returns a list of `Book` objects that are currently borrowed.

## Python Code Solution

```python
class Book:
    def __init__(self, title, author, isbn):
        if not isinstance(title, str) or not title:
            raise ValueError("Book title cannot be empty.")
        if not isinstance(author, str) or not author:
            raise ValueError("Book author cannot be empty.")
        if not isinstance(isbn, str) or not isbn:
            raise ValueError("Book ISBN cannot be empty.")

        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False # New attribute to track availability

    def __str__(self):
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn})"

    def __repr__(self):
        return self.__str__()


class Member:
    def __init__(self, member_id, name):
        if not isinstance(member_id, str) or not member_id:
            raise ValueError("Member ID cannot be empty.")
        if not isinstance(name, str) or not name:
            raise ValueError("Member name cannot be empty.")

        self.member_id = member_id
        self.name = name
        self._borrowed_books = []

    def borrow_book(self, book):
        if not isinstance(book, Book):
            raise TypeError("Only Book objects can be borrowed.")
        if book in self._borrowed_books:
            print(f"{self.name} already borrowed '{book.title}'.")
            return False
        self._borrowed_books.append(book)
        print(f"{self.name} borrowed '{book.title}'.")
        return True

    def return_book(self, book):
        if not isinstance(book, Book):
            raise TypeError("Only Book objects can be returned.")
        if book in self._borrowed_books:
            self._borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'.")
            return True
        print(f"{self.name} did not borrow '{book.title}'.")
        return False

    def get_borrowed_books(self):
        return self._borrowed_books

    def __str__(self):
        return f"Member: {self.name} (ID: {self.member_id})"

    def __repr__(self):
        return self.__str__()


class Library:
    def __init__(self, name):
        if not isinstance(name, str) or not name:
            raise ValueError("Library name cannot be empty.")
        self.name = name
        self._books = []
        self._members = []

    def add_book(self, book):
        if not isinstance(book, Book):
            raise TypeError("Only Book objects can be added to the library.")
        if any(b.isbn == book.isbn for b in self._books):
            print(f"Book with ISBN {book.isbn} already exists in the library.")
            return False
        self._books.append(book)
        print(f"Added book: {book}")
        return True

    def register_member(self, member):
        if not isinstance(member, Member):
            raise TypeError("Only Member objects can be registered.")
        if any(m.member_id == member.member_id for m in self._members):
            print(f"Member with ID {member.member_id} already registered.")
            return False
        self._members.append(member)
        print(f"Registered member: {member}")
        return True

    def _find_book(self, isbn):
        for book in self._books:
            if book.isbn == isbn:
                return book
        return None

    def _find_member(self, member_id):
        for member in self._members:
            if member.member_id == member_id:
                return member
        return None

    def borrow_book(self, book_isbn, member_id):
        book = self._find_book(book_isbn)
        if not book:
            raise ValueError(f"Book with ISBN {book_isbn} not found in the library.")

        if book.is_borrowed:
            raise ValueError(f"Book '{book.title}' is currently borrowed.")

        member = self._find_member(member_id)
        if not member:
            raise ValueError(f"Member with ID {member_id} not found.")

        if member.borrow_book(book):
            book.is_borrowed = True
            print(f"'{book.title}' successfully borrowed by {member.name}.")
            return True
        return False

    def return_book(self, book_isbn, member_id):
        book = self._find_book(book_isbn)
        if not book:
            raise ValueError(f"Book with ISBN {book_isbn} not found in the library.")

        member = self._find_member(member_id)
        if not member:
            raise ValueError(f"Member with ID {member_id} not found.")

        if book not in member.get_borrowed_books():
            raise ValueError(f"Book '{book.title}' was not borrowed by {member.name}.")

        if member.return_book(book):
            book.is_borrowed = False
            print(f"'{book.title}' successfully returned by {member.name}.")
            return True
        return False

    def list_available_books(self):
        return [book for book in self._books if not book.is_borrowed]

    def list_borrowed_books(self):
        return [book for book in self._books if book.is_borrowed]

    def __str__(self):
        return f"Library: {self.name}"


# --- Test Cases --- #
if __name__ == "__main__":
    print("\n--- Testing Library Management System ---")

    # Setup Library, Books, and Members
    my_library = Library("Central City Library")

    book1 = Book("The Great Python", "A. Code", "978-1-2345-6789-0")
    book2 = Book("OOP Masterclass", "B. Design", "978-0-9876-5432-1")
    book3 = Book("Data Science Basics", "C. Anz", "978-5-6789-1234-5")

    my_library.add_book(book1)
    my_library.add_book(book2)
    my_library.add_book(book3)
    my_library.add_book(Book("The Great Python", "A. Code", "978-1-2345-6789-0")) # Duplicate ISBN

    member1 = Member("M001", "Alice Wonderland")
    member2 = Member("M002", "Bob The Builder")

    my_library.register_member(member1)
    my_library.register_member(member2)
    my_library.register_member(Member("M001", "Alice Clone")) # Duplicate ID

    print("\nAvailable Books:", my_library.list_available_books())
    print("Borrowed Books:", my_library.list_borrowed_books())

    # Member 1 borrows a book
    try:
        my_library.borrow_book(book1.isbn, member1.member_id)
    except ValueError as e:
        print(f"Error: {e}")

    print("\nAvailable Books:", my_library.list_available_books())
    print("Borrowed Books:", my_library.list_borrowed_books())
    print("Alice's Borrowed Books:", member1.get_borrowed_books())

    # Member 2 borrows a book
    try:
        my_library.borrow_book(book2.isbn, member2.member_id)
    except ValueError as e:
        print(f"Error: {e}")

    # Attempt to borrow an already borrowed book
    try:
        my_library.borrow_book(book1.isbn, member2.member_id)
    except ValueError as e:
        print(f"Expected Error: {e}")

    # Member 1 returns a book
    try:
        my_library.return_book(book1.isbn, member1.member_id)
    except ValueError as e:
        print(f"Error: {e}")

    print("\nAvailable Books:", my_library.list_available_books())
    print("Borrowed Books:", my_library.list_borrowed_books())
    print("Alice's Borrowed Books:", member1.get_borrowed_books())

    # Attempt to return a book not borrowed by member 2
    try:
        my_library.return_book(book3.isbn, member2.member_id)
    except ValueError as e:
        print(f"Expected Error: {e}")

    # Attempt to borrow a non-existent book
    try:
        my_library.borrow_book("NONEXISTENT-ISBN", member1.member_id)
    except ValueError as e:
        print(f"Expected Error: {e}")

    # Attempt to borrow by non-existent member
    try:
        my_library.borrow_book(book3.isbn, "NONEXISTENT-MEMBER")
    except ValueError as e:
        print(f"Expected Error: {e}")
```
