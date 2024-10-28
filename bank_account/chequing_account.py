"""
Description: A class to represent ChequingAccount objects.
Author: Raven Manalastas
"""

from bank_account.bank_account import BankAccount
from patterns.strategy.overdraft_strategy import OverdraftStrategy
from datetime import date

class ChequingAccount(BankAccount):
    """
    Attributes:
        Inherited attributes from Bank Account Class
        __overdraft_limit (float): The maximum amount a balance can be overdrawn 
                                   (below 0.00) before overdraft fees are applied.
        __overdraft_rate (float): The rate to which overdraft fees will be applied.

    Methods:
        Inherited attributes from Bank Account Class
        __init__(): Initializes the bank_account
        __str__(): Returns a string representation of the bank account.
        get_service_charges(): Returns the service charges for the account.
    """

    def __init__(self, account_number: int, client_number: int, balance: float,
                 date_created: date, overdraft_limit: float, overdraft_rate: float):
        """
        Initializes a Chequing Account object.
        Inherited attributes from Bank Account Class
        Args:
            overdraft_limit (float): The overdraft limit for the account.
            overdraft_rate (float): The rate charged for overdraft usage.
        """
        super().__init__(account_number, client_number, balance, date_created)

        # Validate and set the overdraft_limit
        try:
            self.__overdraft_limit = float(overdraft_limit)
        except ValueError:
            self.__overdraft_limit = -100.0

        # Validate and set the overdraft_rate
        try:
            self.__overdraft_rate = float(overdraft_rate)
        except ValueError:
            self.__overdraft_rate = 0.05

        # Initialize OverdraftStrategy with appropriate arguments
        self.__overdraft_strategy = OverdraftStrategy(self.__overdraft_limit, self.__overdraft_rate)

    def __str__(self) -> str:
        """
        Returns a string representation of the ChequingAccount object.

        Returns:
            str: A string containing the account details, 
                 including the overdraft limit, overdraft rate, and account type.
        """
        return super().__str__() + (f"\n Overdraft Limit: ${self.__overdraft_limit:.2f} "
                                   f"Overdraft Rate: {self.__overdraft_rate:.2%} "
                                   f"Account Type: Chequing") 
    
    def get_service_charges(self) -> float:
        """
        Returns the calculated service charges for the account.

        Returns: 
            float: The total service charges for the account, 
                   the overdraft limit and rate if applicable.
        """
        # Use the strategy to calculate service charges based on the balance

        return self.__overdraft_strategy.calculate_service_charge(self)

# - Old logic commented out
#        if self.balance >= self.__overdraft_limit:
#            return self.BASE_SERVICE_CHARGE
#        else:
#            return self.BASE_SERVICE_CHARGE + (self.__overdraft_limit - self.balance) * self.__overdraft_rate
# - Old logic commented out
