# Intermediate Software Development Automated Teller Project
This project will be developed over the course of several assignments.  Each 
assignment will build on the work done in the previous assignment(s).  Ultimately, 
an entire system will be created to manage bank transactions for clients who 
have one or more bank accounts.

## Author
Raven Manalastas

## Assignment
Assignment 1: Classes, Encapsulation and Unit Test Planning. 
This assignment will produce some foundational classes to be used in an overall system. 
Focusing on encapsulation through private attributes and public accessors/mutators, as covered in Module 01, 
and the classes will undergo detailed unit testing, including careful test planning.

Assignment 2: Applying Object-Oriented Design.
This Assignment is extending the BankAccount class from the pervious Assignment 1. 
The BankAccount class will serve as a base class for more specific subclasses. 
Each subclass will inherit the attributes and methods of the base class while adding its own specific features. 
Polymorphism will be used by letting each subclass give its own version of a method from the base class. 
Unit testing will focus on checking that polymorphism works as expected.

Assignment 3: Applying Design Patterns
This Assignment is continuing on from the pervious Assignments 1 and 2,
by fixing the current service charge calculation issues by using the Strategy Pattern to make the system more scalable. 
It also introduces the Observer Pattern, which notifies clients of large transactions or when their balance drops below a minimum value.

## Encapsulation
Encapsulation is a key concept in object-oriented programming. 
It combines data and methods to protect data from outside interference. 
In the BankAccount and Transaction classes, private data is hidden, and public methods like deposit and withdraw 
allow users to interact with the class without knowing the internal details. This makes the classes easy to use and maintain.

## Polymorphism
Polymorphism is the a key concept in the object-oriented programming(OOP).
it allows objects of different classes to be treated as objects of a common superclass.
In the BankAccount subclasses, polymorphism is achieved through method overriding, 
where the 'get_service_charges()' method is implemented differently in each subclass 
to provide a specific implementation for each account type.
This allows objects of different BankAccount subclasses to be treated as objects of a common superclass, 
providing increased flexibility, improved code reuse, and easier maintenance.

## Strategy Pattern
The Strategy pattern was used in this assignment to manage different service charge 
calculations for each account type, providing flexibility in how charges are applied. 
I created separate strategy classes for each account’s unique service charge formula and connected them to the get_service_charge method. 
This setup allows each account to automatically select the correct calculation. 
Additionally, this design makes it easy to add or update service charge strategies in the future without altering the main account classes.

## Observer Pattern
The Observer Pattern was used in this assignment to manage notifications for different types of BankAccounts. 
The Subject class handles adding, removing, and notifying observers through their update methods. 
I created the Client class, which inherits from the Observer superclass, to define how notifications are handled. 
This allows Client instances to observe multiple BankAccount types and receive updates when important events occur, 
like large transactions or low balances during deposits and withdrawals. 
This design makes it easy to add or change observers in the future without affecting the main BankAccount classes.