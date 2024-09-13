"""
Description: Unit tests for the Client class.
Author: ACE Faculty
Modified by: Raven Manalastas
Date: September 13, 2024
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_client.py
"""
import unittest
from client.client import Client
from email_validator import validate_email, EmailNotValidError

class TestClient(unittest.TestCase):

    def setUp(self):
        # setUp runs AUTOMATICALLY prior to every test
        # in the test class. Anything declared here with
        # self. will be accessible in the remaining tests.
        self.client = Client(7910, "Jorel", "Cruz", "jorelcruz@rrc.ca")

    def test_init_valid_inputs_attributes_set(self):
        # Arrange: None - (Preconditions)

        # Act (Method Inputs)
        client = Client(7910, "Jorel", "Cruz", "jorelcruz@rrc.ca")

        # Assert (Expected Value)
        self.assertEqual(7910, client._Client__client_number)
        self.assertEqual("Jorel", client._Client__first_name)
        self.assertEqual("Cruz", client._Client__last_name)
        self.assertEqual("jorelcruz@rrc.ca", client._Client__email_address)

    def test_init_invaild_client_raise_valueerror(self):
        # Arrange: none
        # Act and Assert
        with self.assertRaises(ValueError):
            client = Client("INVALID", "Jorel", "Cruz", "jorelcruz@rrc.ca")
    
    def test_init_blank_first_name_rasie_valueerror(self):
        # Arrange: none
        # Act and Assert
        with self.assertRaises(ValueError):
            client = Client(7910, "", "Cruz", "jorelcruz@rrc.ca")

    def test_init_blank_last_name_raise_valueerror(self):
        # Arrange: none
        # Act and Assert
        with self.assertRaises(ValueError):
            client = Client(7910, "Jorel", "", "jorelcruz@rrc.ca")

    def test_init_invalid_email_address_rasie_valueerror(self):
        # Arrange: none
        # Act and Assert
        with self.assertRaises(EmailNotValidError):
            client = Client(7910, "Jorel", "Cruz", "jorel_cruz@rrcca")

    def test_client_number_accessor_returns_client_number(self):
        # Arrange: Done in the setUp
        # Act and Assert
        self.assertEqual(7910, self.client.client_number)

    def test_first_name_accessor_returns_first_name(self):
        # Arrange: Done in the setUp
        # Act and Assert
        self.assertEqual("Jorel", self.client.first_name)

    def test_last_name_accessor_returns_last_name(self):
        # Arrange: Done in the setUp
        # Act and Assert
        self.assertEqual("Cruz", self.client.last_name)

    def test_email_address_accessor_returns_email_address(self):
        # Arrange: Done in the setUp
        # Act and Assert
        self.assertEqual("jorelcruz@rrc.ca", self.client.email_address)

    def test_str_returns_formatted_string(self):
        # Arrange
        # Remaining arrange is in setUp
        excepted = "Cruz, Jorel [7910] - jorelcruz@rrc.ca"

        # Act and Assert
        self.assertEqual(excepted, str(self.client))