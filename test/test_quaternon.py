import os
import sys


DIRECTORY = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    os.path.pardir
))
sys.path.append(DIRECTORY)

from HyperComplexSystems.quternion import Quaternion as Q


if __name__ == "__main__":

    q3 = Q(1.0, 1.2, 1.1, 1.3)
    q4 = Q(1.5, 1.2, 1.3, 1.2)

    q5 = q3 * q4
    q6 = 5.0 * q3
    q7 = q3 * 5.0
    qd = q3.dot(q4)
    qc = q3.cross(q4)

    print(qd)
    print(qc)

    q8 = Q.inverse(q7)
    print(q8)
