# Creating a DataFrame with missing values
data_missing = {'A': [1, 2, None, 4],
                'B': [5, 6, None, 8]}
df_missing = pd.DataFrame(data_missing)


# Mean imputation for column 'A'
df_missing['A'] = df_missing['A'].fillna(df_missing['A'].mean())


# Dropping rows with missing values in column 'B'
df_missing.dropna(subset=['B'], inplace=True)


# Handling Outliers
data_outliers = {'Values': [10, 12, 15, 11, 13, 100]}
df_outliers = pd.DataFrame(data_outliers)


import numpy as np
z = np.abs((df_outliers['Values'] - df_outliers['Values'].mean()) / df_outliers['Values'].std())


dfoutlierscleaned = df_outliers[z < 2] # removed the outlier
