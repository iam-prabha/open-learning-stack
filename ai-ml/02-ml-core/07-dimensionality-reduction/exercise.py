# exercise.py - Practice with PCA

import numpy as np
from sklearn.decomposition import PCA
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler

# TODO 1: Load the 'breast_cancer' dataset (30 features).
data = load_breast_cancer()
X = data.data

# TODO 2: Why MUST you scale this data before PCA?
# Answer: ...

# TODO 3: Initialize PCA with n_components=5. 
# Fit it to the scaled data.

# TODO 4: How much variance is explained by the 
# FIRST principal component alone?
# (Hint: model.explained_variance_ratio_[0])

# TODO 5: Define 'Principal Components' in your own words.
# Answer: ...

# TODO 6: What is a common use-case for PCA besides speed?
# Answer: ...

# CHALLENGE: Find the minimum number of components 
# required to keep at least 90% of the variance. 
# (Hint: Loop through n_components and check sum of variance ratio)

# --- Verification ---
print("--- Results ---")
# Check your PCA logic vs the solution!
