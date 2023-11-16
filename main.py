import numpy as np
import time
np.random.seed(1)

from matrix_class import *
from matrix_mult import *

if __name__ == "__main__":
    m1 = matrix(1000,1000)
    m2 = matrix(1000,1000)

    m1.set_RandomMatrix(1,100)
    m2.set_RandomMatrix(1,100)

    st = time.process_time()

    m3 = matrix_Naive(m1, m2)

    et = time.process_time()
    res = et - st
    print("------ Naive ------")
    print("CPU Execution time:", res, "seconds")

    st = time.process_time()

    m3 = matrix_Strassen(m1, m2)

    et = time.process_time()
    res = et - st
    print("------ Strassen ------")
    print("CPU Execution time:", res, "seconds")

def matrix_mult_test():
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
    