# example.py - k-Nearest Neighbors Classification

import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_wine

# 1. Load data
wine = load_wine()
X, y = wine.data, wine.target

# 2. Split and Scale
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 3. Model Training (k=3)
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

# 4. Predictions
print(f"Accuracy with k=3: {model.score(X_test, y_test)*100:.2f}%")

# 5. Finding the best 'k' (Elbow Method)
scores = []
for k in range(1, 15, 2):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    scores.append(knn.score(X_test, y_test))

print(f"\nBest k found: {range(1, 15, 2)[np.argmax(scores)]} with {max(scores)*100:.2f}% accuracy")

# 6. Identifying Neighbors
sample = X_test[0].reshape(1, -1)
distances, indices = model.kneighbors(sample)
print(f"\nDistances to 3 closest neighbors: {distances}")
print(f"Indices of neighbors: {indices}")
