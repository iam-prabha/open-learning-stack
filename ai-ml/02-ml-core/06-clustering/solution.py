# solution.py - Clustering answers

import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris

# TODO 1 & 2
iris = load_iris()
X = iris.data
model = KMeans(n_clusters=3, n_init=10)

# TODO 3
y_kmeans = model.fit_predict(X)

# TODO 4
print(f"Discovered Centers:\n{model.cluster_centers_}")

# TODO 5
# Answer: Inertia is the sum of squared distances of 
# samples to their closest cluster center. LOWER 
# inertia is generally better (means tighter clusters), 
# but it always goes down as K increases.

# TODO 6
# Answer: Training on data that has no labels, forcing 
# the model to find its own patterns and structures.

# CHALLENGE ANSWER
for k in range(1, 7):
    km = KMeans(n_clusters=k, n_init=10)
    km.fit(X)
    print(f"K={k}, Inertia={km.inertia_:.2f}")
# The 'elbow' usually appears at K=3 for this dataset, 
# match the 3 real species of flowers.

print("\n--- Why it works ---")
print("1. Discovery: Clustering helps you find groups in your data that you didn't even know existed (e.g., hidden segments of customers).")
print("2. Diversity: It is great for detecting anomalies—if a point doesn't belong to any cluster, it's probably suspicious.")
print("3. Preprocessing: You can use cluster labels as a new feature for other models (e.g., 'this user belongs to group A').")
print("4. Compression: It allows us to represent thousands of similar data points with just a single point (the cluster center).")

export {};
