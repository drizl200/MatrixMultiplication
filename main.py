import numpy as np

from matrix_class import *

if __name__ == "__main__":
    m1 = matrix(2,3)
    m2 = matrix(3,3)
    m2.set_RandomMatrix(1,20)

    m1.printMatrix()
    m2.printMatrix()