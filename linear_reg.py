import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


data = pd.read_csv('https://raw.githubusercontent.com/campusx-official/100-days-of-machine-learning/refs/heads/main/day48-simple-linear-regression/placement.csv')


X = data[['cgpa']]
y = data['package']  


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


simple_regressor = LinearRegression()
simple_regressor.fit(X_train, y_train)


y_pred = simple_regressor.predict(X_test)


# Model evaluation
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)


print("Simple Linear Regression:")
print("Mean Squared Error:", mse)
print("R-squared:", r2)
