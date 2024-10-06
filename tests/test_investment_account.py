"""
Description: A class to represent InvestmentAccount objects.
Author: Raven Manalastas
the following command:
    python -m unittest tests/test_investment_account.py
"""
from datetime import date
from bank_account.investment_account import InvestmentAccount
import unittest

class TestInvestmentAccount(unittest.TestCase):
    """
    This class contains unit tests for the InvestmentAccount class.
    """

    def setUp(self):
        self.investment_account = InvestmentAccount(709, 9710, 450, date(2011, 7, 9), 2)

    def test_init_vaild_inputs_attributes_set(self):
        # Arrange:
        investment_account = InvestmentAccount(709, 9710, 450, date(2011, 7, 9), 2)

        # Act and Assert:
        self.assertEqual(709, self.investment_account._BankAccount__account_number)
        self.assertEqual(9710, self.investment_account._BankAccount__client_number)
        self.assertEqual(450, self.investment_account._BankAccount__balance)

        # protected attributes
        self.assertEqual(date(2011, 7, 9), self.investment_account._date_created)

        # private attributes
        self.assertEqual(2, self.investment_account._InvestmentAccount__management_fee)

    def test_init_management_fee_invalid_input_type(self):
        """
        Test that the management_fee has a invalid type
        """
        # Act and Assert:
        self.investment_account = InvestmentAccount(709, 9710, 450, date(2011, 7, 9), 
                                                    "Invalid investment")
        self.assertEqual(2.55, self.investment_account._InvestmentAccount__management_fee)

    def test_get_services_charges_method_date_created_more_than_ten_years_ago(self):
        """
        Test that the get_service_charges date created is more than ten years ago
        """
        # Act and Assert:
        get_service_charges = self.investment_account.get_service_charges()

        self.assertEqual(0.50, get_service_charges)

    def test_get_services_charges_method_date_created_equal_ten_years_ago(self):
        """
        Test that the get_service_charges date created is equal ten years ago
        """
        # Act and Assert:
        self.investment_account = InvestmentAccount(709, 9710, 450, date(2014, 7, 9), 2)
        get_service_charges = self.investment_account.get_service_charges()

        self.assertEqual(2.5, get_service_charges)

    def test_get_services_charges_method_date_within_ten_years(self):
        """
        Test that the get_service_charges date created is within ten years ago
        """
        # Act and Assert:
        self.investment_account = InvestmentAccount(709, 9710, 450, date(2018, 7, 9), 2)

        get_service_charges = self.investment_account.get_service_charges()

        self.assertEqual(2.5, get_service_charges)

    def test_str_method_display_waived_managment_fee_when_date_created_ten_years_ago(self):
        """
        Tests that the str method displays the correct information 
        when the date created is more than ten years ago.
        """
        # Act and Assert:
        self.assertEqual(f"Account Number: 709 Balance: $450.00"
                         f"\nDate Created: 2011-07-09 Management Fee: Waived "
                         f"Account Type: Investment", str(self.investment_account))
    
    def test_str_mothod_display_management_fee_when_date_created_within_ten_years(self):
        """
        Tests that the str method displays the correct information 
        when the date created is within ten years ago.
        """
        # Act and Assert:
        self.investment_account = InvestmentAccount(709, 9710, 450, date(2018, 7, 9), 2)

        self.assertEqual(f"Account Number: 709 Balance: $450.00"
                         f"\nDate Created: 2018-07-09 Management Fee: $2.00 "
                         f"Account Type: Investment", str(self.investment_account))