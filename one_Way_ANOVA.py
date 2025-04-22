import pandas as pd
from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd


# Data
data = {'group': ['15mg', '15mg', '15mg', '15mg', '15mg', '15mg', '15mg',
                '30mg', '30mg', '30mg', '30mg', '30mg', '30mg', '30mg',
                '45mg', '45mg', '45mg', '45mg', '45mg', '45mg', '45mg'],
       'headache': [9, 8, 7, 8, 8, 9, 8,
                    7, 6, 6, 7, 8, 7, 6,
                    4, 3, 2, 3, 4, 3, 2]}
df = pd.DataFrame(data)


# Perform one-way ANOVA
fvalue, pvalue = stats.f_oneway(df['headache'][df['group'] == '15mg'],
                               df['headache'][df['group'] == '30mg'],
                               df['headache'][df['group'] == '45mg'])


print(f"F-statistic: {fvalue:.2f}")
print(f"P-value: {pvalue:.3f}")


# Critical value (you'll need to look this up in an F-distribution table)
# For alpha = 0.05, df_between = 2, df_within = 18
critical_value = 3.55


# Decision rule
if fvalue > critical_value:
   print("Reject H0: There is a significant difference between at least two groups.")
else:
   print("Fail to reject H0: There is no significant difference between the groups.")
