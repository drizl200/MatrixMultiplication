from matrix_class import *
import math

def matrix_ViableMult(MatA, MatB):
    match = (MatA.cols == MatB.rows)
    return match

def matrix_2k(Mat):
    while not math.log(Mat.rows, 2).is_integer():
        # need to make an append column method
        Mat.appendZeroRow()
    while not math.log(Mat.cols, 2).is_integer():
        Mat.appendZeroCol()


def matrix_Naive(MatA, MatB):
    if not matrix_ViableMult(MatA, MatB):
        raise ValueError("Columns of Matrix A do not Match Columns of Matrix B!")
        return
    
    m1 = matrix(MatA.rows, MatB.cols)
    for i in range(MatA.rows):
        for j in range(MatB.cols):
            for k in range(m1.rows):
                m1.matrix[i][j] += MatA.matrix[i][k] * MatB.matrix[k][j]

    return m1

def matrix_Strassen(MatA, MatB):
    if not matrix_ViableMult(MatA, MatB):
        raise ValueError("Columns of Matrix A do not Match Columns of Matrix B!")
        return
    
    m = matrix(MatA.rows, MatB.cols)
    m1 = matrix(m.rows/2, m.cols/2)
    m2 = matrix(m.rows/2, m.cols/2)
    m3 = matrix(m.rows/2, m.cols/2)
    m4 = matrix(m.rows/2, m.cols/2)
    m5 = matrix(m.rows/2, m.cols/2)
    m6 = matrix(m.rows/2, m.cols/2)
    m6 = matrix(m.rows/2, m.cols/2)

    a11 = matrix(MatA.rows/2, MatA.cols/2)
    a12 = matrix(MatA.rows/2, MatA.cols/2)
    a21 = matrix(MatA.rows/2, MatA.cols/2)
    a22 = matrix(MatA.rows/2, MatA.cols/2)

    b11 = matrix(MatB.rows/2, MatB.cols/2)
    b12 = matrix(MatB.rows/2, MatB.cols/2)
    b21 = matrix(MatB.rows/2, MatB.cols/2)
    b22 = matrix(MatB.rows/2, MatB.cols/2)

    matrix_2k(MatA)
    matrix_2k(MatB)

"""for i in range(MatA.rows):
        for j in range(MatB.cols):"""
    