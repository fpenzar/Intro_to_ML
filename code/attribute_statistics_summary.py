# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 13:10:48 2023

@author: evaka
"""

import numpy as np
import pandas as pd
from transform import *
import matplotlib.pyplot as plt

"""filename = '../Data/iris.csv'
df = pd.read_csv(filename)

raw_data = df.values  
cols = range(0, 4) 
X = raw_data[:, cols]
attributeNames = np.asarray(df.columns[cols])
classLabels = raw_data[:,-1] 
classNames = np.unique(classLabels)
classDict = dict(zip(classNames,range(len(classNames))))
y = np.array([classDict[cl] for cl in classLabels])
N, M = X.shape
C = len(classNames) """

print("|Attribute | empirical mean | std deviation | median | range |")
print("|:--- | :---: | :---: | :---: | :---: |")
for i in range (M):
    # Compute values
    if attribute_names[i] not in ["Continent", "Country"]:
        x = X[:,i]
        x= x.astype(float)
        mean_x = x.mean()

        std_x = x.std(ddof=1)
        median_x = np.median(x)
        range_x = x.max()-x.min()
    
        print("|"+ attribute_names[i]+ "| %.3f |%.3f |%.3f |%.3f |" % (mean_x, std_x, median_x, range_x))
    
cov_matrix = np.cov(X[:,1:M-6].astype(float), rowvar=False)

print("Covariance Matrix:")
print(cov_matrix)

plt.figure()
plt.imshow(cov_matrix, cmap='viridis', interpolation='nearest')
plt.title('Covariance Matrix')
plt.colorbar()
plt.xticks(np.arange(len(cov_matrix)), attribute_names[1:M-6],rotation=270)
plt.yticks(np.arange(len(cov_matrix)), attribute_names[1:M-6])
"""plt.xlabel('Variables')
plt.ylabel('Variables')"""
"""for i in range(len(cov_matrix)):
    for j in range(len(cov_matrix)):
        plt.text(j, i, '{:.2f}'.format(cov_matrix[i, j]),
                 ha='center', va='center', color='black', fontsize=12)"""

plt.show()


    
    
correlation_matrix = np.corrcoef(X[:,1:M-6].astype(float), rowvar=False)

# Print the correlation matrix
print("Correlation Matrix:")
print(correlation_matrix)

plt.figure()
plt.imshow(correlation_matrix, cmap='viridis', interpolation='nearest')
plt.title('Correlation Matrix')
plt.colorbar()
plt.xticks(np.arange(len(correlation_matrix)), attribute_names[1:M-6],rotation=270)
plt.yticks(np.arange(len(correlation_matrix)), attribute_names[1:M-6])
"""plt.xlabel('Variables')
plt.ylabel('Variables')"""
"""for i in range(len(correlation_matrix)):
    for j in range(len(correlation_matrix)):
        plt.text(j, i, '{:.2f}'.format(correlation_matrix[i, j]),
                 ha='center', va='center', color='black', fontsize=12)"""

plt.show()