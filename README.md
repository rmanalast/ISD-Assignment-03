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