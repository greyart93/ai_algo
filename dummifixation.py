import pandas as pd
import numpy as np


df = pd.read_csv('https://raw.githubusercontent.com/campusx-official/100-days-of-machine-learning/refs/heads/main/day26-ordinal-encoding/customer.csv')


df = df.iloc[:, 2:]
df.sample(5)


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df.drop(['purchased'], axis=1), df['purchased'], test_size=0.2)


from sklearn.preprocessing import OrdinalEncoder
oe = OrdinalEncoder(categories=[['Poor', 'Average', 'Good'], ['School', 'UG', 'PG']])


oe.fit(X_train)


X_train = oe.transform(X_train)
X_test = oe.transform(X_test)


X_train = pd.DataFrame(X_train, columns=['review', 'education'])
X_test = pd.DataFrame(X_test, columns=X_test.columns)


X_train.sample(5)
