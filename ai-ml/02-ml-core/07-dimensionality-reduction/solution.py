# solution.py - PCA answers

import numpy as np
from sklearn.decomposition import PCA
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler

# TODO 1
data = load_breast_cancer()
X = data.data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# TODO 2
# Answer: PCA looks for the 'direction of maximum variance'. 
# If one feature is measured in 1000s (Income) and 
# another in 0s (Rating), the 1000s will mathematically 
# look like they have 'more variance' just because 
# the numbers are bigger.

# TODO 3 & 4
pca = PCA(n_components=5)
pca.fit(X_scaled)
print(f"PC1 Variance: {pca.explained_variance_ratio_[0]*100:.2f}%")

# TODO 5
# Answer: New, artificial features that represent 
# directions in the data that contain the most 'spread' 
# or information.

# TODO 6
# Answer: Data Visualization (converting high-D data 
# to 2D scatter plots) or Noise Reduction.

# CHALLENGE ANSWER
full_pca = PCA().fit(X_scaled)
cum_var = np.cumsum(full_pca.explained_variance_ratio_)
n_90 = np.argmax(cum_var >= 0.90) + 1
print(f"Components needed for 90% variance: {n_90}")

print("\n--- Why it works ---")
print("1. Redundancy: Most high-D data is redundant—if you know a house's square footage, you can probably guess the number of rooms. PCA exploits this.")
print("2. Orthogonality: All Principal Components are perpendicular (uncorrelated) to each other, which makes life easier for downstream models.")
print("3. Human-Readable: We can't see in 30D, but we can see in 2D. PCA is our 'glasses' for high-dimensional data.")
print("4. Signal vs Noise: The first few components capture the 'Signal' (real patterns), while the later ones usually capture randomized 'Noise'.")

export {};
