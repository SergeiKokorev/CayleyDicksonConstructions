import sys
from const.files import IMPORTED_DIR
sys.path.append(IMPORTED_DIR)
print(IMPORTED_DIR)
from HyperComplexSystems.vector import *


class Vector:

    def __init__(self, vector: list=[0.0, 0.0, 0.0]):
        self.__vector = vector

    @property
    def vector(self) -> list:
        return self.__vector

    @vector.setter
    def vector(self, vector: list):
        if isinstance(vector, list):
            self.__vector = vector

    def __add__(self, val):
        res = self.__iterrator(val)
        if res:
            return Vector(vector=[a + b for a, b in zip(self.vector, res)])
        elif isinstance(val, (int, float)):
            return Vector(vector=[(a + val) for a in self.vector])
        else:
            raise TypeError(f'Wrong variable type {val.__class__.__name__}')

    def __sub__(self, val):
        res = self.__iterrator(val)
        if res:
            return Vector(vector=[a - b for a, b in zip(self.vector, res)])
        elif isinstance(val, (int, float)):
            return Vector(vector=[(a - val) for a in self.vector])
        else:
            raise TypeError(f'Wrong variable type {val.__class__.__name__}')

    def __rsub__(self, val):
        res = self.__iterrator(val)
        if res:
            return Vector(vector=[b - a for a, b in zip(self.vector, res)])
        elif isinstance(val, (int, float)):
            return Vector(vector=[(val - a) for a in self.vector])
        else:
            raise TypeError(f'Wrong variable type {val.__class__.__name__}')

    def __mul__(self, vector):
        return Vector(vector=[
            self.vector[1] * vector.vector[2] - self.vector[2] * vector.vector[1],
            self.vector[2] * vector.vector[0] - self.vector[0] * vector.vector[2],
            self.vector[0] * vector.vector[1] - self.vector[1] * vector.vector[0]
        ])
    
    def __str__(self):
        return f'[{self.vector[0]} {self.vector[1]} {self.vector[2]}]'

    def dot(self, vector) -> float:
        res = self.__iterrator(vector)
        return sum([a * b for a, b in zip(self.vector, res)])

    @property
    def mod(self) -> float:
        return (sum([a * a for a in self.vector])) ** 0.5

    @staticmethod
    def __iterrator(iterrator):
        if isinstance(iterrator, Vector):
            return iterrator.vector
        elif hasattr(iterrator, '__iter__') and not isinstance(iterrator, (dict, str)):
            return iterrator
        else:
            return None
