from sklearn.cluster import KMeans
import os
import matplotlib.pyplot as plt
import pandas as pd
dir = os.path.dirname(__file__)
datafile = os.path.join(dir, 'xx2020.csv')
dataset = pd.read_csv(datafile)
# 数据清洗
dataset.drop_duplicates()  # 去重，这个数据没必要
dataset.isnull().sum()  # 查看空值情况，应该没有空值，空值太多的列可以删除
print(dataset.isnull().sum())

L = dataset.iloc[:, 0].values
X = dataset.iloc[:, 1:39].values


# 查看某一列统计
dataset.describe()['专业概论与新生研讨']
print(dataset.describe()['专业概论与新生研讨'])


# Using the elbow method to find the optimal number of clusters
wcss = []
for i in range(1, 39):
    kmeans = KMeans(n_clusters=i, max_iter=300, n_init=10,
                    init='k-means++', random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 39), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

# 开始聚类
kmeans = KMeans(n_clusters=6, n_init=10, init='k-means++', random_state=0)
kmeans.fit_predict(X)
# print(L)
# print(kmeans.labels_)
df1 = pd.DataFrame(L)
# print(df1)
df2 = pd.DataFrame(kmeans.labels_)
# print(df2)
df3 = pd.concat([df1, df2], axis=1)
print(df3.values)
df3.to_csv(datafile+".clustered.csv")
