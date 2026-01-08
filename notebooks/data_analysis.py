import pandas as pd

# Load dataset
df = pd.read_csv("data/student_data.csv")

# Clean column names (important best practice)
df.columns = df.columns.str.strip()

print("Columns:")
print(df.columns)

print("\nFirst rows:")
print(df.head())

# Average final marks
print("\nAverage Final Marks:")
print(df["final_marks"].mean())
