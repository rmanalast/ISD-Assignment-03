"""
Description: A client program written to verify correctness of 
the BankAccount sub classes.
Author: ACE Faculty
Edited by: Raven Manalastas
Date: October 06, 2024
"""

# 1.  Import all BankAccount types using the bank_account package
#     Import date from datetime
from bank_account import *
from datetime import date

# 2. Create an instance of a ChequingAccount with values of your 
# choice including a balance which is below the overdraft limit.
chequing_account = ChequingAccount(123, 987, -100.00, date(2008, 5, 15), 100.0, 0.05)

# 3. Print the ChequingAccount created in step 2.
# 3b. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
print(chequing_account)
chequing_service_charge = chequing_account.get_service_charges()
print(f"Calculated Service Charges: ${chequing_service_charge:.2f}")

# 4a. Use ChequingAccount instance created in step 2 to deposit 
# enough money into the chequing account to avoid overdraft fees.
# 4b. Print the ChequingAccount
# 4c. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
chequing_account.deposit(500)
print(chequing_account)
chequing_service_charge = chequing_account.get_service_charges()
print(f"Calculated Service Charges: ${chequing_service_charge:.2f}")

print("===================================================")
# 5. Create an instance of a SavingsAccount with values of your 
# choice including a balance which is above the minimum balance.
savings_account = SavingsAccount(150, 255, 250.00, date(2010, 12, 10), 100)

# 6. Print the SavingsAccount created in step 5.
# 6b. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.
print(savings_account)
print(savings_account.get_service_charges())


# 7a. Use this SavingsAccount instance created in step 5 to withdraw 
# enough money from the savings account to cause the balance to fall 
# below the minimum balance.
# 7b. Print the SavingsAccount.
# 7c. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.
savings_account.withdraw(100.0)
print(savings_account)
savings_service_charge = savings_account.get_service_charges()
print(f"Calculated Service Charges: ${savings_service_charge:.2f}")

print("===================================================")
# 8. Create an instance of an InvestmentAccount with values of your 
# choice including a date created within the last 10 years.
investment_account = InvestmentAccount(500, 425, 200.00, date(2022, 1, 29), 2)

# 9a. Print the InvestmentAccount created in step 8.
# 9b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 8.
print(investment_account)
investment_service_charge = investment_account.get_service_charges()
print(f"Calculated Service Charges: ${investment_service_charge:.2f}")

# 10. Create an instance of an InvestmentAccount with values of your 
# choice including a date created prior to 10 years ago.
old_investment_account = InvestmentAccount(100, 50, 2400.00, date(2002, 2, 10), 5)

# 11a. Print the InvestmentAccount created in step 10.
# 11b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 10.
print(old_investment_account)
old_investment_service_charge = old_investment_account.get_service_charges()
print(f"Calculated Service Charges: ${old_investment_service_charge:.2f}")

print("===================================================")

# 12. Update the balance of each account created in steps 2, 5, 8 and 10 
# by using the withdraw method of the superclass and withdrawing 
# the service charges determined by each instance invoking the 
# polymorphic get_service_charges method.
chequing_account.withdraw(chequing_service_charge)
savings_account.withdraw(savings_service_charge)
investment_account.withdraw(investment_service_charge)
old_investment_account.withdraw(old_investment_service_charge)

# 13. Print each of the bank account objects created in steps 2, 5, 8 and 10.
print(chequing_account)
print(savings_account)
print(investment_account)
print(old_investment_account)