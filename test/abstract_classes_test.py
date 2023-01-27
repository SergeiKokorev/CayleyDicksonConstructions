import os
import sys


IMPORTED_DIR = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    os.pardir
))
sys.path.append(IMPORTED_DIR)

from HyperComplexSystems.dual import Dual



if __name__ == "__main__":

    dn1 = Dual(real=1.5, dual=2.0)
    dn2 = Dual(real=1.2, dual=2.2)

    print('*** Dual Numbers ***')
    print('dn1 = ', dn1)
    print('dn2 = ', dn2, end='\n\n')

    print('*** Additions ***')
    print('1.5 + dn1 = ', 1.5 + dn1)
    print('dn1 + dn2 = ', dn1 + dn2)
    print('dn1 + 1.5 = ', dn1 + 1.5, end='\n\n')

    print('*** Substraction ***')
    print('1.5 - dn1 = ', 1.5 - dn1)
    print('dn1 - dn2 = ', dn1 - dn2)
    print('dn1 - 1.5 = ', dn1 - 1.5, end='\n\n')




