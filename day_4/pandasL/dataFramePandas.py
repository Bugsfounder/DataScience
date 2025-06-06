import pandas as pd


# creating data from via dictionary
data = {
    "Name": ["Alice", "bob", "Charlie", "diana"],
    "age": [25, 30, 35, 28],
    "city": ["NYC", "UA", "Chicago", "India"],
    "salary": [50000, 60000, 70000, 80000],
}


df = pd.DataFrame(data)
print(df)

# creating dataframe via list of dictionary
data_list = [
    {"name": "Alice", "age": 25, "city": "NIC"},
    {"name": "manisha", "age": 17, "city": "muzaffarpur"},
]

print()
df = pd.DataFrame(data_list)
print(df)

df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})

print("TODO")
print("H: ", df.shape)
print("H: ", df.size)
print("H: ", df["A"])
print("H: ", df.iloc[0])
print("H: ", df.describe())
