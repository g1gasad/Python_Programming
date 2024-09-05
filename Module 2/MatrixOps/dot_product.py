import numpy as np
a = [[-2, -6, 1],      # [00, 01, 02]
     [4, 4, -3],       # [10, 11, 12]  
     [0, -4, 6]]       # [20, 21, 22]
b = [[0, 5, 0],
     [-2, 1, 2],      
     [3, 3, 0]]

new_mat = []
s = 0
i = 0
for j in range(len(a[i])):
    # x = a[i][j]
    for k in range(len(b)):
        x = a[i][k]
        y = b[k][j]
        print(x, y)
        m = x*y
        s += m