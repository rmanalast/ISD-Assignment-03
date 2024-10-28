"""
Description: A class to represent SavingsAccount objects.
Author: Raven Manalastas
"""

from bank_account.bank_account import BankAccount
from patterns.strategy.minimum_balance_strategy import MinimumBalanceStrategy
from datetime import date

class SavingsAccount(BankAccount):
    """
    Attributes:
        Inherited attributes from Bank Account Class
        (float): The minimum balance for the savings account

    Methods:
        Inherited attributes from Bank Account Class
        __init__(): Initializes the bank_account
        __str__(): Returns a string representation of the bank account.
        get_service_charges(): Returns the service charges for the account.
    """

    def __init__(self, account_number: int, client_number: int, balance: float,
                 date_created: date, minimum_balance: float):
        """
        Initializes a Investment Account object.
        Inherited attributes from Bank Account Class
        Args:
            minimum_balance (float): The minimum balance for the savings account
        """
        super().__init__(account_number, client_number, balance, date_created)

        # self.SERVICE_CHARGE_PREMIUM = 2.00

        # Validate and set the minimum_balance
        try:
            self.__minimum_balance = float(minimum_balance)
        except ValueError:
            self.__minimum_balance = 50.0

        # Initialize MinimumBalanceStrategy with appropriate arguments
        self._minimum_balance_strategy = MinimumBalanceStrategy(self.__minimum_balance)

    def __str__(self) -> str:
        """
        Returns a string representation of the SavingsAccount object.

        Returns: 
            str: A string containing the account details, 
                 including the minimum balance and account type.
        """
        return super().__str__() + (f"\nMinimum Balance: ${self.__minimum_balance:.2f} "
                                    f"Account Type: Savings")
    
    def get_service_charges(self) -> float:
        """
        Returns the calculated service charges for the account.

        Returns:
            float: The total service charges for the account, 
                   which may vary based on the minimum balance requirement.
        """
        # Use the MinimumBalanceStrategy to calculate service charges based on the balance

        return self._minimum_balance_strategy.calculate_service_charge(self)

# - Old logic commented out
#        if self.balance >= self.__minimum_balance:
#            get_service_charge = self.BASE_SERVICE_CHARGE
#        else:
#            get_service_charge = self.BASE_SERVICE_CHARGE * self.SERVICE_CHARGE_PREMIUM
#        
#        return get_service_charge
# - Old logic commented out