# solution.py - Linear Regression answers

import numpy as np
from sklearn.linear_model import LinearRegression

# TODO 1 & 2
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([2, 4, 6, 8, 10])

# TODO 3
model = LinearRegression()
model.fit(X, y)

# TODO 4
print(f"Slope: {model.coef_[0]:.2f}")

# TODO 5
pred_6 = model.predict([[6]])
print(f"Prediction for 6: {pred_6[0]:.2f}")

# TODO 6
# Answer: MSE is more sensitive to large errors (due to 
# the squaring), and its derivative is 'nicer' for 
# optimization (gradient descent).

# CHALLENGE ANSWER
slope = model.coef_[0]
intercept = model.intercept_
manual_pred = (slope * 10) + intercept
print(f"Manual Prediction for 10: {manual_pred:.2f}")

print("\n--- Why it works ---")
print("1. Simplicity: Linear regression is fast and easy to interpret. You can explain exactly *why* a prediction was made using the slope.")
print("2. Baseline: It serves as a perfect 'baseline' model—if a complex neural network can't beat linear regression, the complex model is overkill.")
print("3. Extrapolation: It allows us to estimate values outside of our original data range (though this can be risky).")
print("4. Statistical Foundation: It is literally the most studied algorithm in statistics, with decades of math proving its properties.")

export {};
