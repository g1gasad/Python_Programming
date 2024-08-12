import numpy as np

matrix = np.array([[3, 4, 2], [1, 7, 0], [8, 7, 2]])

print("old matrix:\n", matrix)

matrix[-1][-1] = 69
print("new matrix:\n", matrix)