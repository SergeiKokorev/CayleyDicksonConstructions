import math


from dataclasses import dataclass
from HyperComplexSystems.vector import Vector


@dataclass
class Quaternion:
    w: float
    q1: float
    q2: float
    q3: float

    @property
    def Quatenion(self) -> list:
        return [self.w, self.q1, self.q2, self.q3]

    @property
    def Vector(self) -> Vector:
        return Vector(*[self.q1, self.q2, self.q3])

    @property
    def vector(self) -> list:
        return [self.q1, self.q2, self.q3]

    @property
    def mod(self) -> float: # Quaternion module
        return self.norm ** 0.5
    
    @property
    def norm(self) -> float: # Quaternion norm
        return self.w ** 2 + self.q1 ** 2 + self.q2 ** 2 + self.q3 ** 2

    @property
    def arg(self) -> float: # Quaternion argument
        math.acos(self.w / self.mod)

    # Quaternion algebra
    def __add__(self, val):
        if isinstance(val, Quaternion):
            return Quaternion(self.w + val.w, self.q1 + val.q1,
                              self.q2 + val.q2, self.q3 + val.q3)
        elif isinstance(val, float | int):
            return Quaternion(self.w + val, self.q1 + val,
                              self.q2 + val, self.q3 + val)
        else:
            msg = f"Unsupported type {type(val).__name__} for Quaternion addition\n"
            raise TypeError(msg)
    
    def __sub__(self, val):
        if isinstance(val, Quaternion):
            return Quaternion(self.w - val.w, self.q1 - val.q1,
                              self.q2 - val.q2, self.q3 - val.q3)
        elif isinstance(val, float | int):
            return Quaternion(self.w - val, self.q1 - val, self.q2 - val, self.q3 - val)
        else:
            msg = f"Unsupported type {type(val).__name__} for Quaternion substractoin\n"
            raise TypeError(msg)

    def __rsub__(self, val):
        if isinstance(val, Quaternion):
            return Quaternion(val.w - self.w, val.q1 - self.q1,
                              val.q2 - self.q2, val.q3 - self.q3)
        elif isinstance(val, float | int):
            return Quaternion(val - self.w, val - self.q1, val - self.q2, val - self.q3)
        else:
            msg = f"Unsupported type {type(val).__name__} for Quaternion substraction\n"
            raise TypeError(msg)

    def __mul__(self, val):
        if isinstance(val, float | int):
            return Quaternion(self.w * val, self.q1 * val, self.q2 * val, self.q3 * val)
        elif isinstance(val, Quaternion):
            return Quaternion(self.w * val.w - self.Vector.dot(val.Vector),
                *(self.w * val.Vector + val.w * self.Vector + self.Vector * val.Vector).vector)
        else:
            msg = f"Unsupported type {type(val).__name__} for Quaternion multiplication\n"
            raise TypeError(msg)

    def __rmul__(self, val):
        if isinstance(val, float | int):
            return Quaternion(self.w * val, self.q1 * val, self.q2 * val, self.q3 * val)
        else:
            msg = f"Unsupported type {type(val).__name__} for Quaternion multiplication\n"
            raise TypeError(msg)

    def __str__(self):
        return f'Quaternion:\n{round(self.w, 4)} + ({round(self.q1, 4)})i' \
            f' + ({round(self.q2, 4)})j + ({round(self.q3, 4)})k\n' \
            f'Module: {round(self.mod, 4)};\tNorm: {round(self.norm, 4)}'

    def cross(self, quaternion):
        if isinstance(quaternion, Quaternion):
            return Quaternion(0.0, *(self.w * quaternion.Vector + \
                quaternion.w * self.Vector + self.Vector * quaternion.Vector).vector)
        else:
            msg = f"Unsupported type {type(quaternion).__name__} for Quaternion vector multiplication\n"
            raise TypeError(msg)

    def dot(self, quaternion):
        if isinstance(quaternion, Quaternion):
            return Quaternion(self.w * quaternion.w - self.Vector.dot(quaternion.Vector),
                             0.0, 0.0, 0.0)
        else:
            msg = f"Unsupported type {type(quaternion).__name__} for Quaternion scalar multiplication\n"
            raise TypeError(msg)

    @classmethod
    def conjugate(cls, quaternion):
        return Quaternion(quaternion.w, -quaternion.q1, -quaternion.q2, -quaternion.q3)

    @classmethod
    def normalize(cls, quaternion):
        if isinstance(quaternion, Quaternion):
            mod = quaternion.mod
            w = quaternion.w / mod
            q1 = quaternion.q1 / mod
            q2 = quaternion.q2 / mod
            q3 = quaternion.q3 / mod
            return Quaternion(w, q1, q2, q3)
        else:
            raise TypeError(f"Wrong argument type: {type(quaternion).__name__}")

    @classmethod
    def inverse(cls, quaternion):
        return cls.conjugate(quaternion) * (1 / quaternion.norm)
