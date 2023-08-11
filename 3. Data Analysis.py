# Let's begin with the first analysis: Distribution of House Prices.

# Step 1: Let's load the data and take a look at the first few rows to understand what we're working with.
import pandas as pd
# Load the dataset
file_path = "PATH TO THE DATASET"
df = pd.read_csv(file_path)
# Display the first few rows of the dataset
df.head()

# Analysis 1: Distribution of House Prices

# Create a histogram to visualize the distribution of house prices
plt.figure(figsize=(10, 6))
plt.hist(df['price'], bins=30, color='skyblue', edgecolor='black')
plt.title('Distribution of House Prices')
plt.xlabel('Price')
plt.ylabel('Number of Houses')
plt.show()

# Analysis 2: Distribution of House Categories ('Basic' vs 'Luxury')

# Create a bar chart to visualize the distribution of house categories
category_counts = df['category'].value_counts()
plt.figure(figsize=(8, 5))
category_counts.plot(kind='bar', color=['lightcoral', 'lightgreen'])
plt.title('Distribution of House Categories')
plt.xlabel('Category')
plt.ylabel('Number of Houses')
plt.xticks(rotation=0)
plt.show()

# Analysis 3: Price Distribution by Category

# Create a boxplot to compare the price distributions of 'Basic' and 'Luxury' houses
plt.figure(figsize=(8, 6))
df.boxplot(column='price', by='category', patch_artist=True, boxprops=dict(facecolor='lightgray'))
plt.title('Price Distribution by Category')
plt.suptitle('')  # Remove automatic title
plt.xlabel('Category')
plt.ylabel('Price')
plt.show()

# Analysis 4: Price vs. Square Meters

# Create a scatter plot to visualize the relationship between square meters and price
plt.figure(figsize=(10, 6))
plt.scatter(df['squareMeters'], df['price'], alpha=0.5, color='dodgerblue')
plt.title('Price vs. Square Meters')
plt.xlabel('Square Meters')
plt.ylabel('Price')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.show()

# Analysis 5: Number of Houses with Specific Features

# Create a bar chart to visualize the number of houses with specific features
features = ['hasYard', 'hasPool', 'hasStormProtector', 'hasStorageRoom']
feature_counts = df[features].sum()

plt.figure(figsize=(10, 6))
feature_counts.plot(kind='bar', color='mediumpurple')
plt.title('Number of Houses with Specific Features')
plt.xlabel('Features')
plt.ylabel('Number of Houses')
plt.xticks(rotation=45)
plt.show()

# Analysis 6: Price Distribution based on Number of Previous Owners

# Create a boxplot to visualize the distribution of prices based on the number of previous owners
plt.figure(figsize=(12, 7))
df.boxplot(column='price', by='numPrevOwners', patch_artist=True, boxprops=dict(facecolor='lightyellow'))
plt.title('Price Distribution based on Number of Previous Owners')
plt.suptitle('')  # Remove automatic title
plt.xlabel('Number of Previous Owners')
plt.ylabel('Price')
plt.show()