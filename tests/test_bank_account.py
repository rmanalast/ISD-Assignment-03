"""
Description: Unit tests for the BankAccount class.
Author: ACE Faculty
Modified by: Raven Manalastas
Date: September 13, 2024
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_bank_account.py
"""
import unittest
from bank_account.bank_account import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        # setUp runs AUTOMATICALLY prior to every test
        # in the test class. Anything declared here with
        # self. will be accessible in the remaining tests.
        self.bank_account = BankAccount(710, 7910, 2500.00)

    def test_init_valid_inputs_attributes_set(self):
        # Arrange: None - (Preconditions)

        # Act (Method Inputs)
        bank_account = BankAccount(710, 7910, 2500.00)

        # Assert (Expected Value)
        self.assertEqual(710, bank_account._BankAccount__account_number)
        self.assertEqual(7910, bank_account._BankAccount__client_number)
        self.assertEqual(2500.00, bank_account._BankAccount__balance)

    def test_init_non_numeric_account_number_raise_valueerror(self):
        # Arrange: none
        # Act and Assert
        with self.assertRaises(ValueError):
            bank_account = BankAccount("abc", 7910, 2500.00)
    
    def test_init_non_numeric_client_number_raise_valueerror(self):
        # Arrange: none
        # Act and Assert
        with self.assertRaises(ValueError):
            bank_account = BankAccount(710, "def", 2500.00)

    def test_init_non_numeric_balance_set_to_zero_rasie_valueerror(self):
        # Arrange: none
        # Act and Assert
        with self.assertRaises(ValueError):
            bank_account = BankAccount(710, 7910, "zero")

    def test_account_number_accessor_returns_account_number(self):
        # Arrange: Done in the setUp
        # Act and Assert
        self.assertEqual(710, self.bank_account.account_number)

    def test_client_number_accessor_returns_client_number(self):
        # Arrange: Done in the setUp
        # Act and Assert
        self.assertEqual(7910, self.bank_account.client_number)

    def test_balance_accessor_returns_balance(self):
        # Arrange: Done in the setUp
        # Act and Assert
        self.assertEqual(2500.00, round(self.bank_account.balance, 2))

    def test_update_balance_positive_amount_updates_balance(self):
        # Arrange: Done in the setUp
        # Act (Method Inputs)
        self.bank_account.update_balance(100)
        # Assert (Expected Value)
        self.assertEqual(2600.00, self.bank_account.balance)
    
    def test_update_balance_negative_amount_updates_balance(self):
        # Arrange: Done in the setUp
        # Act (Method Inputs)
        self.bank_account.update_balance(-100)
        # Assert (Expected Value)
        self.assertEqual(2400.00, self.bank_account.balance)

    def test_update_balance_non_numeric_amount_prints_error(self):
        # Arrange: Done in the setUp
        # Act (Method Inputs)
        self.bank_account.update_balance("zero")
        # Assert (Expected Value)
        self.assertEqual(2500.00, self.bank_account.balance)

    def test_deposit_method_when_valid_amount(self):
        # Arrange: Done in the setUp
        # Act (Method Inputs)
        self.bank_account.deposit(100)
        # Assert
        self.assertEqual(2600.00, self.bank_account.balance)

    def test_deposit_method_when_negative_amount(self):
        # Arrange: Done in the setUp
        # Act (Method Inputs)
        # Assert
        with self.assertRaises(ValueError):
            self.bank_account.deposit(-100)

    def test_withdraw_method_when_vaild_amount_taken_out(self):
        # Arrange: Done in the setUp
        # Act (Method Inputs)
        self.bank_account.withdraw(100)
        # Assert
        self.assertEqual(2400.00, self.bank_account.balance)

    def test_withdraw_method_when_negative_amount(self):
        # Arrange: Done in the setUp
        # Act (Method Inputs)
        # Assert
        with self.assertRaises(ValueError):
            self.bank_account.withdraw(-100)

    def test_withdraw_method_when_amount_exceeds(self):
        # Arrange: Done in the setUp
        # Act (Method Inputs)
        # Assert
        with self.assertRaises(ValueError):
            self.bank_account.withdraw(2600)

    def test_str_returns_string_representation(self):
        # Arrange: Done in the setUp
        # Act (Method Inputs)
        account_string = str(self.bank_account)
        # Assert (Expected Value)
        self.assertEqual(account_string, "Account Number: 710 Balance: $2,500.00")