"""
Description: A class to manage ManagementFeeStrategy objects.
Author: Raven Manalastas
"""
from .service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount
from bank_account.investment_account import InvestmentAccount
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
    TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)
    # Calculate 10 years ago

    def __init__(self, date_created: date, management_fee: float):
        """
        Initializes the ManagementFeeStrategy with the provided creation date and management fee.

        Args:
            date_created (date): The date when the account was created.
            management_fee (float): The management fee associated with the account.
        """
        if isinstance(date_created, date):
            self.__date_created = date_created

        if isinstance(management_fee, float):
            self.__management_fee = management_fee
    
    def calculate_service_charge(self, account: BankAccount) -> float:
        """
        Calculate service charges based on the account creation date and the management fee.

        Args:
            account (BankAccount): The bank account to calculate service charges for.

        Returns:
            float: The calculated service charge.
        """
        if self.__date_created <= InvestmentAccount.TEN_YEARS_AGO:
            return BankAccount.BASE_SERVICE_CHARGE
        else:
            return BankAccount.BASE_SERVICE_CHARGE + self.__date_created