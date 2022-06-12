#Michael Thorman
#Lab 2
#9/24/21
#Computing C=C+A*B and analyze performance

import numpy as np
from timeit import default_timer as timer
from datetime import timedelta

def ijk(A, B, C):

    n = int(input("Please enter a value for N: "))



    A = np.random.normal(size=(n, n)).astype('float64')
    B = np.random.normal(size=(n, n)).astype('float64')
    C = np.zeros((n, n)).astype('float64')
    start = timer()
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k]*B[k][j]
    end = timer()
    print(timedelta(seconds=end-start))


A = []
B = []
C = []
ijk(A, B, C)




