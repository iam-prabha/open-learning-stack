# exercise.py - Practice with SVM

from sklearn import svm
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler

# TODO 1: Load the 'iris' dataset and take 
# only the first two features (sepal length/width).
iris = load_iris()
X = iris.data[:, :2]
y = iris.target

# TODO 2: Scale the data using StandardScaler.

# TODO 3: Initialize an SVC model with kernel='rbf' 
# and C=1.0. Fit it to the scaled data.

# TODO 4: Compare the accuracy to an SVM model with C=0.01. 
# Which one is more 'regularized'?
# Answer: ...

# TODO 5: What are 'Support Vectors'? 
# Answer: ...

# TODO 6: Why SHOULD you use a Kernel (like 'poly' or 'rbf') 
# instead of a linear boundary?
# Answer: ...

# CHALLENGE: Find the coordinates of the Support Vectors 
# for your trained model and print the first 3.
# (Hint: model.support_vectors_)

# --- Verification ---
print("--- Results ---")
# Check your SVM logic vs the solution!
