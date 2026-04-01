# exercise.py - Practice with Clustering

import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris

# TODO 1: Load the 'iris' data (X only).
iris = load_iris()
X = iris.data

# TODO 2: Initialize KMeans with k=3. 
# Why 3? (Hint: How many flower types are in iris?)

# TODO 3: Fit the model and predict the labels.

# TODO 4: Print the cluster centers.

# TODO 5: What is 'Inertia' in K-Means? 
# Does a HIGHER or LOWER inertia mean better clusters?
# Answer: ...

# TODO 6: Define 'Unsupervised Learning' in one sentence.
# Answer: ...

# CHALLENGE: Implement the 'Elbow Method' for K=1 to K=6. 
# Print the Inertia for each K. 
# Where does the 'elbow' appear visually (if you could plot it)?

# --- Verification ---
print("--- Results ---")
# Check your clustering logic vs the solution!
