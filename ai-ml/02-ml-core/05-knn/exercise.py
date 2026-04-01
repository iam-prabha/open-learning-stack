# exercise.py - Practice with k-NN

import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# TODO 1: Load the 'digits' dataset (8x8 images of numbers).
digits = load_digits()
X, y = digits.data, digits.target

# TODO 2: Split data (80% train, 20% test).

# TODO 3: Scale the data. (k-NN is very sensitive to scale!)

# TODO 4: Initialize a KNeighborsClassifier with k=5. 
# Fit it to the training data.

# TODO 5: Calculate the test accuracy.

# TODO 6: What happens to the 'Decision Boundary' 
# as you INCREASE 'k'? (Does it get smoother or more jagged?)
# Answer: ...

# CHALLENGE: Write a loop to test k=1, k=3, and k=21. 
# Which one performs best? Why might a very high 'k' 
# be a bad idea?

# --- Verification ---
print("--- Results ---")
# Check your k-NN logic vs the solution!
