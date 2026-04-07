# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Visualizing Clusters
#
# Let's see how K-Means partitions the space into voronoi cells.

# %%
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=10)
model = KMeans(n_clusters=4, n_init=10)
model.fit(X)
y_kmeans = model.predict(X)
centers = model.cluster_centers_

plt.figure(figsize=(10,6))
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis', alpha=0.6)
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, marker='X', label='Centroids')
plt.title("Discovered Clusters (K=4)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
