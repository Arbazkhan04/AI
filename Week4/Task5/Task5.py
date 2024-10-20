import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Generating the number of rows
num_of_rows = 1000

# Generating same random data
np.random.seed(100)

# Generating data
start_date = datetime.now() - timedelta(days=365*2)
date = [start_date + timedelta(days=np.random.randint(0, 365*2)) for _ in range(num_of_rows)]
company = np.random.choice(["Toyota", "Honda", "Suzuki", "Kia", "Nissan"], num_of_rows)
open_price = np.random.randint(50, 500, num_of_rows)
close_price = np.random.randint(50, 500, num_of_rows)
volume_trade = np.random.randint(1000, 1000000, num_of_rows)

# Generating dataset
stock_data = pd.DataFrame({
    'Date': date,
    'Company': company,
    'Open Price': open_price,
    'Close Price': close_price,
    'Volume Traded': volume_trade
})

# Displays the dataset
print(stock_data.head())

# Calculating percentage change in Close Price
close_array = stock_data['Close Price'].to_numpy()
percentage_changes = np.diff(close_price) / close_price[:-1] * 100

# Adding percentage change to stock_data
stock_data['Percentage'] = np.append([0], percentage_changes)
stock_data.loc[stock_data['Percentage'] < 0, 'Percentage'] = 0
print(stock_data.head())

# Filtering the data based on percentage change
prev_percentage = stock_data['Percentage'].shift(1)
filter_data = stock_data[stock_data['Percentage'] > (prev_percentage + 2)]
print(filter_data.head())

# Grouping the data to get total volume traded by company
total_volume_traded = stock_data.groupby('Company')['Volume Traded'].sum().reset_index()
print(total_volume_traded)

# Plotting the Close Price trend over time for a particular company (e.g., "Toyota")
company_data = stock_data[stock_data['Company'] == 'Toyota']

plt.figure(figsize=(10, 6))
plt.plot(company_data['Date'], company_data['Close Price'], color='blue', label='Close Price')
plt.title('Close Price Trend Over Time for Toyota', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Close Price ($)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Calculating average percentage change by company
avg_percentage_change = stock_data.groupby('Company')['Percentage'].mean().reset_index()

# Plotting a bar chart to compare average percentage change in Close Price for different companies
plt.figure(figsize=(10, 6))
plt.bar(avg_percentage_change['Company'], avg_percentage_change['Percentage'], color=['orange', 'blue', 'green', 'red', 'purple'])
plt.title('Average Percentage Change in Close Price by Company', fontsize=16)
plt.xlabel('Company', fontsize=12)
plt.ylabel('Average Percentage Change (%)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()
