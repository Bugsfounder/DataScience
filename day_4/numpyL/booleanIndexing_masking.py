import numpy as np

arr = np.array([1, 5, 10, 15, 20, 25, 30])

mask = arr > 15

print(mask)  # [False False False False  True  True  True]
