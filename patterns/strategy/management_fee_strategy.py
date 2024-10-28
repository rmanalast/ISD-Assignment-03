"""
Description: A class to manage ManagementFeeStrategy objects.
Author: Raven Manalastas
"""
from .service_charge_strategy import ServiceChargeStrategy
from datetime import date, timedelta

class ManagementFeeStrategy(ServiceChargeStrategy):
    """
    A strategy for calculating management fees based on the creation date of an account.

    Attributes:
        __date_created (date): The date when the account was created.
        __management_fee (float): The management fee associated with the account.
    
    Methods:
        calculate_service_charge (account: BankAccount): Calculates the service charge.
    """
    def __init__(self, date_created: date, management_fee: float, TEN_YEARS_AGO: date):
        """
        Initializes the ManagementFeeStrategy with the provided creation date and management fee.

        Args:
            date_created (date): The date when the account was created.
            management_fee (float): The management fee associated with the account.
        """
        super().__init__()
        
        self.TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)
        # Calculate 10 years ago

        if isinstance(date_created, date):
            self._date_created = date_created

        if isinstance(management_fee, float):
            self.__management_fee = management_fee
    
    def calculate_service_charge(self, account):
        """
        Calculate service charges based on the account creation date and the management fee.

        Returns:
            float: The calculated service charge.
        """
        if account._date_created < self.TEN_YEARS_AGO:
            get_service_charge = self.BASE_SERVICE_CHARGE
        else:
            get_service_charge = self.BASE_SERVICE_CHARGE + self.__management_fee

        return get_service_charge
        