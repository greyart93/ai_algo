import pandas as pd
df = pd.
read_json('https://gist.githubusercontent.com/greyart93/e5bb39da824130e46568f955f3e48c15/raw/6d33f966bdea711938c831d1a44334346f28737b/result2.json')
df


# handling missing values
df['GPA'] = df['GPA'].fillna(df['GPA'].mode(), limit=2)
df


# handling outlier
df['Z-score'] = np.abs((df['GPA'] - df['GPA'].mean()) / df['GPA'].std())
df = df[df['Z-score'] < 2]
df


df = df[['StudentID','GPA','Result']]
df


# grouping
df.groupby('Result')['GPA'].count()


# sorting
df.sort_values(by='GPA', ascending=False)


# filtering
df[(df['GPA'] > 2) & (df['Result'] == 'Pass')]
