"""
Description: A class to manage ServiceChargeStrategy objects.
Author: Raven Manalastas
"""
from abc import ABC, abstractmethod
from bank_account import *

class ServiceChargeStrategy (ABC):
    """
    Methods:
        calculate_service_charge (account: BankAccount):
            Abstract method that calculates the service charge 
            on the provided BankAccount instance.
    """
    @abstractmethod
    def __init__(self):
        """ Initializes a newly created ServiceChargeStrategy abstract class.
        """
        
        self.BASE_SERVICE_CHARGE = 0.50 # Constant service charge

    @abstractmethod
    def calculate_service_charge(self, account: BankAccount) -> float:
        """
        Calculates the service charge for a given BankAccount

        Returns:
            float: The calculated service charge.
        """
        pass