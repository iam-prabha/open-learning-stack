# example.py - Linear Regression with Scikit-Learn

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# 1. Simulated Data (House Size in sqft, Price in $1000s)
X = np.array([[1000], [1500], [2000], [2500], [3000]])
y = np.array([200, 310, 390, 505, 610])

# 2. Training the Model
model = LinearRegression()
model.fit(X, y)

# 3. Model Parameters
# Price = (Slope * Size) + Intercept
slope = model.coef_[0]
intercept = model.intercept_
print(f"Model Formula: Price = {slope:.2f} * Size + {intercept:.2f}")

# 4. Predictions
new_houses = np.array([[1200], [1800]])
preds = model.predict(new_houses)
print(f"\nPredictions for 1200 & 1800 sqft:\n{preds}")

# 5. Model Performance (MSE)
y_pred = model.predict(X)
mse = mean_squared_error(y, y_pred)
print(f"\nMean Squared Error: {mse:.2f}")
