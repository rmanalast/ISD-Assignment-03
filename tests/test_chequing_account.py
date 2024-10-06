"""
Description: A class to represent ChequingAccount objects.
Author: Raven Manalastas
the following command:
    python -m unittest tests/test_chequing_account.py
"""
from datetime import date
from bank_account.chequing_account import ChequingAccount
import unittest

class TestChequingAccount(unittest.TestCase):
    """
    This class contains unit tests for the ChequingAccount class.
    """
    
    def setUp(self):
        self.chequing_account = ChequingAccount(710, 7910, 2500.00, date(2024, 7, 10), 50, .10)

    def test_init_vaild_inputs_attributes_set(self):
        # Arrange:
        chequing_account = ChequingAccount(710, 7910, 2500.00, date(2024, 7, 10), 50, .10)

        # Act and Assert:
        self.assertEqual(710, self.chequing_account._BankAccount__account_number)
        self.assertEqual(7910, self.chequing_account._BankAccount__client_number)
        self.assertEqual(2500.00, self.chequing_account._BankAccount__balance)

        # protected attributes
        self.assertEqual(date(2024, 7, 10), self.chequing_account._date_created)

        # private attributes
        self.assertEqual(50, self.chequing_account._ChequingAccount__overdraft_limit)
        self.assertEqual(.10, self.chequing_account._ChequingAccount__overdraft_rate)

    def test_init_overdraft_limit_input_invalid_type(self):
        """
        Test that the overdraft_limit has a invalid type
        """
        # Act and Assert:
        self.chequing_account = ChequingAccount(710, 7910, 2500.00, date(2024, 7, 10), "invalid limit", .10)

        self.assertEqual(-100, self.chequing_account._ChequingAccount__overdraft_limit)

    def test_init_overdraft_rate_input_invalid_type(self):
        """
        Test that the overdraft_rate has a invalid type
        """
        # Act and Assert:
        self.chequing_account = ChequingAccount(710, 7910, 2500.00, date(2024, 7, 10), 50, "invalid rate")

        self.assertEqual(0.05, self.chequing_account._ChequingAccount__overdraft_rate)

    def test_init_date_created_input_invalid_type(self):
        """
        Test that the date_created has a invalid type
        """
        # Act and Assert:
        self.chequing_account = ChequingAccount(710, 7910, 2500.00, "invalid date", 50, .10)

        self.assertEqual(date.today(), self.chequing_account._date_created)

    def test_get_service_charges_method_balance_greater_than_overdraft_limit(self):
        """
        Test that the get_service_charges balance is greater than the overdraft_limit
        """
        # Act and Assert:
        get_service_charges = self.chequing_account.get_service_charges()

        self.assertEqual(0.50, get_service_charges)

    def test_get_service_charges_method_balance_less_than_overdraft_limit(self):
        """
        Test that the get_service_charges balance is less than the overdraft_limit
        """
        # Act and Assert:
        self.chequing_account = ChequingAccount(710, 7910, -300, date(2024, 7, 10), 50, .10)
        
        get_service_charges = self.chequing_account.get_service_charges()

        self.assertEqual(35.50, get_service_charges)

    def test_get_service_charges_method_balance_equal_than_overdraft_limit(self):
        """
        Test that the get_service_charges balance is equal to the overdraft_limit
        """
        # Act and Assert:
        self.chequing_account = ChequingAccount(710, 7910, 50, date(2024, 7, 10), 50, .10)

        get_service_charges = self.chequing_account.get_service_charges()

        self.assertEqual(0.50, get_service_charges)

    def test_str_method_returns_f_string(self):
        """
        Test that the __str__ method returns the correct string 
        representation of the ChequingAccount object.
        """
        excepted = (f"Account Number: 710 Balance: $2,500.00\n "
                    f"Overdraft Limit: $50.00 Overdraft Rate: 10.00% Account Type: Chequing")
        
        self.assertEqual(str(self.chequing_account), excepted)