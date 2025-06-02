# MLModelsMCA
## How to start

```cmd
source env/bin/activate

jupyter-lab
```
# What is AI?
# What is ML


# Types of ML

## Linear Regression
Linear Regression is a statistical method used to model the relationship between a dependent variable (Y) and one or more independent variables (X) using a straight line:
Y=mX+b
where m is the slope, and b is the intercept. It predicts outcomes based on input data. 🚀

### Linear Regression: house price prediction
```py
# Linear Regression: house price prediction
from sklearn.linear_model import LinearRegression

x = [[1200,8], [1500, 9], [800, 5]]
y = [300000, 400000, 200000]

model = LinearRegression()
model.fit(x,y)

print(model.predict([[1400,8], [11000,3]]))
```
## Clustering: kmeansAlgo
```py
from sklearn.cluster import KMeans

x = [[20,200], [25, 25000],[ 40, 5000], [45,6000]]

model = KMeans(n_clusters=2)

model.fit(x)

print(model.labels_ )
```


