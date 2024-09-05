import numpy as np
import random

mat = np.array([[3, 3, 1], [7, 5, 1], [1, 0, 0]])

mat1 = []
for i in range(4):
    mat1.append([])
    for j in range(4):
        mat1[i].append(random.randint(0, 10))
    
print(np.array(mat1))

# print(mat1)

