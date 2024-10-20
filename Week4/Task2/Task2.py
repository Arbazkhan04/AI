import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

#generating number of rows
num_of_rows = 500

#generating same random numbers
np.random.seed(10)

#generating random data
product = np.random.choice(["Apple", "Mango", "Peach", "Banana", "Pear", "Gava", "Melon", "Plum", "Apricot", "Water Melon"], size=num_of_rows)
price = np.random.randint(10,1000, size=num_of_rows)
quantity = np.random.randint(1,20, size = num_of_rows)
start_date = datetime.now() - timedelta(days=365)
date = [start_date + timedelta(days=np.random.randint(0, 365)) for _ in range(num_of_rows)]

#generating dataset
sales_data = pd.DataFrame({
    'Order ID': [f'ORD{i}' for i in range(1, num_of_rows+1)],
    'Product': product,
    'Price ($)': price,
    'Quantity': quantity,
    'Date': date
})

#displays the dataset
print(sales_data.head(10))


#converting price and quantity to arrays
price_quantity_array = sales_data[['Price ($)', 'Quantity']].to_numpy()

#finding the total sales
total_sales = price_quantity_array[:,0] * price_quantity_array[:,1]

#displays the total sales
print(total_sales[:10])


#Calculating total sales and adding a new column
sales_data['Total Sales'] = sales_data['Price ($)'] * sales_data['Quantity']

#Filtering the data
filter_data = sales_data[sales_data['Total Sales'] > 100]

#displays the filtered data
print("\nSales greater than 100$: \n", filter_data[:5])


#grouping the dataset by product
total_quantity = sales_data.groupby('Product')['Quantity'].sum().reset_index()

#displays the total quantity sold for each product
print(total_quantity[:5])

# Create the scatter plot
plt.figure(figsize=(10,6))
plt.scatter(sales_data['Price ($)'], sales_data['Quantity'], alpha=0.5, color='b')
plt.title('Scatter Plot of Price vs Quantity Sold')
plt.xlabel('Price (in $)')
plt.ylabel('Quantity Sold')
plt.grid(True)
plt.show()

# Create the histogram
plt.figure(figsize=(10,6))
plt.hist(sales_data['Total Sales'], bins=20, color='green', edgecolor='black', alpha=0.7)
plt.title('Distribution of Total Sales Values')
plt.xlabel('Total Sales (in $)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
