# exercise.py - Practice with Decision Trees

from sklearn.datasets import load_breast_cancer
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# TODO 1: Load the 'breast_cancer' dataset.
data = load_breast_cancer()
X, y = data.data, data.target

# TODO 2: Split data into 80% train and 20% test.

# TODO 3: Initialize a DecisionTreeClassifier with 
# 'max_depth=5' and fit it to the training data.

# TODO 4: Calculate the accuracy on the test set.

# TODO 5: Which mathematical metric does a tree use 
# to decide which question to ask first?
# Answer: ...

# TODO 6: What is 'Pruning' and why do we do it?
# Answer: ...

# CHALLENGE: Find the FEATURE IMPORTANCE for all features 
# and print the names of the top 3 most important features.
# (Hint: model.feature_importances_)

# --- Verification ---
print("--- Results ---")
# Check your tree logic vs the solution!
