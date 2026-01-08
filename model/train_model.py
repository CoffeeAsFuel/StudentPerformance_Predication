import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Load data
df = pd.read_csv("data/student_data.csv")
df.columns = df.columns.str.strip()

# Features (inputs) and target (output)
X = df[["study_hours", "attendance", "previous_score"]]
y = df["final_marks"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Evaluate
mae = mean_absolute_error(y_test, predictions)
print("Mean Absolute Error:", mae)

# Test custom prediction
sample = [[6, 80, 70]]
predicted_marks = model.predict(sample)
print("Predicted Final Marks for sample:", predicted_marks[0])
