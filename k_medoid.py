# -*- coding: utf-8 -*-
"""k_medoid.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1r-005IT3SMsbG_3iuvWXhiuWzPhl9dFJ
"""

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
import os

#import country data file
df = pd.read_csv('Country-data.csv')

df.head(10)

df.info()

#scale the data
from sklearn.preprocessing import StandardScaler
df= df.iloc[:,1:]
sc = StandardScaler()
X = sc.fit_transform(df)
X

pip install scikit-learn-extra

from sklearn_extra.cluster import KMedoids

wcss = []
for i in range(1, 11):
    kms = KMedoids(n_clusters = i , random_state = 5)
    kms.fit(X)
    wcss.append(kms.inertia_)
wcss

plt.plot(range(1, 11), wcss)
plt.title('the Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.grid(True)
plt.show()

from sklearn.metrics import silhouette_score
range_n_clusters = [3]

for num_clusters in range_n_clusters:
    
    # intialise kmeans
    kmedoids = KMedoids(n_clusters=num_clusters, max_iter=50)
    kmedoids.fit(X)
    
    cluster_labels = kmedoids.labels_
    
    # silhouette score
    silhouette_avg = silhouette_score(X, cluster_labels)
    print("For n_clusters={0}, the silhouette score is {1}".format(num_clusters, silhouette_avg))

kmedoids = KMedoids(n_clusters = 3 , random_state = 5)
y_hc = kmedoids.fit_predict(X)
y_hc

df['Cluster']=y_hc

df['Cluster'].value_counts()

df_0=df[df['Cluster']==0]
df_0

df_1=df[df['Cluster']==1]
df_1

df_2=df[df['Cluster']==2]
df_2



plt.figure(figsize=[12,8])
sns.scatterplot(df.gdpp, df.income, palette='Set1')
plt.show()

