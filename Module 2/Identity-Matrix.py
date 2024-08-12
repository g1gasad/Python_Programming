import numpy as np
# help(np.array)

def identity_matrix(n):
    mat = []
    for i in range(n):
        mat.append([])
        for j in range(n):
            if i==j:
                mat[i].append(1)
            else:
                mat[i].append(0)
    return np.array(mat)

dimension = int(input("Enter the dimensions for your identity square matrix: "))
my_mat = identity_matrix(dimension)
print(my_mat)

flatten = [i for sublist in my_mat for i in sublist]
print(flatten)