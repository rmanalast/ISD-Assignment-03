"""
Description: A class to manage MinimumBalanceStrategy objects.
Author: Raven Manalastas
"""
from .service_charge_strategy import ServiceChargeStrategy

class MinimumBalanceStrategy(ServiceChargeStrategy):
    """
    A strategy for calculating service charges based on maintaining a minimum balance in a bank account. 

    Attributes:
        __minimum_balance (float): The minimum balance required to avoid a premium service charge.

    Methods:
        calculate_service_charge (account: BankAccount): Calculates the service charge.
    """
    SERVICE_CHARGE_PREMIUM = 2.0 # Constant premium charge for low balance

    def __init__(self, minimum_balance: float):
        """
        Initializes the MinimumBalanceStrategy with a specified minimum balance.

        Args:
            minimum_balance (float): The minimum balance required to avoid a premium service charge.
        """
        super().__init__()

        if isinstance (minimum_balance, float):
            self.__minimum_balance = minimum_balance

    def calculate_service_charge(self, account):
        """
        Calculate service charges based on whether the account balance is below the minimum balance.

        Args:
            account (BankAccount): The bank account to calculate service charges for.

        Returns:
            float: The calculated service charge.
        """
        if account.balance >= self.__minimum_balance:
            get_service_charge = self.BASE_SERVICE_CHARGE
        else:
            get_service_charge = self.BASE_SERVICE_CHARGE * self.SERVICE_CHARGE_PREMIUM
        
        return get_service_charge