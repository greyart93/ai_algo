

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris


iris = load_iris()
data = pd.DataFrame(data= np.c_[iris['data'], iris['target']],
                    columns= iris['feature_names'] + ['target'])
X = data.drop('target', axis=1)


x = StandardScaler().fit_transform(X)


pca = PCA()
principalComponents = pca.fit_transform(x)


explained_variance_ratio = pca.explained_variance_ratio_
cumulative_variance_ratio = np.cumsum(explained_variance_ratio)


n_components_95 = np.argmax(cumulative_variance_ratio >= 0.95) + 1


print(f"Number of components explaining 95% variance: {n_components_95}")


plt.figure(figsize=(8, 6))
plt.bar(range(1, len(explained_variance_ratio) + 1), explained_variance_ratio, alpha=0.5, align='center', label='Individual explained variance')
plt.step(range(1, len(cumulative_variance_ratio) + 1), cumulative_variance_ratio, where='mid', label='Cumulative explained variance')
plt.ylabel('Explained variance ratio')
plt.xlabel('Principal component index')
plt.legend(loc='best')
plt.tight_layout()
plt.show()


pca = PCA(n_components=n_components_95)
principalComponents = pca.fit_transform(x)


principalDf = pd.DataFrame(data = principalComponents, columns = [f'PC{i+1}' for i in range(n_components_95)])


if n_components_95 == 2:
   plt.figure(figsize=(8,6))
   plt.scatter(principalDf['PC1'], principalDf['PC2'])
   plt.xlabel('Principal Component 1')
   plt.ylabel('Principal Component 2')
   plt.title('Data in Reduced Dimensional Space')
   plt.show()
elif n_components_95 > 2:
   print("Visualization for more than 2 components is not directly plotted.")
