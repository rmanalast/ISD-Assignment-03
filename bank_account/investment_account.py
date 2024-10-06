"""
Description: A class to represent InvestmentAccount objects.
Author: Raven Manalastas
"""

from bank_account.bank_account import BankAccount
from datetime import date, timedelta

class InvestmentAccount(BankAccount):
    """
    Attributes:
        Inherited attributes from Bank Account Class
        __management_fee (float): The management fee for the investment account.

    Methods:
        Inherited attributes from Bank Account Class
        __init__(): Initializes the bank_account
        __str__(): Returns a string representation of the bank account.
        get_service_charges(): Returns the service charges for the account.
    """

    def __init__(self, account_number: int, client_number: int, balance: float,
                 date_created: date, management_fee: float):
        """
        Initializes a Investment Account object.
        Inherited attributes from Bank Account Class
        Args:
            management_fee (float): The management fee for the investment account
        """
        super().__init__(account_number, client_number, balance, date_created)

        self.TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)

        # Validate and set the management_fee
        try:
            self.__management_fee = float(management_fee)
        except ValueError:
            self.__management_fee = 2.55

    def __str__(self) -> str:
        """
        Returns a string representation of the InvestmentAccount object.
        """
        if self.TEN_YEARS_AGO <= self._date_created:
            return super().__str__() + (f"\nDate Created: {self._date_created} "
                                        f"Management Fee: ${self.__management_fee:.2f} "
                                        f"Account Type: Investment")
        else:
            return super().__str__() + (f"\nDate Created: {self._date_created} "
                                        f"Management Fee: Walved Account Type: Investment")
        
    def get_services_charges(self) -> float:
        """
        Returns the calculated service charges for the account.
        """
        if self._date_created.year < self.TEN_YEARS_AGO.year:
            get_service_charge = self.BASE_SERVICE_CHARGE
        else:
            get_service_charge = self.BASE_SERVICE_CHARGE + self.__management_fee

        return get_service_charge