import numpy as np

def matrix_sum(x,y):
    a = np.array(x)
    b = np.array(y)
    return a+b

x = [[1,2,3,4],[1,2,3,4],[1,2,3,4]]
y = [[5,6,7,8],[5,6,7,8],[5,6,7,8]]
print(matrix_sum(x,y))