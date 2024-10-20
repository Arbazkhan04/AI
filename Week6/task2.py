from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
import matplotlib.pyplot as plt

# Setting random seed for reproducibility
np.random.seed(0)

# Number of rows (employees)
n = 1500

# Step 1: Generate Dummy Data
# EmployeeID: A unique identifier for each employee
employee_id = np.arange(1, n + 1)

age = np.random.randint(22, 61, n)
years_of_experience = np.random.randint(1, 50, n)  # Allow some values over 40 for outliers

gender = np.random.choice(['Male', 'Female'], n)
performance_rating = np.random.randint(1, 6, n)

# Create a DataFrame
df = pd.DataFrame({
    'EmployeeID': employee_id,
    'Age': age,
    'Years of Experience': years_of_experience,
    'Gender': gender,
    'Performance Rating': performance_rating
})

# Print the first 10 rows of the generated data
print(df.head(10))
df.to_csv('employee_performance_data.csv', index=False)

# Check for missing values
print(df.isnull().sum())  # No missing values in this dataset

# Encoding categorical variables
label_encoder = LabelEncoder()
df['Gender'] = label_encoder.fit_transform(df['Gender'])
print(df.head(10))

# Detecting outliers using box plot
plt.boxplot(df['Years of Experience'])
plt.title('Years of Experience Box Plot')
plt.show()

# Removing outliers (values over 40)
df = df[df['Years of Experience'] <= 40]
print(df.head(10))  # Verify that outliers have been removed


# Scale the Age and Years of Experience columns using standardization
scaler = StandardScaler()
df[['Age', 'Years of Experience']] = scaler.fit_transform(df[['Age', 'Years of Experience']])
print(df.head(10))

# 2.8 Step 7: Data Visualization
# Task: Create a box plot for the Performance Rating to understand the distribution of ratings.
plt.boxplot(df['Performance Rating'])
plt.title('Performance Rating Box Plot')
plt.show()

#Task: Create a scatter plot to visualize the relationship between Years of
# Experience and Performance Rating.
plt.scatter(df['Years of Experience'], df['Performance Rating'])
plt.title('Years of Experience vs Performance Rating')
plt.xlabel('Years of Experience')
plt.ylabel('Performance Rating')
plt.show()


# Task: Calculate the correlation between Age, Years of Experience, and Performance Rating.
correlation_matrix = df[['Age', 'Years of Experience', 'Performance Rating']].corr()
print(correlation_matrix)


# Task: Create a new feature called Experience per Age by dividing Years of Experience by Age.
df['Experience per Age'] = df['Years of Experience'] / df['Age']
print(df.head(10))


# Task: Drop irrelevant columns, like EmployeeID, from the dataset. 
df = df.drop(columns=['EmployeeID'])
print(df.head(10))

# Task: Split the data into training and testing sets.
X = df.drop(columns=['Performance Rating'])
y = df['Performance Rating']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0) 
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape) #.shape returns the number of rows and columns in the dataset
