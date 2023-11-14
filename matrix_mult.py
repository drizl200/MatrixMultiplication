from matrix_class import *

def col_match_rows(MatA, MatB):
    match = (MatA.cols == MatB.rows)
    return match
    

def matmult_Naive(MatA, MatB):
    if not col_match_rows(MatA, MatB):
        raise ValueError("Columns of Matrix A do not Match Columns of Matrix B!")
        return
    
    m1 = matrix(MatA.rows, MatB.cols)
    for i in range(MatA.rows):
        for j in range(MatB.cols):
            for k in range(m1.rows):
                m1.matrix[i][j] += MatA.matrix[i][k] * MatB.matrix[k][j]

    return m1