import math

from dataclasses import dataclass


from HyperComplexSystems.quternion import Quaternion
from HyperComplexSystems.dualnumbers import DualNumber
from HyperComplexSystems.dual import Dual


@dataclass
class DualQuaternion(Dual):
    D0: Quaternion
    D1: Quaternion

    @staticmethod
    def __check_type(var):
        if not isinstance(var, float | int | DualQuaternion):
            raise TypeError(f'{var.__class__.__name__} doesn\'t support.')
        elif isinstance(var, float | int):
            return DualQuaternion(D0=Quaternion(var, 0.0, 0.0, 0.0), D1=Quaternion(var, 0.0, 0.0, 0.0))
        elif isinstance(var, DualQuaternion):
            return var

    @property
    def Real(self):
        return self.D0

    @property
    def Dual(self):
        return self.D1

    @property
    def DualQuaternion(self) -> list:
        return [self.D0.Quatenion, self.D1.Quatenion]

    @property
    def parameter(self) -> float:
        return sum([q0 * q1 for q0, q1 in zip(self.D0.Quatenion, self.D1.Quatenion)]) / self.D0.norm

    @property
    def dual_parameter(self) -> float:
        return self.D1.w / self.D0.w

    @property
    def mod(self) -> DualNumber:
        return DualNumber(a=self.D0.mod, b=self.D0 * self.parameter)

    @property
    def norm(self) -> DualNumber:
        return DualNumber(a=self.D0.norm, b=2 * self.parameter * self.D0.norm)

    def __add__(self, dn):
        return super().__add__(self.__check_type(dn))

    def __sub__(self, val):
        if isinstance(val, DualQuaternion):
            return DualQuaternion(D0=(self.D0 - val.D0), D1=(self.D1 - val.D1))
        elif isinstance(val, (float, int)):
            return DualQuaternion(D0=(self.D0 - val), D1=(self.D1 - val))
        else:
            msg = f'Type {type(val).__name__} is not supported for Dual Quaternion substraction\n'
            raise TypeError(msg)
    
    def __rsub__(self, val):
        if not isinstance(val, (float, int)):
            msg = f'Type {type(val).__name__} is not supported for Dual Quaternion substraction\n'
            raise TypeError(msg)

        return DualQuaternion(D0=(val - self.D0), D1=(val - self.D1))

    def __mul__(self, val):
        if isinstance(val, DualQuaternion):
            return DualQuaternion(D0=(self.D0 * val.D0), D1=(self.D0 * val.D1 + self.D1 * val.D0))
        elif isinstance(val, (float, int)):
            return DualQuaternion(D0=(self.D0 * val), D1=(self.D1 * val))
        else:
            msg = f'Type {type(val).__name__} is not supported for Dual Quaternion multiplication\n'
            raise TypeError(msg)

    def dot(self, dq):
        if not isinstance(dq, DualQuaternion):
            msg = f'Type {type(dq).__name__} is not supported for Dual Quaternion dot product\n'
            raise TypeError(msg)

        return DualQuaternion(D0=(self.D0.dot(dq.D0)), D1=(self.D1.dot(dq.D0) + self.D0.dot(dq.D1)))

    def cross(self, dq):
        if not isinstance(dq, DualQuaternion):
            msg = f'Type {type(dq).__name__} is not supported for Dual Quaternion cross product\n'
            raise TypeError(msg)

        return DualQuaternion(D0=(self.D0.cross(dq.D0)), D1=(self.D1.cross(dq.D0) + self.D1.cross(dq.D1)))

    def circle(self, dq):
        if not isinstance(dq, DualQuaternion):
            msg = f'Type {type(dq).__name__} is not supported for Dual Quaternion circle product\n'
            raise TypeError(msg)

        return DualQuaternion(D0=(self.D0.dot(dq.D0) + self.D1.dot(dq.D1)), D1=Quaternion(0.0, 0.0, 0.0, 0.0))

    @classmethod
    def quaternion_conjugate(cls, dq):
        if not isinstance(dq, DualQuaternion):
            msg = 'Parameter must be object of DualQuaternion type'
            raise TypeError(msg)
        
        return DualQuaternion(D0=dq.D0.conjugate(), D1=dq.D1.conjugate())

    @classmethod
    def dual_number_conjugate(cls, dq):
        if not isinstance(dq, DualQuaternion):
            msg = 'Parameter must be object of DualQuaternion type'
            raise TypeError(msg)
        
        return DualQuaternion(D0=dq.D0, D1=(-1) * dq.D1)

    @classmethod
    def conjugate(cls, dq):
        if not isinstance(dq, DualQuaternion):
            msg = 'Parameter must be object of DualQuaternion type'
            raise TypeError(msg)
        
        return DualQuaternion(D0=dq.D0.conjugate(), D1=Quaternion((-1) * dq.D1.w, *dq.D1.vector))

    @classmethod
    def inverse(self, dq):
        if not isinstance(dq, DualQuaternion):
            msg = 'Parameter must be object of DualQuaternion type'
            raise TypeError(msg)
        
     
