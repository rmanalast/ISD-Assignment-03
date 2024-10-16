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

        Returns:
            str: A string containing the account details, 
                 including the date created, management fee 
                 (if applicable), and account type.
        """
        # The string varuable calls the abstract method 
        # of the bank_account string
        string = super().__str__() 

        if self.TEN_YEARS_AGO <= self._date_created:
            
            string += (f"\nDate Created: {self._date_created} "
                       f"Management Fee: ${self.__management_fee:.2f} "
                       f"Account Type: Investment")
        else:
            string += (f"\nDate Created: {self._date_created} "
                       f"Management Fee: Waived Account Type: Investment")
            
        return string
        
    def get_service_charges(self) -> float:
        """
        Returns the calculated service charges for the account.

        Returns:
            float: The total service charges for the account, 
                   which may vary based on the account's creation date and management fee.
        """
        if self._date_created < self.TEN_YEARS_AGO:
            get_service_charge = self.BASE_SERVICE_CHARGE
        else:
            get_service_charge = self.BASE_SERVICE_CHARGE + self.__management_fee

        return get_service_charge