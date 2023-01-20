import os
import sys


IMPORTED_DIR = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    os.pardir
))
sys.path.append(IMPORTED_DIR)


from HyperComplexSystems.dualnumbers import DualNumber


if __name__ == "__main__":

    dn1 = DualNumber(1.5, 1.2)
    dn2 = DualNumber(1.0, 2.5)

    print(f'First {dn1}')
    print(f'Second {dn2}')

    print(f'DualNumber additions : {dn1 + dn2}')
    print(f'DualNumber substruction : {dn1 - dn2}')
    print(f'DualNumber LSH scalar substraction : {dn1 - 2.5}')
    print(f'DualNumber RHS scalar substraction : {2.5 - dn1}')
    print(f'DualNumber division : {dn1 / dn2}')
    print(f'DualNumber LHS scalar division : {dn1 / 2.5}')
    print(f'DualNumber RHS scalar division : {2.5 / dn1}')
    print(f'DualNumber absolute value : {abs(dn1)}')
    print(f'DualNumber module : {dn1.module}')
