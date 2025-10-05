# OOPS - BankAccount Class Assignment

This assignment focuses on implementing Object-Oriented Programming (OOP) concepts in Python by creating a `BankAccount` class. The class will include methods for depositing, withdrawing, and checking the balance, with proper exception handling for insufficient funds.

## Assignment Objective

Create a Python class named `BankAccount` that has the following functionalities:

*   **`__init__(self, account_holder, initial_balance=0)`**: The constructor should initialize the `account_holder` (string) and `_balance` (float) attributes. The `_balance` should be protected (by convention) and default to 0 if not provided.
*   **`deposit(self, amount)`**: A method to add funds to the account. It should accept a positive `amount` and update the `_balance`. Raise a `ValueError` if the deposit amount is not positive.
*   **`withdraw(self, amount)`**: A method to remove funds from the account. It should accept a positive `amount`, update the `_balance`, and raise a `ValueError` if the withdrawal amount is not positive. It *must* raise an `InsufficientFundsError` (a custom exception) if the `_balance` is not sufficient for the withdrawal.
*   **`check_balance(self)`**: A method to return the current `_balance` of the account.

## Custom Exception: `InsufficientFundsError`

You need to define a custom exception class named `InsufficientFundsError` that inherits from Python's built-in `ValueError`.

## Python Code Solution

```python
class InsufficientFundsError(ValueError):
    """Custom exception raised when there are insufficient funds for a withdrawal."""
    pass


class BankAccount:
    """Represents a bank account with deposit, withdraw, and balance check functionalities.

    {/*
    Attributes:
        account_holder (str): The name of the account holder.
        _balance (float): The current balance of the account (protected).
    */}
    def __init__(self, account_holder, initial_balance=0.0):
        if not isinstance(account_holder, str) or not account_holder:
            raise ValueError("Account holder name must be a non-empty string.")
        if not isinstance(initial_balance, (int, float)) or initial_balance < 0:
            raise ValueError("Initial balance must be a non-negative number.")

        self.account_holder = account_holder
        self._balance = float(initial_balance)
        print(f"Account created for {self.account_holder} with initial balance: ${self._balance:.2f}")

    def deposit(self, amount):
        """Deposits a specified amount into the account.

        Args:
            amount (float): The amount to deposit. Must be positive.

        Raises:
            ValueError: If the deposit amount is not positive.
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Deposit amount must be a positive number.")
        self._balance += amount
        print(f"Deposited ${amount:.2f}. New balance: ${self._balance:.2f}")

    def withdraw(self, amount):
        """Withdraws a specified amount from the account.

        Args:
            amount (float): The amount to withdraw. Must be positive.

        Raises:
            ValueError: If the withdrawal amount is not positive.
            InsufficientFundsError: If the account balance is insufficient.
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Withdrawal amount must be a positive number.")
        if amount > self._balance:
            raise InsufficientFundsError(
                f"Insufficient funds. Attempted to withdraw ${amount:.2f}, but current balance is ${self._balance:.2f}."
            )
        self._balance -= amount
        print(f"Withdrew ${amount:.2f}. New balance: ${self._balance:.2f}")

    def check_balance(self):
        """Returns the current balance of the account.

        Returns:
            float: The current account balance.
        """
        return self._balance

    def __str__(self):
        return f"BankAccount(holder={self.account_holder}, balance=${self._balance:.2f})"

    def __repr__(self):
        return self.__str__()


# --- Test Cases --- #
if __name__ == "__main__":
    print("\n--- Testing BankAccount Class ---")

    # 1. Create a new account
    account1 = BankAccount("Alice Johnson", 1000)
    print(f"Current balance: ${account1.check_balance():.2f}")

    # 2. Deposit funds
    account1.deposit(500)
    account1.deposit(25.50)
    print(f"Current balance: ${account1.check_balance():.2f}")

    # 3. Withdraw funds successfully
    try:
        account1.withdraw(200)
        print(f"Current balance: ${account1.check_balance():.2f}")
    except (ValueError, InsufficientFundsError) as e:
        print(f"Error during withdrawal: {e}")

    # 4. Attempt to withdraw more than available balance (InsufficientFundsError)
    try:
        account1.withdraw(1500)
    except InsufficientFundsError as e:
        print(f"Expected Error: {e}")
    except ValueError as e:
        print(f"Unexpected ValueError: {e}")
    print(f"Balance after failed withdrawal: ${account1.check_balance():.2f}")

    # 5. Attempt to deposit a negative amount (ValueError)
    try:
        account1.deposit(-100)
    except ValueError as e:
        print(f"Expected Error: {e}")
    print(f"Balance after failed deposit: ${account1.check_balance():.2f}")

    # 6. Attempt to withdraw a negative amount (ValueError)
    try:
        account1.withdraw(-50)
    except ValueError as e:
        print(f"Expected Error: {e}")
    print(f"Balance after failed withdrawal attempt: ${account1.check_balance():.2f}")

    # 7. Create account with invalid initial balance
    try:
        BankAccount("Bob", -50)
    except ValueError as e:
        print(f"Expected Error (Invalid initial balance): {e}")

    # 8. Create account with invalid holder name
    try:
        BankAccount(123)
    except ValueError as e:
        print(f"Expected Error (Invalid account holder): {e}")

    account2 = BankAccount("Charlie Brown")
    print(account2)
