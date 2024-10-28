"""
Description: A class to manage Observer objects.
Author: Raven Manalastas
"""
from abc import ABC, abstractmethod

class Observer(ABC):
    """ 
    Methods:
        update (message: str): Called to notify the observer of a change.
    """

    @abstractmethod
    def __init__(self):
        """ 
        Initializes a newly created Observer abstract class.
        """
        pass

    @abstractmethod
    def update(self, message: str):
        """
        Notifies the observer with a message about a change.
        
        Args:
            message (str): The message or notification sent by the subject 
                           to inform the observer of a change or event.

        Returns:
            none: This method performs an action based on the message 
                  but does not return a value.
        """
        pass
