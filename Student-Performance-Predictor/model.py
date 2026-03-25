import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression

# Generate synthetic data for demonstration
X, y = make_regression(n_samples=100, n_features=1, noise=10)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Generate predictions
predictions = model.predict(X_test)

# Visualization
plt.scatter(X_test, y_test, color='blue', label='Actual')
plt.scatter(X_test, predictions, color='red', label='Predicted')
plt.title('Student Performance Prediction')
plt.xlabel('Feature (X)')
plt.ylabel('Target (y)')
plt.legend()

# Save the visualization to output.png
plt.savefig('output.png')
plt.close()