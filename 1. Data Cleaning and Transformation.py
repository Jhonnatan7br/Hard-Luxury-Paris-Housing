"""DATA CLEANING, MINING AND TRANSFORMATION""" 

# Step 1: Let's load the data and take a look at the first few rows to understand what we're working with.
import pandas as pd
# Load the dataset
file_path = "PATH TO THE DATASET"
df = pd.read_csv(file_path)
# Display the first few rows of the dataset
df.head()

# Step 2: Check for missing values
# Check the number of missing values in each column
df.isnull().sum()

# Step 3: Check for duplicate rows
# Count the number of duplicate rows
num_duplicates = df.duplicated().sum()
num_duplicates

# Step 4: Check for outliers
import matplotlib.pyplot as plt
# Create a boxplot for the 'price' column
plt.boxplot(df['price'])
plt.title('Boxplot of Price')
plt.show()

# Step 5: Check data types
# Check the data types of each column
df.dtypes

# Step 6: Check for inconsistent values
# Check for any years in the 'made' column that are after the current year
inconsistent_years = df[df['made'] > 2023]
inconsistent_years

# DATA TRANSFORMATION

import pandas as pd
import numpy as np

# Load the dataset again
df_transformed = pd.read_csv("/mnt/data/Paris Housing Luxury Classification.csv")

# 1. Normalization: Normalize the 'squareMeters' column for demonstration
df_transformed['squareMeters_normalized'] = (df_transformed['squareMeters'] - df_transformed['squareMeters'].mean()) / df_transformed['squareMeters'].std()

# 2. One-Hot Encoding: Convert the 'category' column into separate binary columns
df_transformed = pd.concat([df_transformed, pd.get_dummies(df_transformed['category'], prefix='category')], axis=1)

# 3. Feature Engineering: Create a "total area" feature
df_transformed['total_area'] = df_transformed['squareMeters'] + df_transformed['basement'] + df_transformed['attic'] + df_transformed['garage']

# 4. Log Transformation: Apply log transformation to 'price' column
df_transformed['price_log'] = df_transformed['price'].apply(lambda x: np.log1p(x))

# 5. Binning: Convert 'price' into bins or categories (Low, Medium, High)
bins = [0, df_transformed['price'].quantile(0.33), df_transformed['price'].quantile(0.66), df_transformed['price'].max()]
labels = ['Low', 'Medium', 'High']
df_transformed['price_bin'] = pd.cut(df_transformed['price'], bins=bins, labels=labels, include_lowest=True)

# Display the first few rows of the transformed dataset
df_transformed.head()


