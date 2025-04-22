import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("products.csv")

# Line Chart: Trends over time (release_date vs revenue)
df['release_date'] = pd.to_datetime(df['release_date'])  # Ensure the date column is in datetime format
df.sort_values('release_date', inplace=True)
plt.figure(figsize=(10, 6))
plt.plot(df['release_date'], df['revenue ($)'], marker='o', label='Revenue Trend')
plt.title("Revenue Trend Over Time")
plt.xlabel("Release Date")
plt.ylabel("Revenue ($)")
plt.legend()
plt.grid()
plt.show()

# Bar Chart: Comparison across brands (brand vs revenue)
brand_means = df.groupby('brand')['revenue ($)'].mean()
plt.figure(figsize=(10, 6))
brand_means.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title("Average Revenue Across Brands")
plt.xlabel("Brand")
plt.ylabel("Average Revenue ($)")
plt.xticks(rotation=45)
plt.show()

# Histogram: Distribution of product prices
plt.figure(figsize=(10, 6))
plt.hist(df['price'], bins=10, color='orange', edgecolor='black')
plt.title("Distribution of Product Prices")
plt.xlabel("Price ($)")
plt.ylabel("Frequency")
plt.grid(axis='y')
plt.show()

# Scatter Plot: Relationship between price and rating
plt.figure(figsize=(10, 6))
plt.scatter(df['price'], df['rating'], color='green', alpha=0.7)
plt.title("Scatter Plot of Price vs Rating")
plt.xlabel("Price ($)")
plt.ylabel("Rating")
plt.grid()
plt.show()
