import pandas as pd
import numpy as np

df = pd.read_csv("data.csv")
print(df.head())
print()
print(df.tail())


# Types of missing data:
# MCAR: Missing Completely At Random
# MAR: Missing At Random
# MNAR: Missing Not At Random

# way to see data
print("isnull".upper())
print(df.isnull())
print("isna".upper())
print(df.isna())
print("notnull".upper())
print(df.notnull())
print("notna".upper())
print(df.notna())
print("info".upper())
print(df.info())

# using series
print()
s = pd.Series([10, np.nan, 30, None, 50])

mask = s.isnull()
print(mask)


# handling missing data: removal methods

"""
axis
how
thresh
subset
inplace
"""
print("\nHandling Missing values", end="\n")
# Remove rows with any missing values
data_clean1 = df.dropna()

# Remove columns with any missing values
data_clean2 = df.dropna(axis=1)

# Keep rows with at least 2 non-NA values
data_clean3 = df.dropna(thresh=2)

# Remove rows where columns 'a' or 'b' have missing values
data_clean4 = df.dropna(subset=["a", "b"])

print("data_clean1\n:", data_clean1)
print("data_clean2\n:", data_clean2)
print("data_clean3\n:", data_clean3)
print("data_clean4\n:", data_clean4)


# imputation methods --> filling values

filledData = df.fillna(0)
# filledData = df.fillna()
filledData2 = df.fillna(method="ffill")
filledData3 = df.fillna(method="bfill")
filledData4 = df.interpolate()
print(filledData)
print(filledData2)
print(filledData3)
print(filledData4)
