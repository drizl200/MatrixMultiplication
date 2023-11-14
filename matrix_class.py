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

    def set_SimpleMatrix(self, n, m):
        num = 1
        for i in range(self.rows):
            for j in range(len(self.cols)):
                self.matrix[i][j] = num
                num += 1
    
    def get_RandomMatrix(self, low, high):
        '''
        num = np.random.randint(low, high)
        
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j] = num
                num = np.random.randint(low, high)
        '''
         
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