from dataclasses import dataclass


@dataclass
class DualNumber:
    a: int | float
    b: int | float

    @staticmethod
    def __check_type(var):
        if not isinstance(var, float | int | DualNumber):
            raise TypeError(f'{var.__class__.__name__} doesn\'t support.')
        elif isinstance(var, float | int):
            return DualNumber(var, 0)
        elif isinstance(var, DualNumber):
            return var

    @property
    def module(self):
        return abs(self.a)

    def __str__(self):
        return f'{self.__class__.__name__} = {self.a} + {self.b}e'

    def __add__(self, dn):
        dn = self.__check_type(dn)
        return DualNumber(self.a + dn.a, self.b + dn.b)

    def __sub__(self, dn):
        dn = self.__check_type(dn)
        return DualNumber(self.a - dn.a, self.b - dn.b)

    def __rsub__(self, dn):
        dn = self.__check_type(dn)
        return DualNumber(dn.a - self.a, dn.b - self.b)

    def __mul__(self, dn):
        dn = self.__check_type(dn)
        return DualNumber(self.a * dn.a, (self.a * dn.b + self.b * dn.a))

    def __truediv__(self, dn):
        dn = self.__check_type(dn)
        return DualNumber(self.a / dn.a, (self.b * dn.a - self.a * dn.b) / dn.a ** 2)

    def __rtruediv__(self, dn):
        dn = self.__check_type(dn)
        return DualNumber(dn.a / self.a, (dn.b * self.a - dn.a * self.b) / self.a ** 2)

    def __abs__(self) -> float:
        return abs(self.a)

