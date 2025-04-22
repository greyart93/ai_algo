import pandas as pd
from scipy import stats


from sklearn.datasets import load_iris
iris = load_iris()
data = pd.DataFrame(data= np.c_[iris['data'], iris['target']],
                    columns= iris['feature_names'] + ['target'])


setosa = data['sepal length (cm)'][data['target'] == 0]
versicolor = data['sepal length (cm)'][data['target'] == 1]


t_statistic, p_value = stats.ttest_ind(setosa, versicolor)




alpha = 0.05  # Significance level


print(f"T-statistic: {t_statistic}")
print(f"P-value: {p_value}")


if p_value < alpha:
   print("Reject the null hypothesis.")
   print("There is a statistically significant difference in sepal length between Iris-setosa and Iris-versicolor.")
else:
   print("Fail to reject the null hypothesis.")
   print("There is no statistically significant difference in sepal length between Iris-setosa and Iris-versicolor.")


data['petal_width_category'] = pd.cut(data['petal width (cm)'], bins=[0, 1, 10], labels=['small', 'large'])
contingency_table = pd.crosstab(data['target'], data['petal_width_category'])




chi2, p, dof, expected = stats.chi2_contingency(contingency_table)


print("\nChi-Square Test:")
print(f"Chi2 Statistic: {chi2}")
print(f"P-value: {p}")
print(f"Degrees of Freedom: {dof}")


if p < alpha:
   print("Reject the null hypothesis.")
   print("There is a statistically significant association between species and petal width category.")
else:
   print("Fail to reject the null hypothesis.")
   print("There is no statistically significant association between species and petal width category.")
