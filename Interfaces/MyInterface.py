from abc import ABCMeta, abstractmethod, abstractproperty


class MyInterface(metaclass=ABCMeta):

    @abstractmethod
    def do_something(self, value):
        """Required method"""

    def some_property(self):
        """Required property"""


class MyImplementation(MyInterface):

    def __init__(self, value=None):
        self._myprop = value

    def do_something(self, value):
        """Implementation of do_something method"""
        self._myprop *= 2 + value

    @property
    def some_property(self):
        return self._myprop

