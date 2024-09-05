import numpy as np

matrix = []
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of cols: "))

for i in range(rows):
    matrix.append([])
    for j in range(cols):
        value = input("Enter value: ")
        if value == "":
            value = None
        matrix[i].append(value)
arr1 = np.array(matrix)    
print(arr1)

for r in range(len(arr1)):
    for c in range(len(arr1[0])):
        print(arr1[r][c], end=" ")
    print()