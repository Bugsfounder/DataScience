import numpy as np


# arithmetic operations on arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([2, 3, 4])

print(arr1 + arr2)  # both array has to be same shape
print(arr1 - arr2)  # both array has to be same shape
print(arr1 * arr2)  # both array has to be same shape
print(arr1 / arr2)  # both array has to be same shape


# scaler operation
arr = np.array([1, 2, 3, 4, 5])
print(f"Add 10: {arr+10}")
print(f"multiply by 3: {arr * 3}")
print(f"Square root: {np.sqrt(arr)}")
