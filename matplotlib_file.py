import pandas as pd
import matplotlib.pyplot as plt

try:
    # Attempt to read the file
    df = pd.read_csv("products.csv")
    print("File loaded successfully.")
except FileNotFoundError:
    print("Error: The file 'products.csv' was not found. Please check the file path.")
    exit()
except pd.errors.EmptyDataError:
    print("Error: The file is empty. Please provide a valid dataset.")
    exit()
except pd.errors.ParserError:
    print("Error: The file could not be parsed. Please check the file format.")
    exit()

try:
    # Line Chart: Trends over time (release_date vs revenue)
    if 'release_date' in df.columns and 'revenue ($)' in df.columns:
        df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')  # Handle invalid dates
        df.dropna(subset=['release_date'], inplace=True)  # Drop rows with invalid dates
        df.sort_values('release_date', inplace=True)
        plt.figure(figsize=(10, 6))
        plt.plot(df['release_date'], df['revenue ($)'], marker='o', label='Revenue Trend')
        plt.title("Revenue Trend Over Time")
        plt.xlabel("Release Date")
        plt.ylabel("Revenue ($)")
        plt.legend()
        plt.grid()
        plt.show()
    else:
        print("Error: Columns 'release_date' and 'revenue ($)' are required for the line chart.")

    # Bar Chart: Comparison across brands (brand vs revenue)
    if 'brand' in df.columns and 'revenue ($)' in df.columns:
        brand_means = df.groupby('brand')['revenue ($)'].mean()
        plt.figure(figsize=(10, 6))
        brand_means.plot(kind='bar', color='skyblue', edgecolor='black')
        plt.title("Average Revenue Across Brands")
        plt.xlabel("Brand")
        plt.ylabel("Average Revenue ($)")
        plt.xticks(rotation=45)
        plt.show()
    else:
        print("Error: Columns 'brand' and 'revenue ($)' are required for the bar chart.")

    # Histogram: Distribution of product prices
    if 'price' in df.columns:
        plt.figure(figsize=(10, 6))
        plt.hist(df['price'], bins=10, color='orange', edgecolor='black')
        plt.title("Distribution of Product Prices")
        plt.xlabel("Price ($)")
        plt.ylabel("Frequency")
        plt.grid(axis='y')
        plt.show()
    else:
        print("Error: Column 'price' is required for the histogram.")

    # Scatter Plot: Relationship between price and rating
    if 'price' in df.columns and 'rating' in df.columns:
        plt.figure(figsize=(10, 6))
        plt.scatter(df['price'], df['rating'], color='green', alpha=0.7)
        plt.title("Scatter Plot of Price vs Rating")
        plt.xlabel("Price ($)")
        plt.ylabel("Rating")
        plt.grid()
        plt.show()
    else:
        print("Error: Columns 'price' and 'rating' are required for the scatter plot.")

except KeyError as e:
    print(f"Error: Missing column - {e}. Please check the dataset.")
except ValueError as e:
    print(f"Error: Data type issue - {e}. Please check the dataset.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
