# Step 1: Let's load the data and take a look at the first few rows to understand what we're working with.
import pandas as pd
# Load the dataset
file_path = "PATH TO THE DATASET"
df = pd.read_csv(file_path)
# Display the first few rows of the dataset
df.head()

"""DATA SCIENCE AND ENGINEERING"""

# Hypothesis 1: Houses with a pool are more expensive on average than houses without a pool.

# Calculate the average price of houses with a pool
average_price_with_pool = df[df['hasPool'] == 1]['price'].mean()

# Calculate the average price of houses without a pool
average_price_without_pool = df[df['hasPool'] == 0]['price'].mean()

average_price_with_pool, average_price_without_pool

# Hypothesis 2: The newer the house, the higher the price.

# Create a scatter plot of the year a house was built ('made') vs the price of the house
plt.scatter(df['made'], df['price'])
plt.title('House Price vs Year Built')
plt.xlabel('Year Built')
plt.ylabel('Price')
plt.show()

# Hypothesis 3: The number of rooms in a house is positively correlated with the price of the house.

# Calculate the Pearson correlation coefficient between 'numberOfRooms' and 'price'
correlation = df['numberOfRooms'].corr(df['price'])

# Create a scatter plot of the number of rooms vs the price of the house
plt.scatter(df['numberOfRooms'], df['price'])
plt.title('House Price vs Number of Rooms')
plt.xlabel('Number of Rooms')
plt.ylabel('Price')
plt.show()

correlation

# Hypothesis 4: Houses classified as 'Luxury' have more floors on average than houses classified as 'Basic'.

# Calculate the average number of floors in 'Luxury' houses
average_floors_luxury = df[df['category'] == 'Luxury']['floors'].mean()

# Calculate the average number of floors in 'Basic' houses
average_floors_basic = df[df['category'] == 'Basic']['floors'].mean()

average_floors_luxury, average_floors_basic

"""Data engineering process (After cleaning and transformation)"""

# Time series analysis

import pandas as pd
import matplotlib.pyplot as plt

# Reload the dataset
df = pd.read_csv("/mnt/data/Paris Housing Luxury Classification.csv")

# Group by 'made' and calculate the average price for each year
time_series_data = df.groupby('made')['price'].mean()

# Plot the average price over the years to detect seasonality or trends
plt.figure(figsize=(12, 6))
time_series_data.plot()
plt.title('Average House Price Over Years')
plt.xlabel('Year')
plt.ylabel('Average Price')
plt.grid(True)
plt.show()

# Implement window-based features: Calculate a 3-year rolling average for demonstration purposes
time_series_data_rolling_avg = time_series_data.rolling(window=3).mean()

# Plot the rolling average
plt.figure(figsize=(12, 6))
time_series_data_rolling_avg.plot(color='orange', label='3-Year Rolling Average')
time_series_data.plot(alpha=0.5, label='Original Average Prices')
plt.title('3-Year Rolling Average of House Prices')
plt.xlabel('Year')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.show()

# Convert the timestamp column to a datetime object
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Set the timestamp as the index for time-series analysis
df.set_index('timestamp', inplace=True)

# Resample the data to get monthly average prices
monthly_avg = df['price'].resample('M').mean()

# Plot the monthly average prices
monthly_avg.plot()

# Implement a rolling average
rolling_avg = monthly_avg.rolling(window=3).mean()
rolling_avg.plot()

# Database Storage (using SQLite):

import sqlite3

# Create a new SQLite database or connect to an existing one
conn = sqlite3.connect('housing_data.db')

# Store the dataframe in a new table named "houses"
df.to_sql('houses', conn, if_exists='replace')


"""AUTOMATION AND PIPELINE"""

# Pseudo-code for an automated data pipeline

def ingest_data():
    # Code to collect new data entries
    pass

def clean_data(raw_data):
    # Code to clean and preprocess the raw data
    return cleaned_data

def transform_data(cleaned_data):
    # Code to perform feature engineering, transformations, etc.
    return transformed_data

def store_data(transformed_data):
    # Code to store the data in a database, as shown above
    pass

def run_pipeline():
    raw_data = ingest_data()
    cleaned_data = clean_data(raw_data)
    transformed_data = transform_data(cleaned_data)
    store_data(transformed_data)

# You would then schedule run_pipeline() to run periodically using tools like Apache Airflow or cron jobs


