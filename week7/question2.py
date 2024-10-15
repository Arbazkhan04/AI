# Task 2: Classification Algorithms
# Question 3: Apply k-Nearest Neighbors (k-NN) for Classification
# - Train a k-NN model on the Iris dataset. - Test different values of k (e.g., 1
# to 15) and observe the impact on accuracy

import pandas as pd
from sklearn.datasets import load_iris 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

iris_df['target'] = iris.target
print(iris_df)




