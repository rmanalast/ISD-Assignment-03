"""
Description: A class to manage Bank Account objects.
Author: Raven Manalastas
"""

from abc import ABC, abstractmethod
from datetime import date
from patterns.observer.subject import Subject

class BankAccount(Subject, ABC):
    """
    Attributes:
    __account_number (int): An integer value representing the bank account number.
    __client_number (int): An integer value representing the client number representing the account holder.
    __balance (float): A float value representing the current balance of the bank account.
    _date_created (date): A date object representing the date the account was created. 

    Methods:
    __init__(): Initializes the bank_account
    account_number(): Accessor for the account_number attribute.
    client_number(): Accessor for the client_number attribute.
    balance(): Accessor for the balance attribute.
    update_balance(amount: float): Updates the balance of the account by the given amount.
    deposit(amount: float): Deposits the given amount into the account.
    withdraw(amount: float): Withdraws the given amount from the account.
    __str__(): Returns a string representation of the bank account.
    get_service_charges(): Returns the service charges for the account.
    """

    # BASE_SERVICE_CHARGE = 0.50

    @abstractmethod
    def __init__(self, account_number: int, client_number: int, balance: float,
                 date_created: date):
        """
        Initializes the class attributes with argument values.
        Args
            account_number (int): An integer value representing the bank account number.
            client_number (int): An integer value representing the client number representing the account holder.
            blance (float): A float value representing the current balance of the bank account.
            date_created: (date): A date object representing the date the account was created.

        Raises:
            ValueError:
                    When the account number is non-numeric/integer.
                    When the client number is non-numeric/integer.
                    When the balance cannot be converted to a float
        """
        if not isinstance(account_number, int):
            raise ValueError("Account number must be an integer.")
        
        self.__account_number = account_number

        if not isinstance(client_number, int):
            raise ValueError("Client Number must an integer.")
        
        self.__client_number = client_number
        
        try:
            if not isinstance(balance, float):
                self.__balance = float(balance)
            else:
                self.__balance = balance
        except ValueError:
            self.__balance = 0.00
        
        
        self.__balance = balance

        if not isinstance(date_created, date):
            self._date_created = date.today()
        else:
            self._date_created = date_created

        # Constants
        self.LARGE_TRANSACTION_THRESHOLD = 9999.99
        
        self.LOW_BALANCE_LEVEL = 50.0

    @property
    def account_number(self) -> int:
        """
        Accessor for the __account_number attribute.
        Returns:
            int - An integer value representing the bank account number.
        """
        return self.__account_number
    
    @property
    def client_number(self) -> int:
        """
        Accessor for the __client_number attribute.
        Returns:
            int - An integer value representing the client number representing the account holder.
        """
        return self.__client_number
    
    @property
    def balance(self) -> float:
        """
        Accessor for the __blance attribute.
        Returns:
            float - A float value representing the current balance of the bank account.
        """
        return self.__balance
    
    def update_balance(self, amount) -> float:
        """
        Updates the balance of the account by the given amount.

        Args:
            amount (float): The amount to be added to the balance.

        Raises:
            ValueError: When the amount cannot be converted to a float.
        """
        if not isinstance(self.__balance, float):
            self.__balance = self.__balance

        self.__balance += amount

        if self.__balance < self.LOW_BALANCE_LEVEL:
            self.notify(f"Low balance warning {self.__balance}: on account {self.__account_number}")

        if amount > self.LARGE_TRANSACTION_THRESHOLD:
            self.notify(f"Large transaction {amount}: on account {self.__account_number}")

    def deposit(self, amount) -> float:
        """
        Deposits the given amount into the account.

        Args:
            amount (float): The amount to be deposited into the account.

        Raises:
            ValueError: When the amount is not numeric or not positive.
        """
        try:
            float(amount)
        except TypeError:
            raise TypeError(f"Deposit amount: {amount} must be numeric.")
        if amount <= 0:
            raise ValueError(f"Deposit amount: ${amount:,.2f} must be positive.")
        self.update_balance(amount)
        
    def withdraw(self, amount) -> float:
        """
        Withdraws the given amount from the account.

        Args:
            amount (float): The amount to be withdrawn from the account.

        Raises:
            ValueError: When the amount is not numeric, not positive, or exceeds the account balance.
        """
        try:
            float(amount)
        except TypeError:
             raise TypeError(f"Withdraw amount: {amount} must be numeric.")
        if amount <= 0:
            raise ValueError(f"Withdrawal amount: ${amount:,.2f} must be positive.")
        if amount > self.__balance:
            raise ValueError(f"Withdrawal amount: ${amount:,.2f} must not exceed the account balance: ${self.__balance:,.2f}")
        self.update_balance(-abs(amount))
        
    def __str__(self) -> str:
        """
        Returns a string representation of the BankAccount object.
        """
        return f"Account Number: {self.__account_number} Balance: ${self.__balance:,.2f}"
    
    @abstractmethod
    def get_service_charges(self) -> float:
        """
        Returns the calculated service charges for the account.

        Returns:
            float: The calculated service charges.
        """
        pass