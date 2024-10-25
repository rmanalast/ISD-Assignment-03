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
        TEN_YEARS_AGO (date): A constant representing the date ten years ago from today.
    
    Methods:
        calculate_service_charge (account: BankAccount):
            Calculates the service charge based on the account's creation date.
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
    
    def calculate_service_charge(self, account: BankAccount):
        """
        Calculates the service charge based on the account's creation date
        which if the account is older than 10 years.

        Args:
            account (BankAccount): The bank account for 
            which the service charge is being calculated.

        Returns:
            float: Base service charge for accounts older than 10 years, 
                   or base charge plus management fee for newer accounts.
        """
        if self.__date_created <= InvestmentAccount.TEN_YEARS_AGO:
            return BankAccount.BASE_SERVICE_CHARGE
        else:
            return BankAccount.BASE_SERVICE_CHARGE + self.__date_created