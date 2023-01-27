import os
import sys


DIRECTORY = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    os.path.pardir
))
sys.path.append(DIRECTORY)

from HyperComplexSystems.vector import Vector as vct


if __name__ == "__main__":

    v1 = vct(1.0, 2.0, 3.0)
    v2 = vct(4.0, 5.0, 6.0)

    print('Vector 1', end='\t')
    print(v1)
    print('Vector 2', end='\t')
    print(v2)

    print(f'Addition : {v1 + v2}')
    print(f'Substraction : {v1 - v2}')
    print(f'Righthand substraction 5.0 - v1: {5.0 - v1}')
    print(f'Cross product : {v1 * v2}')
    print(f'Dot product : {v1.dot(v2)}')
    print(f'Module v1 : {v1.mod}')
