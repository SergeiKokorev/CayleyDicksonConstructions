from dataclasses import dataclass


from HyperComplexSystems.dual import Dual


@dataclass
class DualNumber(Dual):
    D0: int | float
    D1: int | float

    @property
    def mod(self):
        return abs(self.D0)

    def __str__(self):
        return f'{self.__class__.__name__} = {self.D0} + {self.D1}e'

    def __abs__(self) -> float:
        return abs(self.D0)
