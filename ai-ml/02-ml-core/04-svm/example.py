# example.py - SVM Classification & Kernels

import numpy as np
from sklearn import svm
from sklearn.datasets import make_moons
from sklearn.preprocessing import StandardScaler

# 1. Create data (Non-linear 'Moon' shape)
X, y = make_moons(n_samples=100, noise=0.1)

# 2. IMPORTANT: Scale the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. Model 1: Linear Kernel (Will fail on moons)
linear_model = svm.SVC(kernel='linear')
linear_model.fit(X_scaled, y)
print(f"Linear SVM Accuracy: {linear_model.score(X_scaled, y)*100:.1f}%")

# 4. Model 2: RBF Kernel (The 'Kernel Trick')
rbf_model = svm.SVC(kernel='rbf', gamma='auto')
rbf_model.fit(X_scaled, y)
print(f"RBF SVM Accuracy: {rbf_model.score(X_scaled, y)*100:.1f}%")

# 5. Parameters
print(f"\nNumber of Support Vectors: {len(rbf_model.support_)}")
print(f"Indices of Support Vectors: {rbf_model.support_[:5]}...")

# 6. Predictions
sample = [[0.5, -0.5]]
sample_scaled = scaler.transform(sample)
print(f"\nPrediction for sample: {rbf_model.predict(sample_scaled)}")
