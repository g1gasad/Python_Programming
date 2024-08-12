import numpy as np
# help(np.array)

def create_matrix(rows, cols):
    mat = []
    for i in range(rows):
        mat.append([])
        for _ in range(cols):
            mat[i].append(np.random.randint(10))
    return np.array(mat)

my_mat = create_matrix(5, 4)
print(my_mat)

flatten = [i for sublist in my_mat for i in sublist]
print(flatten)