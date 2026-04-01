# example.py - K-Means Clustering & Elbow Method

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# 1. Create simulated data (4 clear clusters)
X, y_true = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# 2. Training the Model (K=4)
model = KMeans(n_clusters=4, n_init=10)
model.fit(X)
y_kmeans = model.predict(X)

# 3. Model Parameters
centers = model.cluster_centers_
print(f"Cluster Centroids:\n{centers}")

# 4. The Elbow Method (Finding the best K)
# Inertia = Sum of squared distances to center
wcss = [] # Within cluster sum of squares
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, n_init=10)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

print("\nWCSS for K=1..10:")
for i, val in enumerate(wcss):
    print(f"K={i+1}: {val:.2f}")

# 5. Prediction for new data
new_point = np.array([[2.0, 1.0]])
cluster = model.predict(new_point)
print(f"\nNew point (2.0, 1.0) belongs to Cluster: {cluster[0]}")
