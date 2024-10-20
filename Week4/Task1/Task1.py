import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Initialize the number of days
num_of_days = 365

# Generate date range
np.random.seed(10)
dates = pd.date_range(start="2023-01-01", periods=num_of_days)

# Generate random data for weather conditions
temprature = np.random.uniform(10, 40, size=num_of_days)
humidity = np.random.uniform(30, 90, size=num_of_days)
wind_speed = np.random.uniform(0, 20, size=num_of_days)
weather_condition = np.random.choice(["sunny", "rainy", "cloudy"], size=num_of_days)

# Create a DataFrame
weather_data = pd.DataFrame({
    'Date': dates,
    'Temprature (°C)': temprature,
    'Humidity (%)': humidity,
    'Wind Speed (km/h)': wind_speed,
    'Weather Condition': weather_condition
})

# Display first few rows of the dataset
print(weather_data.head())

# Convert temperature column to numpy array
temp_array = weather_data['Temprature (°C)'].to_numpy()

# Calculate mean, median, and standard deviation
temp_mean = np.mean(temp_array)
temp_median = np.median(temp_array)
temp_standard_deviation = np.std(temp_array)

# Display statistics
print("Mean of the temperature: ", temp_mean)
print("Median of the temperature: ", temp_median)
print("Standard Deviation of the temperature: ", temp_standard_deviation)

# Filter the data for sunny days with temperature > 30°C
filter_temp = weather_data[(weather_data['Temprature (°C)'] > 30) & (weather_data['Weather Condition'] == 'sunny')]
total_days = len(filter_temp)

# Display number of filtered sunny days
print("Number of Sunny days: ", total_days)

# Group the data by weather condition and calculate average humidity
average_humidity = weather_data.groupby('Weather Condition')['Humidity (%)'].mean()
print("Average humidity by weather condition: \n", average_humidity)

# Plot the temperature variation over the year
plt.figure(figsize=(10, 6))
plt.plot(weather_data['Date'], weather_data['Temprature (°C)'], color='blue', label='Temperature (°C)')

# Adding labels and title
plt.title('Temperature Variation Over the Year', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Temperature (°C)', fontsize=12)
plt.grid(True)
plt.legend()
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()

# Create a bar plot for the number of days for each weather condition
weather_condition_counts = weather_data['Weather Condition'].value_counts()

# Plotting the bar chart
plt.figure(figsize=(8, 5))
weather_condition_counts.plot(kind='bar', color=['yellow', 'lightblue', 'gray'])

# Adding labels and title
plt.title('Number of Days for Each Weather Condition', fontsize=16)
plt.xlabel('Weather Condition', fontsize=12)
plt.ylabel('Number of Days', fontsize=12)
plt.grid(axis='y')
# Show the bar plot
plt.tight_layout()
plt.show()
