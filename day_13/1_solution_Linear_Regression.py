house_data = {
    "SquareFootage": [1500, 1800, 1200, 2000, None],
    "Bedrooms": [3, 4, None, 5, 2],
    "Bathrooms": [2, None, 1, 3, 1],
    "YearBuilt": [1995, 2005, 1980, None, 2010],
    "Price": [300000, 350000, 250000, 400000, 275000],
}

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# You have a dataset with missing values in some of the independent variables used for predicting house prices. How would you handle missing data before fitting a linear regression model?

df = pd.DataFrame((house_data))
df.ffill(inplace=True)

xt, xts, yt, yts = train_test_split(
    df["SquareFootage"], df["SquareFootage"], test_size=0.2, random_state=42
)
model = LinearRegression(max_tier=1000)
model.fit(xt, yt)


# model.predict(5000)
# Suppose you are building a linear regression model to predict employee salaries based on years of experience, education level, and job role. How would you determine which features are most influential in the prediction?
# employee_data = {
#     "YearsExperience": [5, 10, 2, 8, 3],
#     "EducationLevel": ["Bachelor's", "Master's", "PhD", "Bachelor's", "Master's"],
#     "JobRole": ["Data Analyst", "Manager", "Researcher", "Engineer", "Developer"],
#     "Salary": [70000, 100000, 85000, 90000, 75000],
# }
