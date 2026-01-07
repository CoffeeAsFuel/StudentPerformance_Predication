import pandas as pd

# Load dataset
data = pd.read_csv("data/student_data.csv")

# Show first 5 rows
print("First 5 rows of dataset:")
print(data.head())

# Dataset information
print("\nDataset Info:")
print(data.info())
