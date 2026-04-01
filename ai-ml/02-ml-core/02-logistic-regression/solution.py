# solution.py - Logistic Regression answers

import numpy as np
from sklearn.linear_model import LogisticRegression

# TODO 1 & 2
X = np.array([20, 25, 30, 45, 50, 60]).reshape(-1, 1)
y = np.array([0, 0, 0, 1, 1, 1])

# TODO 3
model = LogisticRegression()
model.fit(X, y)

# TODO 4
pred_35 = model.predict([[35]])
print(f"35-year-old click prediction: {pred_35[0]}")

# TODO 5
prob_35 = model.predict_proba([[35]])
print(f"Probabilities: {prob_35[0]}") # [No, Yes]

# TODO 6
# Answer: Log-loss penalizes models extremely heavily 
# for being 'confidently wrong' (e.g. predicting 0.99 
# probability for a 0). MSE is 'too soft' for classification.

# CHALLENGE ANSWER
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

manual_prob = sigmoid(2.0)
print(f"Manual Prob for z=2: {manual_prob:.4f}")

print("\n--- Why it works ---")
print("1. Probability Estimation: It doesn't just give you a category; it tells you HOW LIKELY it is. This is crucial for medical or financial AI.")
print("2. Robustness: It is less sensitive to outliers than Linear Regression because the Sigmoid curve 'caps' extreme values between 0 and 1.")
print("3. Efficiency: It is extremely fast to train and use, making it the 'workhorse' of the internet (used for ad-clicks and simple fraud detection).")
print("4. Interpretability: Like Linear Regression, you can look at the coefficients to see which features are the most important for the prediction.")

export {};
