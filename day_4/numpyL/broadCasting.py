import numpy as np


arr = np.array([[1, 2, 3], [4, 5, 6]])
scaler = 10

result = arr + scaler
print(result)

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
arr_id = np.array([10, 20, 30])

result = arr_2d + arr_id
print(result)
