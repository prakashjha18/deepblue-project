# K-Means Clustering

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.externals import joblib

# Importing the dataset

dataset = pd.read_csv(r"C:\Users\Rajesh\.spyder-py3\predict queue wait time\pqtdoctor2.csv")
dataset=dataset.iloc[:,0:6]
datacor=dataset.corr()
dataset.corr()
X = dataset.iloc[:, 0:3].values
X6 =  dataset.iloc[:, 1].values

# y = dataset.iloc[:, 3].values

# Splitting the dataset into the Training set and Test set
"""from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)"""

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train.reshape(-1,1))"""

# Using the elbow method to find the optimal number of clusters
X = dataset.iloc[:, [1,4]].values
from sklearn.cluster import KMeans
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

# Fitting K-Means to the dataset
kmeans = KMeans(n_clusters = 4, init = 'k-means++', random_state = 42)
y_kmeans = kmeans.fit_predict(X)

# Visualising the clusters
plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s = 100, c = 'blue', label = 'Cluster 2')
plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s = 100, c = 'green', label = 'Cluster 3')
plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], s = 100, c = 'cyan', label = 'Cluster 4')
#plt.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4, 1], s = 100, c = 'magenta', label = 'Cluster 5')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroids')
plt.title('Clusters of patients')
plt.xlabel('age of patients')
plt.ylabel('consultancy time')
plt.legend()
plt.show()


X = dataset.iloc[:, 0:3].values
y = dataset.iloc[:, 4].values


from sklearn.model_selection import train_test_split
# Splitting the dataset into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

#sc_X = StandardScaler()
# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""

# Fitting Multiple Linear Regression to the Training set
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 3000, random_state = 0)
regressor.fit(X_train, y_train)


# Predicting the Test set results
y_pred = regressor.predict(X_test)

from sklearn.metrics import r2_score
cm = r2_score(y_test, y_pred)

y5=regressor.predict(X)

plt.scatter(X6, y, color = 'red')
plt.plot(X,regressor.predict(X), color = 'blue')
plt.title('Truth or Bluff (Random Forest Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

joblib.dump(regressor, 'randomfrest.pkl') 
  
# Load the model from the file 
#knn_from_joblib = joblib.load('randomfrest.pkl')  

pkl =  open("C:\\Users\\abc\\.spyder-py3\\predict queue wait time\\randomforest.pkl","wb")
joblib.dump(regressor,pkl)
pkl.close()
pklout =  open("C:\\Users\\abc\\.spyder-py3\\predict queue wait time\\randomforest.pkl","rb")
knn_from_joblib = joblib.load(pklout)
  
# Use the loaded model to make predictions 
knn_from_joblib.predict(X_test) 

ini_array = np.array([[1, 28, 1]])
str2 = knn_from_joblib.predict(ini_array) 
print(str2)














