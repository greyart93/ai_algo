import numpy as np
import pandas as pd


df = pd.read_csv('https://raw.githubusercontent.com/campusx-official/100-days-of-machine-learning/refs/heads/main/day24-standardization/Social_Network_Ads.csv')


df = df.iloc[:, 2:]


from sklearn.model_selection import train_test_split


X_train, X_test, y_train, y_test = train_test_split(df.drop('Purchased', axis=1), df['Purchased'], test_size=0.2, random_state=0)


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)


X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)


np.round(X_train_scaled.describe(), 1)


np.round(X_train.describe(), 1)


from sklearn.preprocessing import MinMaxScaler
minmax = MinMaxScaler()
minmax.fit(X_train)
X_train_minmax = minmax.transform(X_train)
X_test_minmax = minmax.transform(X_test)
X_train_minmax = pd.DataFrame(X_train_minmax, columns=X_train.columns)
X_test_minmax = pd.DataFrame(X_test_minmax, columns=X_test.columns)
X_train_minmax.describe()
