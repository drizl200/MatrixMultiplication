import numpy as np
import time
np.random.seed(int(time.time())) 

from matrix_class import *
from matrix_mult import *

DIM = 4
RANGE_LOW = -100
RANGE_HIGH = 100

def matrix_pair(_dim, range_low, range_high):
    m1 = matrix(_dim,_dim)
    m2 = matrix(_dim,_dim)

    m1.set_RandomMatrix(range_low, range_high)
    m2.set_RandomMatrix(range_low, range_high)
    return m1, m2
                                    
def naive_test():
    m1, m2 = matrix_pair(DIM, RANGE_LOW, RANGE_HIGH)                                            
    return time_test(matrix_Naive, m1, m2)

def strassen_test():
    m1, m2 = matrix_pair(DIM, RANGE_LOW, RANGE_HIGH)
    return time_test(matrix_Strassen, m1, m2)

def time_test(alg, MatA, MatB, algName = ""):
    st = time.process_time()

    m = alg(MatA, MatB)

    et = time.process_time()
    res = et - st
    if algName == "":
        return res
    else: 
        print("------ ", algName ," ------")
        print("CPU Execution time:", res, "seconds")
        return res

if __name__ == "__main__":
    data_naive = []
    data_strassen = []
    for i in range(1): 
        data_naive.append(naive_test())
        data_strassen.append(strassen_test())
        if i == 0:
            print("Starting point:")
            print(data_naive[i])
            print(data_strassen[i])

        if i == 14:
            print("half way: ", time.time())

    print(data_naive)
    print("naive alg average: ", np.mean(data_naive))
    print(data_strassen)
    print("strassen alg average: ", np.mean(data_strassen))