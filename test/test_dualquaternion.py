import os
import sys


IMPORTED_DIR = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    os.pardir
))
sys.path.append(IMPORTED_DIR)

from HyperComplexSystems.dualquaternion import DualQuaternion as DQ
from HyperComplexSystems.quternion import Quaternion as Q


if __name__ == "__main__":

    dq1 = DQ(D0=Q(1.0, 1.2, 1.1, 1.3), D1=Q(1.1, 1.2, 1.3, 0.5))
    dq2 = DQ(D0=Q(1.5, 1.3, 1.4, 1.6), D1=Q(1.7, 1.3, 1.0, 1.5))

    dq3 = dq1 + 1.5
    print(dq3)
