import pandas as pd
import numpy as np


print("\nSERIES 1")
series1 = pd.Series([10, 20, 30, 40, 50])
print(series1)

print("\nSERIES 2")
series2 = pd.Series([10, 20, 30], index=["a", "b", "c"])

print(series2)

print("\nSERIES 3")
data_dict = {"apple": 5, "orange": 8}
series3 = pd.Series(data_dict)
print(series3)


print(series1.iloc[0])
print(series1.loc[0])
