import numpy as np

# array
arrId = np.array([1, 2, 3, 4, 5])
print(arrId)

# 2d array
arr2d = np.array([[1, 2, 3], [4, 5, 6]])


# array indexing
print(arrId[0])
print(arrId[1])
print(arrId[3])
print(arrId[-1])

# slicing
print(arrId[0:4])
print(arrId[::2])

print(arr2d[0][1:3])
print(arr2d[0][::-1])
