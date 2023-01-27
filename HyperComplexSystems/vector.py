import sys
from dataclasses import dataclass
from const.files import IMPORTED_DIR
sys.path.append(IMPORTED_DIR)
from HyperComplexSystems.vector import *


@dataclass
class Vector:

    x: float | int
    y: float | int
    z: float | int

    @property
    def vector(self) -> list:
        return [self.x, self.y, self.z]

    @vector.setter
    def vector(self, vector: list):
        if isinstance(vector, list):
            self.x = vector[0]
            self.y = vector[1]
            self.z = vector[2]

    def __add__(self, val):
        res = self.__iterrator(val)
        if res:
            return Vector(*[a + b for a, b in zip(self.vector, res)])
        elif isinstance(val, (int, float)):
            return Vector(*[(a + val) for a in self.vector])
        else:
            raise TypeError(f'Wrong variable type {val.__class__.__name__}')

    def __sub__(self, val):
        res = self.__iterrator(val)
        if res:
            return Vector(*[a - b for a, b in zip(self.vector, res)])
        elif isinstance(val, (int, float)):
            return Vector(*[(a - val) for a in self.vector])
        else:
            raise TypeError(f'Wrong variable type {val.__class__.__name__}')

    def __rsub__(self, val):
        res = self.__iterrator(val)
        if res:
            return Vector(*[b - a for a, b in zip(self.vector, res)])
        elif isinstance(val, (int, float)):
            return Vector(*[(val - a) for a in self.vector])
        else:
            raise TypeError(f'Wrong variable type {val.__class__.__name__}')

    def __mul__(self, val):
        if isinstance(val, Vector):
            return Vector(*[
                self.vector[1] * val.vector[2] - self.vector[2] * val.vector[1],
                self.vector[2] * val.vector[0] - self.vector[0] * val.vector[2],
                self.vector[0] * val.vector[1] - self.vector[1] * val.vector[0]
            ])
        elif isinstance(val, (float, int)):
            return Vector(*[v * val for v in self.vector])

    def __rmul__(self, val):
        if isinstance(val, (float, int)):
            return Vector(*[v * val for v in self.vector])
    
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
        elif isinstance(iterrator, list):
            return iterrator
        else:
            return None
