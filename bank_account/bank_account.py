"""
Description: A class to manage Bank Account objects.
Author: Raven Manalastas
"""
class BankAccount:
    """
    Attributes:
    __account_number (int): An integer value representing the bank account number.
    __client_number (int): An integer value representing the client number representing the account holder.
    __balance (float): A float value representing the current balance of the bank account.

    Methods:
    __init__(): Initializes the bank_account
    account_number(): Accessor for the account_number attribute.
    client_number(): Accessor for the client_number attribute.
    balance(): Accessor for the balance attribute.
    update_balance(amount: float): Updates the balance of the account by the given amount.
    deposit(amount: float): Deposits the given amount into the account.
    withdraw(amount: float): Withdraws the given amount from the account.
    __str__(): Returns a string representation of the bank account.
    """

    def __init__(self, account_number: int, client_number: int, balance: float):
        """
        Initializes the class attributes with argument values.
        Args
            account_number (int): An integer value representing the bank account number.
            client_number (int): An integer value representing the client number representing the account holder.
            blance (float): A float value representing the current balance of the bank account.

        Raises:
            ValueError:
                    When the account number is non-numeric/integer.
                    When the client number is non-numeric/integer.
                    When the balance cannot be converted to a float
        """
        if isinstance(account_number, int):
            self.__account_number = account_number
        else:
            raise ValueError("Account number must be an integer.")
        
        if isinstance(client_number, int):
            self.__client_number = client_number
        else:
            raise ValueError("Client Number must an integer.")
        
        # this try block validates the balance argument, if it is valid, 
        # set the __balance attribute to the balance argument, 
        # if it hits an exception, set the __balance attribute to 0.0 and print an error message
        try:
            self.__balance = float(balance)
        except ValueError:
            self.__balance = 0.0
            print("Invalid balance value. Balance set to 0.0.")

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
        try:
            amount = float(amount)
            self.__balance += amount
        except ValueError:
            print("Invalid amount value. Balance not updated.")
    
    def deposit(self, amount) -> float:
        """
        Deposits the given amount into the account.

        Args:
            amount (float): The amount to be deposited into the account.

        Raises:
            ValueError: When the amount is not numeric or not positive.
        """
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError(f"Deposit amount: {amount:,.2f} must be positive.")
            self.update_balance(amount)
        except ValueError:
            raise ValueError("Deposit amount must be numeric.")
        
    def withdraw(self, amount) -> float:
        """
        Withdraws the given amount from the account.

        Args:
            amount (float): The amount to be withdrawn from the account.

        Raises:
            ValueError: When the amount is not numeric, not positive, or exceeds the account balance.
        """
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError(f"Withdrawal amount: {amount:,.2f} must be positive.")
            if amount > self.__balance:
                raise ValueError(f"Withdrawal amount: {amount:,.2f} must not exceed the account balance: {self.__balance:,.2f}")
            self.update_balance(-amount)
        except ValueError:
            raise ValueError("Withdraw amount must be numeric.")
        
    def __str__(self) -> str:
        """
        Returns a string representation of the BankAccount object.
        """
        return f"Account Number: {self.__account_number} Balance: ${self.__balance:,.2f}"