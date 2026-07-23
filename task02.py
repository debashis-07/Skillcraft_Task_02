import sys
import io
# Force terminal to use UTF-8 encoding for output
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


import pandas as pd

# 1. Load the Dataset
# Replace 'global_superstore.csv' with your actual file name if different
file_path = 'superstore.csv'

print("Loading dataset...")
try:
    # ISO-8859-1 encoding handles special characters often found in Global Superstore datasets
    df = pd.read_csv(file_path, encoding='ISO-8859-1')
    print("Dataset Loaded Successfully!\n")
except FileNotFoundError:
    print(f"Error: Could not find '{file_path}'. Make sure it's in your project folder.")
    exit()

# Preview dataset structure
print("--- Initial Overview ---")
df.info()

# 2. Identify and Handle Missing Values
print("\n--- Missing Values Before Cleaning ---")
print(df.isnull().sum()[df.isnull().sum() > 0])

# Fill missing text values with 'Unknown' and numeric values with 0
for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = df[col].fillna('Unknown')
    else:
        df[col] = df[col].fillna(0)

print("Missing values after cleaning:", df.isnull().sum().sum())

# 3. Drop Duplicate Rows
initial_count = len(df)
df = df.drop_duplicates()
print(f"\nDuplicates removed: {initial_count - len(df)} rows.")

# 4. Convert Data Types (e.g., Strings to Datetime)
date_cols = ['Order Date', 'Ship Date']

for col in date_cols:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors='coerce')
        print(f"Converted '{col}' to datetime format.")

# 5. Export Cleaned Dataset
output_file = 'cleaned_superstore.csv'
df.to_csv(output_file, index=False)
print(f"\nSuccess! Cleaned data saved as '{output_file}'.")