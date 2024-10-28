"""
Description: A class to manage OverdraftStrategy objects.
Author: Raven Manalastas
"""
from .service_charge_strategy import ServiceChargeStrategy

class OverdraftStrategy(ServiceChargeStrategy):
    """
    A strategy for calculating service charges based on the overdraft policy of a bank account.

    Attributes:
        __overdraft_limit (float): The maximum amount that can be overdrawn from the account.
        __overdraft_rate (float): The rate applied to the amount overdrawn, as a decimal.
    
    Methods:
        calculate_service_charge (account: BankAccount): Calculates the service charge.

    """
    def __init__(self, overdraft_limit: float, overdraft_rate: float):
        """
        Initializes the OverdraftStrategy with an overdraft limit and rate.

        Args:
            overdraft_limit (float): The maximum amount that can be overdrawn from the account.
            overdraft_rate (float): The rate applied to the amount overdrawn, as a decimal.
        """
        super().__init__()

        if isinstance(overdraft_limit, float):
            self.__overdraft_limit = overdraft_limit

        if isinstance(overdraft_rate, float):
            self.__overdraft_rate = overdraft_rate

    def calculate_service_charge(self, account):
        """
        Calculates the service charge for the given bank account based on the overdraft strategy.

        Returns:
            float: The calculated service charge.
        """
        if account.balance >= self.__overdraft_limit:
            
            get_service_charges = self.BASE_SERVICE_CHARGE
            
            return self.BASE_SERVICE_CHARGE
        else:
            get_service_charges = self.BASE_SERVICE_CHARGE + \
            (self.__overdraft_limit - account.balance) * self.__overdraft_rate
            
            return get_service_charges