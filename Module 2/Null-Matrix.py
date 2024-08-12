import numpy as np

def null_mat(rows, cols):
    mat = []
    for i in range(rows):
        mat.append([])
        for _ in range(cols):
            mat[i].append(0)
    return np.array(mat)

matrix = null_mat(4, 4)
print(matrix)
