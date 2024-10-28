"""
Description: A client program written to verify implementation 
of the Observer Pattern.
Author: ACE Faculty
Edited by: Raven Manalastas
Date: October 27, 2024
"""

# 1.  Import all BankAccount types using the bank_account package
#     Import date
#     Import Client
from bank_account import *
from datetime import date
from client.client import Client

# 2. Create a Client object with data of your choice.
client = Client(7910, "Raven", "Manalastas", "rmanalastas@pixell-river.com")

# 3a. Create a ChequingAccount object with data of your choice, using the client_number 
# of the client created in step 2.
# 3b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in step 2.
chequing_client = ChequingAccount(123, 9876, 10000.00, date(2023, 10, 27), -100.00, 0.05 )
savings_client = SavingsAccount(456, 5432, 5700.00, date(2021, 4, 5), 60.00,)

# 4 The ChequingAccount and SavingsAccount objects are 'Subject' objects.
# The Client object is an 'Observer' object.  
# 4a.  Attach the Client object (created in step 1) to the ChequingAccount object (created in step 2).
# 4a.  Attach the Client object (created in step 1) to the SavingsAccount object (created in step 2).
chequing_client.attach(client)
savings_client.attach(client)

# 5a. Create a second Client object with data of your choice.
# 5b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in this step.
second_client = Client(1079, "Raven", "Manalastas", "rmanalastas@pixell-river.com")
second_savings_client = SavingsAccount(789, 1098, 1500.00, date(2021, 4, 5), 40.00)
second_savings_client.attach(second_client)

# 6. Use the ChequingAccount and SavingsAccount objects created 
# in steps 3 and 5 above to perform transactions (deposits and withdraws) 
# which would cause the Subject (BankAccount) to notify the Observer 
# (Client) as well as transactions that would not 
# cause the Subject to notify the Observer.  Ensure each 
# BankAccount object performs at least 3 transactions.
# REMINDER: the deposit() and withdraw() methods can raise exceptions
# ensure the methods are invoked using proper exception handling such 
# that any exception messages are printed to the console.
chequing_client.deposit(10000.00)
chequing_client.withdraw(1500.00)
chequing_client.deposit(500.00)

savings_client.deposit(10000.00) 
savings_client.withdraw(14999.00)
savings_client.deposit(500.00) 

second_savings_client.deposit(10000.00)
second_savings_client.withdraw(10999.00)
second_savings_client.deposit(500.00)

#All other test outputs beforehand is kept for logging.