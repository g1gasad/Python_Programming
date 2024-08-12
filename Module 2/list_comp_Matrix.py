import numpy as np

def matrix(rows, cols):
    matrix =  [[np.random.randint(10) for j in \
            range(cols)] for i in range(rows)]
    return matrix # np.array(matrix)

rows, cols = 3, 4
my_mat = matrix(rows, cols)

for r in range(rows):
    for c in range(cols):
        print(my_mat[r][c], end=" ")
    print()
    
# By default, print statement inserts a new line
# with the end parameter, we can choose the spacing