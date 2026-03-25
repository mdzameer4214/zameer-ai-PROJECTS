import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Sample data
# Suppose we have some feature data and corresponding targets
np.random.seed(42)
X = np.random.rand(100, 1) * 10  # Feature: Random numbers from 0 to 10
Y = 3 * X + np.random.randn(100, 1) * 3  # Target: Linear relation with noise

# Split the data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Create a linear regression model
model = LinearRegression()
model.fit(X_train, Y_train)

# Predict the values
Y_pred = model.predict(X_test)

# Visualization
plt.scatter(X_test, Y_test, color='blue', label='Actual data')
plt.plot(X_test, Y_pred, color='red', linewidth=2, label='Predicted data')
plt.title('YouTube Trend Prediction')
plt.xlabel('Feature')
plt.ylabel('Target')
plt.legend()
plt.savefig('output.png')  # Save the visualization
plt.show()  # Optionally show the plot
