import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("CAvideos.csv")

# Select features
df = df[["views", "likes", "dislikes", "comment_count"]].dropna()

# Features & Target
X = df[["likes", "dislikes", "comment_count"]]
y = df["views"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction
predictions = model.predict(X_test)

# Accuracy
print("Model Score:", model.score(X_test, y_test))

# Visualization
plt.scatter(y_test, predictions)
plt.xlabel("Actual Views")
plt.ylabel("Predicted Views")
plt.show()