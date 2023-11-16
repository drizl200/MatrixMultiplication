import numpy as np
np.random.seed(1)

from matrix_class import *
from matrix_mult import *

if __name__ == "__main__":
    m1 = matrix(2,3)
    m2 = matrix(3,2)

    m1.set_RandomMatrix(1,10)
    m2.set_RandomMatrix(1,10)

    """m3stable = matrix_Naive(m1, m2)
    m3test = matrix_Strassen(m1, m2)"""
    
    m3stable = matrix_Naive(m1, m2)
    m3test = matrix_Strassen(m1, m2)

    print("Here are our two matrices: ")

    m1.printMatrix()
    m2.printMatrix()

    print("=========================")

    print("Output: ")

    m3stable.printMatrix()
    m3test.printMatrix()

    """m3stable.printMatrix()
    m3test.printMatrix()"""
    