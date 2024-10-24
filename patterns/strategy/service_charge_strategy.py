"""
Description: A class to manage ServiceChargeStrategy objects.
Author: Raven Manalastas
"""
from abc import ABC, abstractmethod
from bank_account.bank_account import BankAccount

class ServiceChargeStrategy (ABC):
    """
    Attributes:
        BASE_SERVICE_CHARGE (float): A constant representing the base service charge amount.

    Methods:
        (account: BankAccount):
            Abstract method that calculates the service charge 
            on the provided BankAccount instance.
    """
    BASE_SERVICE_CHARGE = 0.50 # Constant service charge

    @abstractmethod
    def calculate_service_charge(self, account: BankAccount) -> float:
        """
        Calculates the service charge for a given BankAccount

        Args:
            account (BankAccount): An instance of BankAccount 
                                   for which the service charge is to be calculated.

        Returns:
            float: The calculated service charge based on the account's specifics.
        """
        pass