from matrix_class import *
import math

def matrix_ViableMult(MatA, MatB):
    match = (MatA.cols == MatB.rows)
    return match

def matrix_2k(MatM):
    m = matrix (MatM.rows, MatM.cols)
    m = MatM
    if m.rows == m.cols:
        while not math.log(m.rows, 2).is_integer():
            m.appendZeroRow()
        while not math.log(m.cols, 2).is_integer():
            m.appendZeroCol()
    elif m.rows > m.cols:
        while not math.log(m.rows, 2).is_integer():
            m.appendZeroRow()
        while m.rows > m.cols:
            m.appendZeroCol()
    elif m.rows < m.cols:
        while not math.log(m.cols, 2).is_integer():
            m.appendZeroCol()
        while m.rows < m.cols:
            m.appendZeroRow()

    return m

def matrix_KillZeros(MatM):
    m = matrix(MatM.rows, MatM.cols)
    m = MatM
    #remove zero columns
    for j in range(m.cols-1, 0, -1):
        is_zero_col = True
        for i in range(m.rows):
            if m.matrix[i][j] != 0:
                is_zero_col = False
        if is_zero_col:
            m.removeCol()

    #remove zero rows
    for i in range(m.rows -1, 0, -1):
        is_zero_row = True
        for j in range(m.cols):
            if m.matrix[i][j] != 0:
                is_zero_row = False
        if is_zero_row:
            m.removeRow()

    return m
            
def matrix_Naive(MatA, MatB):
    if not matrix_ViableMult(MatA, MatB):
        raise ValueError("The columns of Matrix A do not match rows of Matrix B!")
        return
    
    m = matrix(MatA.rows, MatB.cols)
    for i in range(m.rows):
        for j in range(m.cols):
            for k in range(MatA.cols):
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
    
    MatA = matrix_2k(MatA)
    MatB = matrix_2k(MatB)
    c = matrix(MatA.rows, MatB.cols)
    split_index = int(MatA.rows/2)

    m1 = matrix( split_index,  split_index)
    m2 = matrix( split_index,  split_index)
    m3 = matrix( split_index,  split_index)
    m4 = matrix( split_index,  split_index)
    m5 = matrix( split_index,  split_index)
    m6 = matrix( split_index,  split_index)
    m6 = matrix( split_index,  split_index)
    m7 = matrix( split_index,  split_index)

    a11 = matrix( split_index,  split_index)
    a12 = matrix( split_index,  split_index)
    a21 = matrix( split_index,  split_index)
    a22 = matrix( split_index,  split_index)

    b11 = matrix( split_index,  split_index)
    b12 = matrix( split_index,  split_index)
    b21 = matrix( split_index,  split_index)
    b22 = matrix( split_index,  split_index)

    c11 = matrix( split_index,  split_index)
    c12 = matrix( split_index,  split_index)
    c21 = matrix( split_index,  split_index)
    c22 = matrix( split_index,  split_index)

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

    m1 = matrix_Strassen((a11 + a22) , (b11 + b22))
    m2 = matrix_Strassen((a21 + a22), b11)
    m3 = matrix_Strassen(a11, (b12 + (b22 * -1)))
    m4 = matrix_Strassen(a22, (b21 + (b11 * -1)))
    m5 = matrix_Strassen((a11 + a12), b22)
    m6 = matrix_Strassen((a21 + (a11 * -1)), (b11 + b12))
    m7 = matrix_Strassen((a12 + (a22 * -1)), (b21 + b22))

    c11 = (m1 + m4 + (m5 * -1) + m7)
    c12 = (m3 + m5)
    c21 = (m2 + m4)
    c22 = (m1 + (m2 * -1) + m3 + m6)

    for i in range(split_index):
        for j in range(split_index):
            c.matrix[i][j] = c11.matrix[i][j]
            c.matrix[i][j+split_index] = c12.matrix[i][j]
            c.matrix[i+split_index][j] = c21.matrix[i][j]
            c.matrix[i+split_index][j+split_index] = c22.matrix[i][j]
            
    return c