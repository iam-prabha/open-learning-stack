# example.py - Dimensionality Reduction (PCA)

import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler

# 1. Load Data (4 dimensions)
iris = load_iris()
X = iris.data
y = iris.target

# 2. Scale Data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. Model: PCA (Reduce 4D -> 2D)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

print(f"Original shape: {X_scaled.shape}") # (150, 4)
print(f"Reduced shape: {X_pca.shape}")      # (150, 2)

# 4. Explained Variance
# How much info did we keep?
var_ratio = pca.explained_variance_ratio_
print(f"\nExplained Variance Ratio: {var_ratio}")
print(f"Total Info Retained: {np.sum(var_ratio)*100:.2f}%")

# 5. Visualizing the new 2D clusters
plt.figure(figsize=(8,4))
for i, target_name in enumerate(iris.target_names):
    plt.scatter(X_pca[y == i, 0], X_pca[y == i, 1], label=target_name)
plt.title("Iris Data in 2D (via PCA)")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.legend()
plt.show()
