import numpy as np
np.random.seed(27)

from matrix_class import *
from matrix_mult import *

if __name__ == "__main__":
    m1 = matrix(5,5)
    m2 = matrix(5,5)

    m1.set_RandomMatrix(1,10)
    m2.set_RandomMatrix(1,10)

    m1.printMatrix()
    m2.printMatrix()

    m3 = matrix_Naive(m1,m2)
    matrix_2k(m3)
    m3.printMatrix()

    
    """
    m1.set_IdentityMatrix()
    m2.set_RandomMatrix(1,20)
    m3 = matmult_Naive(m1, m2)
    m3.appendZeroCol()
    m3.appendZeroRow()

    m1.printMatrix()
    m2.printMatrix()
    m3.printMatrix()
    """