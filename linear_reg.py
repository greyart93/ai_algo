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
print("Coefficients:", simple_regressor.coef_)
print("Intercept:", simple_regressor.intercept_)

X_multiple = data[['cgpa', 'package']] 
X_multiple_train, X_multiple_test, y_multiple_train, y_multiple_test = train_test_split(X_multiple, y, test_size=0.2, random_state=42)


multiple_regressor = LinearRegression()
multiple_regressor.fit(X_multiple_train, y_multiple_train)


y_multiple_pred = multiple_regressor.predict(X_multiple_test)


mse_multiple = mean_squared_error(y_multiple_test, y_multiple_pred)
r2_multiple = r2_score(y_multiple_test, y_multiple_pred)




print("\nMultiple Linear Regression:")
print("Coefficients:", multiple_regressor.coef_)
print("Intercept:", multiple_regressor.intercept_)
print("Mean Squared Error:", mse_multiple)
print("R-squared:", r2_multiple)
