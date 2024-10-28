"""
Description: A class to manage Subject objects.
Author: Raven Manalastas
"""
from abc import ABC, abstractmethod
from patterns.observer.observer import Observer

class Subject(ABC):
    """
    A class responsible for maintaining a list of its observers 
    and notifying them of state changes.

    Methods:
        attach(observer: Observer): Adds a new observer to the list.
        detach(observer: Observer): Removes an observer from the list.
        notify(message: str): Notifies all attached observers with a message.
    """

    def __init__(self):
        """
        Initializes a newly created Subject instance with an empty list of observers.
        """
        super().__init__()
        self._observers = []
    
    def attach(self, observer: Observer):
        """ 
        Adds a new observer to the list.

        Args:
            observer (Observer): The observer to be added.

        Returns:
            None: This method does not return a value.
        """
        self._observers.append(observer)

    def detach(self, observer: Observer):
        """ 
        Removes an observer from the list.

        Args:
            observer (Observer): The observer to be removed.

        Returns:
            None: This method does not return a value.
        """
        self._observers.remove(observer)

    def notify(self, message: str):
        """ 
        Notifies all attached observers with a message.

        Args:
            message (str): The message to be sent to the observers.

        Returns:
            None: This method does not return a value.
        """
        for observer in self._observers:
            observer.update(message)