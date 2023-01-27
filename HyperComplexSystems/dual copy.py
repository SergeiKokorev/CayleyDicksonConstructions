from dataclasses import dataclass
from abc import ABCMeta


@dataclass
class Dual(metaclass=ABCMeta):
    D0: object
    D1: object

    @property
    def Real(self):
        return self.D0

    @property
    def Dual(self):
        return self.D1

    def __add__(self, dn):
        return Dual(D0=self.D0 + dn.D0, D1=self.D1 + dn.D1)

    def __sub__(self, dn):
        dn = self.__check_type(dn)
        return Dual(D0=self.D0 - dn.D0, D1=self.D1 - dn.D1)

    def __rsub__(self, dn):
        dn = self.__check_type(dn)
        return Dual(dn.D0 - self.D0, dn.D1 - self.D1)

    def __mul__(self, dn):
        dn = self.__check_type(dn)
        return Dual(self.D0 * dn.D0, (self.D0 * dn.D1 + self.D1 * dn.D0))

    def __truediv__(self, dn):
        dn = self.__check_type(dn)
        return Dual(self.D0 / dn.D0, (self.D1 * dn.D0 - self.D0 * dn.D1) / dn.D0 ** 2)

    def __rtruediv__(self, dn):
        dn = self.__check_type(dn)
        return Dual(dn.D0 / self.D0, (dn.D1 * self.D0 - dn.D0 * self.D1) / self.D0 ** 2)

    def __str__(self):
        return f'Real part: {self.D0}\nDual part: {self.D1}'