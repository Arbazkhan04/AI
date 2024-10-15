
import pandas as pd
from sklearn.datasets import load_iris, fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

iris = load_iris()
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_df['target'] = iris.target
print(iris_df)

california = fetch_california_housing()
california_df = pd.DataFrame(data=california.data, columns=california.feature_names)
california_df['target'] = california.target
print(california_df.head(10))

print(iris_df.isnull().sum())
print(california_df.isnull().sum())

sc = StandardScaler() 
iris_df = sc.fit_transform(iris_df)
california_df = sc.fit_transform(california_df)

iris_train, iris_test = train_test_split(iris_df, test_size=0.2)
california_train, california_test = train_test_split(california_df, test_size=0.2)
print("Train and test data:")
print(iris_train)
print("iris test")
print(iris_test)
print("california train")
print(california_train)
print("california test")
print(california_test)

