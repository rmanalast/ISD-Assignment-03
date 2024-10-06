"""
Description: A class to represent SavingsAccount objects.
Author: Raven Manalastas
the following command:
    python -m unittest tests/test_savings_account.py
"""
from datetime import date
from bank_account.savings_account import SavingsAccount
import unittest

class TestSavingsAccount(unittest.TestCase):
    """
    This class contains unit tests for the SavingsAccount class.
    """

    def setUp(self):
        self.savings_account = SavingsAccount(910, 1910, 575, date(2000, 7, 14), 100)

    def test_init_vaild_inputs_attributes_set(self):
        # Arrange:
        savings_account = SavingsAccount(910, 1910, 575, date(2000, 7, 14), 100)

        # Act and Assert:
        self.assertEqual(910, self.savings_account._BankAccount__account_number)
        self.assertEqual(1910, self.savings_account._BankAccount__client_number)
        self.assertEqual(575, self.savings_account._BankAccount__balance)

        # protected attributes
        self.assertEqual(date(2000, 7, 14), self.savings_account._date_created)

        # private attributes
        self.assertEqual(100, self.savings_account._SavingsAccount__minimum_balance)

    def test_init_minimum_balance_input_invalid_type(self):
        """
        Test that the minimum balance has a invalid type
        """
        # Act and Assert:
        self.savings_account = SavingsAccount(910, 1910, 575, date(2000, 7, 14), 
                                              "Invalid minimum balance")
        self.assertEqual(50, self.savings_account._SavingsAccount__minimum_balance)

    def test_service_charges_method_when_balance_greater_than_the_minimum_balance(self):
        """
        Test get_service_charges when balance is greater than minimum.
        """
        # Act and Assert:
        get_service_charges = self.savings_account.get_service_charges()

        self.assertEqual(0.50, get_service_charges)

    def test_service_charges_method_when_balance_equal_to_the_minimum_balance(self):
        """
        Test get_service_charges when balance equals minimum.
        """
        # Act and Assert:
        self.savings_account = SavingsAccount(910, 1910, 100, date(2000, 7, 14), 100)
        get_service_charges = self.savings_account.get_service_charges()

        self.assertEqual(0.50, get_service_charges)

    def test_service_charges_method_when_balance_less_than_the_minimum_balance(self):
        """
        Test get_service_charges when balance is less than minimum.
        """
        # Act and Assert:
        self.savings_account = SavingsAccount(910, 1910, 50, date(2000, 7, 14), 100)
        get_service_charges = self.savings_account.get_service_charges()

        self.assertEqual(1, get_service_charges)

    def test_str_method_returns_f_string(self):
        """
        Test str method returns formatted account info.
        """
        # Act and Assert:
        self.assertEqual(f"Account Number: 910 Balance: $575.00"
                         f"\nMinimum Balance: $100.00 Account Type: Savings",
                         str(self.savings_account))