# exercise.py - Practice with Logistic Regression

import numpy as np
from sklearn.linear_model import LogisticRegression

# TODO 1: Create X (Features) for whether a customer 
# clicked an ad based on 'Age'. 
# (X = [20, 25, 30, 45, 50, 60] reshaped)

# TODO 2: Create y (Clicked: 0=No, 1=Yes)
# (y = [0, 0, 0, 1, 1, 1])

# TODO 3: Fit a LogisticRegression model.

# TODO 4: Predict for someone aged 35. 
# Are they predicted to click?

# TODO 5: Use 'model.predict_proba' to see the confidence 
# for that 35-year-old.

# TODO 6: What is 'Log-Loss' (Cross-Entropy)? 
# Why don't we use Mean Squared Error for classification?
# Answer: ...

# CHALLENGE: Manually implement the Sigmoid function 
# using np.exp, and calculate the probability for 
# a score of z = 2.0.

# --- Verification ---
print("--- Results ---")
# Check your classification logic vs the solution!
