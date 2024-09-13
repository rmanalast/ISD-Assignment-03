"""
Description: A class to manage Client objects.
Author: Raven Manalastas
"""

from email_validator import validate_email, EmailNotValidError

class Client:
    """
    Attributes:
    __client_number (int): An integer value representing the client number.
    __first_name (str): A string value the client's first name.
    __last_name (str): A string value the client's last name.
    __email_address (str): A string value the client's email address.

    Methods:
    __init__(): Initializes the client.
    client_number(): Accessor for the client_number attribute.
    first_name(): Accessor for the first_name attribute.
    last_name(): Accessor for the last_name atrribute.
    email_address(): Acccessor for the email_address atrribute.
    __str__ (): Returns a string representation of the client object.
    """

    def __init__(self, client_number: int, first_name: str, last_name: str, email_address: str):
        """
        Initializes the class attributes with argument values.
        Args
            client_number (int): An integer value representing the client number.
            first_name (str): A string value the client's first name.
            last_name (str): A string value the client's last name.
            email_address (str): A string value the client's email address.

        Raises:
            ValueError:
                When the client number is invalid.
                When the first name is blank
                When the last name is blank.
                When the email address is invalid.
        """
        if isinstance(client_number, int):
            self.__client_number = client_number
        else:
            raise ValueError("Client number is invalid.")
        
        if len(first_name.strip()) == 0:
            raise ValueError("First name cannot be blank.")
        else:
            self.__first_name = first_name
        
        if len(last_name.strip()) == 0:
            self.__last_name = last_name
        else:
            raise ValueError("Last name cannot be blank.")
        
        #this try block validates the email argument, if it is valid, set the-
        #-email attribute to the email argument, if it hits an exception-
        #-print EmailNotValidError
        try:
            valid_email = validate_email(email_address, check_deliverability = False)
        except EmailNotValidError:
            raise EmailNotValidError
        self.__email_address = valid_email.normalized

    @property
    def client_number(self) -> int:
        """
        Accessor for the __client_number attribute.
        Returns:
            int - An integer value representing the client number.
        """
        return self.__client_number
    
    @property
    def first_name(self) -> str:
        """
        Accessor for the __first_name attribute.
        Returns:
            str - A string value the client's first name.
        """
        return self.__first_name

    @property
    def last_name(self) -> str:
        """
        Accessor for the __last_name attribute.
        Returns:
            str - A string value the client's last name.
        """
        return self.__last_name
    
    @property
    def email_address(self) -> str:
        """
        Accessor for the __email_address attribute.
        Returns:
            str - A string value the client's email address.
        """
        return self.__email_address
    
    def __str__(self) -> str:
        """
        Returns a string representation of the client object.
        """
        return f"{self.__last_name}, {self.__first_name} [{self.__client_number}] - {self.__email_address}"