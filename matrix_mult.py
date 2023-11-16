from matrix_class import *
import math

def matrix_ViableMult(MatA, MatB):
    match = (MatA.cols == MatB.rows)
    return match

def matrix_ViableAdd(MatA, MatB):
    match = (MatA.cols == MatB.cols and MatA.rows == MatB.rows)
    return match

def matrix_2k(Mat):
    while not math.log(Mat.rows, 2).is_integer():
        # need to make an append column method
        Mat.appendZeroRow()
    while not math.log(Mat.cols, 2).is_integer():
        Mat.appendZeroCol()

def matrix_Addition(MatA, MatB):
    if not matrix_ViableAdd(MatA, MatB):
        raise ValueError("Matrix A and Matrix B are not the same dimensions")
        return
    
    dim = MatA.rows
    m = matrix(dim, dim)
    for i in range(dim):
        for j in range(dim):
            m.matrix[i][j] = MatA.matrix[i][j] + MatB.matrix[i][j]

    return m

def matrix_Scale(scalar, Mat):
    m = matrix(Mat.rows, Mat.cols)
    for i in range(m.rows):
        for j in range(m.cols):
            m.matrix[i][j] = scalar * Mat.matrix[i][j]
    
    return m

def matrix_Naive(MatA, MatB):
    if not matrix_ViableMult(MatA, MatB):
        raise ValueError("Columns of Matrix A do not Match Columns of Matrix B!")
        return
    
    m = matrix(MatA.rows, MatB.cols)
    for i in range(MatA.rows):
        for j in range(MatB.cols):
            for k in range(m.rows):
                m.matrix[i][j] += MatA.matrix[i][k] * MatB.matrix[k][j]

    return m

def matrix_Strassen(MatA, MatB):
    if not matrix_ViableMult(MatA, MatB):
        raise ValueError("Columns of Matrix A do not Match Columns of Matrix B!")
        return
    
    if MatA.cols == 1:
        m = matrix(1, 1)
        m.matrix[0][0] = MatA.matrix[0][0] * MatB.matrix[0][0]
        return m
    
    matrix_2k(MatA)
    matrix_2k(MatB)
    m = matrix(MatA.rows, MatB.cols)
    split_index = MatA.cols/2

    m1 = matrix( split_index,  split_index)
    m2 = matrix( split_index,  split_index)
    m3 = matrix( split_index,  split_index)
    m4 = matrix( split_index,  split_index)
    m5 = matrix( split_index,  split_index)
    m6 = matrix( split_index,  split_index)
    m6 = matrix( split_index,  split_index)

    a11 = matrix( split_index,  split_index)
    a12 = matrix( split_index,  split_index)
    a21 = matrix( split_index,  split_index)
    a22 = matrix( split_index,  split_index)

    b11 = matrix( split_index,  split_index)
    b12 = matrix( split_index,  split_index)
    b21 = matrix( split_index,  split_index)
    b22 = matrix( split_index,  split_index)

    for i in range(split_index):
        for j in range(split_index):
            a11.matrix[i][j] = MatA.matrix[i][j]
            a12.matrix[i][j] = MatA.matrix[i][j+split_index]
            a21.matrix[i][j] = MatA.matrix[i+split_index][j]
            a22.matrix[i][j] = MatA.matrix[i+split_index][j+split_index]

            b11.matrix[i][j] = MatB.matrix[i][j]
            b12.matrix[i][j] = MatB.matrix[i][j+split_index]
            b21.matrix[i][j] = MatB.matrix[i+split_index][j]
            b22.matrix[i][j] = MatB.matrix[i+split_index][j+split_index]

    m1 = matrix_Strassen(matrix_Addition(a11, a22) , matrix_Addition(b11, b22))
    m2 = matrix_Strassen(matrix_Addition(a21, a22), b11)
    m3 = matrix_Strassen(a11, matrix_Addition(b12 , matrix_Scale(-1, b22)))


"""for i in range(MatA.rows):
        for j in range(MatB.cols):"""
    