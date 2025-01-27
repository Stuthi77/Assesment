# -*- coding: utf-8 -*-
"""lvadsusr80_stuthi_lab2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1g2I0G316JrUCGEO1IrsmVUOglerSzBS3
"""

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
df=pd.read_csv("/content/Mall_Customers.csv")
df

from matplotlib import pyplot as plt
df['Age'].plot(kind='hist', bins=20, title='Age')
plt.gca().spines[['top', 'right',]].set_visible(False)

from matplotlib import pyplot as plt
df['Annual Income (k$)'].plot(kind='hist', bins=20, title='Annual Income (k$)')
plt.gca().spines[['top', 'right',]].set_visible(False)

"""#data Exploration And Preprocessing"""

df.info()

df=df.dropna()
df

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X = df[['CustomerID','Gender','Age','Annual Income','Spending Score']]
x[:, 1] = scaler.fit_transform(x_train[:, 1].reshape(-1, 1)).flatten()
X[:, 1] = scaler.transform(x_test[:, 1].reshape(-1, 1)).flatten()

"""#Optimal number of cluster"""

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs


X, _ = df['Annual Income'](n_samples=300, centers=4, cluster_std=0.60, random_state=0)


wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)


plt.plot(range(1, 11), wcss, marker='o')
plt.title('Elbow Method')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('WCSS')
plt.xticks(range(1, 11))
plt.grid(True)
plt.show()

"""#Clustering Algorithm Application"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
X[:, 1] = scaler.fit_transform(X[:, 1].reshape(-1, 1)).flatten()
X[:, 1] = scaler.transform(X[:, 1].reshape(-1, 1)).flatten()




k = 2


kmeans = KMeans(n_clusters=k, random_state=42)

kmeans.fit(X)


centroids = kmeans.cluster_centers_
labels = kmeans.labels_

plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', c='red', label='Centroids')
plt.title('Customer Segment')
plt.legend()
plt.show()

"""#Strategy Structure based on the Cluster Structures

Target Marketed Stregies- the frequency of high anual income  and  aged between 30 to 40 customer spending is more than all other customers
Female spending is more than male spending
"""