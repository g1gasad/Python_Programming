import array as arr

# INSERTION
# arr1 = arr.array(typecode, [initializers])
arr1 = arr.array('i', [10, 20, 30, 40, 50])
print(arr1)
arr1.insert(-1, 90)
print(arr1)

# DELETION
arr1.remove(40)
print(arr1)

# SEARCHING
print(arr1.index(50))

# UPDATE
arr1[2] = 80
print(arr1)