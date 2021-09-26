import matplotlib
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.preprocessing import StandardScaler

df = pd.read_excel('d:\set.xlsx', header=0)
df_1 = df.drop(['Персона'], axis=1)
X = df_1
X.head()
StandardScaler().fit_transform(X)
model = KMeans(n_clusters = 10)
model.fit(X)
X["cluster"] = model.fit_predict(X)
plt.scatter(X['Стаж вождения, лет'], X['Убыточность, %'], c = X['cluster'])
plt.scatter(X['Возраст, лет'], X['Убыточность, %'], c = X['cluster'])
plt.scatter(X['Уровень заработной платы, руб/год'], X['Убыточность, %'], c = X['cluster'])
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
model = KMeans(n_clusters = 2)
model.fit(X)
#X['cluster'] = model.fit_predict(X)
sns.boxplot (x = "cluster", y="Убыточность, %", data=X)
sns.boxplot (x = "cluster", y="Возраст, лет", data=X)
sns.boxplot (x = "cluster", y="Стаж вождения, лет", data=X)
sns.boxplot (x = "cluster", y="Уровень заработной платы, руб/год", data=X)

#Использовав метод локтя(график осыпи) хорошо видно,, что наилучшей градацией по признакам
#происходит при кол-ве кластеров равном 2.
# Построение дальнейших взаимозависимостей страхового случая, убыточности, и уровня заработной платы
# ЯВНО показывает, что наилучшим критерием служит УРОВЕНЬ ЗАРАБОТНОЙ ПЛАТЫ
# что в целом подтврждается логикой событийности - является случай мошенничеством или нет.

def pred_values(input_data):
    df = pd.read_excel('d:\set.xlsx', header=0)
    df_1 = df.drop(['Персона'], axis=1)
    X = df_1
    StandardScaler().fit_transform(X)
    model = KMeans(init="k-means++", n_clusters=2)
    model.fit(X)
    #X['cluster'] = model.fit_predict(X)
    X_test = pd.DataFrame(input_data)
    X_test = X_test.transpose()
    scaled_test = StandardScaler().fit_transform(X_test)
    predicted_label = model.predict(scaled_test)
    return predicted_label

df_test = [24, 6, 348, 139419]
print(pred_values(df_test))
