from sklearn.preprocessing import OneHotEncoder, LabelEncoder
import pandas as pd

colors = pd.DataFrame(["red", "blue", "pink"])
labelEncoderObj = LabelEncoder().fit_transform(colors)
# print(labelEncoderObj)

# oneHotEncoderObj = OneHotEncoder().fit_transform(colors)
oneHotEncoderObj = OneHotEncoder().fit_transform(colors).toarray()
# print(oneHotEncoderObj.toarray())
# print(oneHotEncoderObj)


data = {
    "Name": ["Alice", "bob", "Charlie", "diana"],
    "age": [25, 30, 35, 28],
    "city": ["NYC", "UA", "Chicago", "India"],
    "salary": [50000, 60000, 70000, 80000],
}


df = pd.DataFrame(data)
l_encoder = LabelEncoder().fit_transform(df["Name"])
print(l_encoder)


# oh_encoder = OneHotEncoder().fit_transform(df["Name"]).toarray() # error
oh_encoder = OneHotEncoder().fit_transform(pd.DataFrame(df["Name"])).toarray()
print(oh_encoder)


print(pd.get_dummies(df))
