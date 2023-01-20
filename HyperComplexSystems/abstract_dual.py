from abc import ABCMeta, abstractmethod


class AbstractDual(metaclass=ABCMeta):

    def __init__(self):
        pass

    @property
    @abstractmethod
    def Re(self):
        pass

    @property
    @abstractmethod
    def Im(self):
        pass

    @Re.setter
    @abstractmethod
    def Re(self, val):
        pass

    @Im.setter
    @abstractmethod
    def Im(self, val):
        pass

    def __add__(self):
        pass

    def __sub__(self):
        pass

    def __rsub__(self):
        pass

    def __mul__(self):
        pass

    def __rmul__(self):
        pass

