import pandas as pd

try:
    # Attempt to read the file
    df = pd.read_csv("products.csv")  # Replace with your actual file name
    print("File loaded successfully.")
    
    # Display the first few rows of the dataset
    print("First few rows of the dataset:")
    print(df.head())
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
    # View data types
    print(df.info())

    # Check for missing values
    print("Missing values before cleaning:")
    print(df.isnull().sum())

    # Fill missing values for numerical columns with their mean
    numeric_cols = df.select_dtypes(include=['number']).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

    # Optionally, drop rows with missing values in non-numeric columns
    df.dropna(subset=df.select_dtypes(exclude=['number']).columns, inplace=True)

    # Verify the dataset after cleaning
    print("Missing values after cleaning:")
    print(df.isnull().sum())
    print(df.info())

    # Task 2: Basic Data Analysis
    # Compute basic statistics for numerical columns
    print("Basic statistics for numerical columns:")
    print(df.describe())

    # Perform groupings on a categorical column and compute the mean of a numerical column
    # Replace 'category_column' and 'numerical_column' with actual column names
    if 'category_column' in df.columns and 'numerical_column' in df.columns:
        grouped_data = df.groupby('category_column')['numerical_column'].mean()
        print("Mean of numerical_column grouped by category_column:")
        print(grouped_data)
    else:
        print("Ensure 'category_column' and 'numerical_column' exist in the dataset.")

    # Identify patterns or interesting findings
    # Example: Check if any group has significantly higher or lower mean
    if 'category_column' in df.columns and 'numerical_column' in df.columns:
        print("Interesting findings:")
        print(grouped_data[grouped_data == grouped_data.max()])
        print(grouped_data[grouped_data == grouped_data.min()])
except KeyError as e:
    print(f"Error: Missing column - {e}. Please check the dataset.")
except ValueError as e:
    print(f"Error: Data type issue - {e}. Please check the dataset.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")