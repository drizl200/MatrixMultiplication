import numpy as np
np.random.seed(27)

class matrix:
    def __init__(self, n, m): 
        self.rows = n
        self.cols = m
        self.matrix = self.get_ZeroMatrix(n, m)
 
    def get_ZeroMatrix(self, n, m):
        z_matrix = [[0 for j in range(m)] for i in range(n)]
        return z_matrix

    def set_SimpleMatrix(self):
        num = 1
        for i in range(self.rows):
            for j in range(len(self.cols)):
                self.matrix[i][j] = num
                num += 1
         
    def set_RandomMatrix(self, low, high):
        num = np.random.randint(low, high)
        
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j] = num
                num = np.random.randint(low, high)

    def set_IdentityMatrix(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if i == j:
                    self.matrix[i][j] = 1
                else:
                    self.matrix[i][j] = 0
    
    def printMatrix(self):
        for i in range(self.rows):
            matrixRow = str(self.matrix[i])
            print(matrixRow)
        
        print("")

    def appendZeroCol(self):
        for i in range(0, self.rows):
            self.matrix[i].append(0)
        self.cols += 1

    def appendZeroRow(self):
        self.matrix.append([0 for j in range(self.cols)])
        self.rows += 1

    def matrix_ViableAdd(self, other_mat):
        match = (self.cols == other_mat.cols and self.rows == other_mat.rows)
        return match

    def __add__(self, other_mat):
        if not self.matrix_ViableAdd(other_mat):
            raise ValueError("Matrix A and Matrix B are not the same dimensions")
            return
        
        dim = self.rows
        m = matrix(dim, dim)
        for i in range(dim):
            for j in range(dim):
                m.matrix[i][j] = self.matrix[i][j] + other_mat.matrix[i][j]

        return m

    def __mul__(self, scalar):
        m = matrix(self.rows, self.cols)
        for i in range(m.rows):
            for j in range(m.cols):
                m.matrix[i][j] = scalar * self.matrix[i][j]
        
        return m