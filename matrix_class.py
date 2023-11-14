import numpy as np
np.random.seed(27)

class matrix:
    def __init__(self, n, m): 
        self.matrix = self.get_SimpleMatrix(n,m)
        self.rows = n
        self.cols = m
 
    def get_SimpleMatrix(self, n, m):
        num = 1
        matrix = [[None for j in range(m)] for i in range(n)]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = num
                num += 1
        
        return matrix
    
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
    
    def printMatrix(self):
        for i in range(self.rows):
            matrixRow = str(self.matrix[i])
            print(matrixRow)