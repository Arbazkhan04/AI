import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split

# Setting random seed for reproducibility
np.random.seed(0)  
n = 1000

# Columns: Creating synthetic customer data
customer_id = np.arange(1, n + 1)
age = np.random.randint(18, 70, n)  
annual_income = np.random.randint(20000, 120000, n)
gender = np.random.choice(['Male', 'Female'], n)
purchased = np.random.choice([0, 1], n) 

# Creating a DataFrame
df = pd.DataFrame({
    'CustomerID': customer_id,
    'Age': age,
    'Annual Income': annual_income,
    'Gender': gender,
    'Purchased': purchased
})

# Save the data to a CSV file
df.to_csv('customer_data.csv', index=False)

# Print the first 10 rows of the data
print(df.head(10))

# Step 1: Check for missing values
print(df.isnull().sum())  # No missing values in this dataset

# Step 2: Encoding categorical variables
label_encoder = LabelEncoder()
df['Gender'] = label_encoder.fit_transform(df['Gender'])  # Encoding Gender
print(df.head(10))

# Step 3: Feature Scaling
# Scaling the Age and Annual Income columns using MinMaxScaler
scaler = MinMaxScaler()
df[['Age', 'Annual Income']] = scaler.fit_transform(df[['Age', 'Annual Income']])
print(df.head(10))

# Step 4: Data Visualization

# Histogram for Age distribution
plt.hist(df['Age'], bins=10, color='blue', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

# Scatter plot for Age vs Annual Income
plt.scatter(df['Age'], df['Annual Income'], color='red')
plt.title('Age vs Annual Income')
plt.xlabel('Age')
plt.ylabel('Annual Income')
plt.show()

# Step 5: Correlation Analysis
# Calculating correlation between Age, Annual Income, and Purchased
correlation_matrix = df[['Age', 'Annual Income', 'Purchased']].corr()
print(correlation_matrix)

# Step 6: Feature Engineering
# Creating a new feature: Income per Age
df['Income per Age'] = df['Annual Income'] / df['Age']
print(df.head(10))

# Step 7: Prepare Data for Modeling
# Dropping the CustomerID column as it is irrelevant for prediction
df.drop('CustomerID', axis=1, inplace=True)
print(df.head(10))

# Step 8: Split the data into training and testing sets
X = df.drop('Purchased', axis=1)
y = df['Purchased']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Printing the shapes of the training and testing sets
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)
