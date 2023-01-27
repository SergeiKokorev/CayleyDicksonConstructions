from abc import ABCMeta, abstractmethod, abstractproperty, abstractclassmethod


class CayleyDicksonPrototype(metaclass=ABCMeta):
    def __init__(self, real: object, dual: object):
        self._D0: object = real
        self._D1: object = dual

    @abstractclassmethod
    def _build_dual(cls, number: object):
        if not isinstance(number, Dual | float | int):
            raise NotImplementedError(f'Unsupported type {type(number).__name__}')
        elif isinstance(number, float | int):
            return cls(real=number, dual=number)
        return number

    @abstractproperty
    def Real (self) -> object:
        return self.__D0
    
    @abstractproperty
    def Dual(self) -> object:
        return self.__D1

    @abstractmethod
    def __add__(self):
        pass

    @abstractmethod
    def __radd__(self):
        pass

    @abstractmethod
    def __sub__(self):
        pass

    @abstractmethod
    def __rsub__(self):
        pass

    @abstractmethod
    def __mul__(self):
        pass

    @abstractmethod
    def __rmul__(self):
        pass

    @abstractmethod
    def __truediv__(self):
        pass

    def __str__(self):
        return f'{round(self._D0, 4)} + ({round(self._D1, 4)})i'



class Dual(CayleyDicksonPrototype):
    def __init__(self, real: object, dual: object):
        super().__init__(real, dual)

    @classmethod
    def _build_dual(cls, number):
        return super()._build_dual(number)

    @property
    def Real(self):
        return self._D0
    
    @property
    def Dual(self):
        return self._D1

    def __add__(self, number: object) -> object:
        number = self._build_dual(number)
        return Dual(real=self.Real + number.Real, dual=self.Dual + number.Dual)

    def __radd__(self, number: object) -> object:
        number = self._build_dual(number)
        return Dual(real=number.Real + self.Real, dual=number.Dual + self.Dual)

    def __sub__(self, number: object) -> object:
        number = self._build_dual(number)
        return Dual(real=self.Real - number.Real, dual=self.Dual - number.Dual)

    def __rsub__(self, number: object) -> object:
        number = self.build_dual(number)
        return Dual(real=number.Real - self.Real, dual=number.Dual - self.Dual)

    def __mul__(self, number: object) -> object:
        number = self._build_dual(number)
        return Dual(real=self.Real * number.Real, dual=self.Dual * number.Dual)

    def __rmul__(self, number: object) -> object:
        number = self._build_dual(number)
        return Dual(real=self.Real * number.Real, dual=self.Dual)

    def __truediv__(self, number: object) -> object:
        number = self._build_dual(number)
        return None
