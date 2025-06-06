import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print("sum: ", np.sum(arr))
print("sum: ", np.sum(arr, axis=0))  # TODO: understand the working of axis
print("sum: ", np.sum(arr, axis=1))
print("max: ", np.max(arr))
print("min: ", np.min(arr))
print("mean: ", np.mean(arr))
print("std: ", np.std(arr))
