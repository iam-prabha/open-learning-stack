# solution.py - k-NN answers

import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# TODO 1 & 2
digits = load_digits()
X, y = digits.data, digits.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# TODO 3
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# TODO 4
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)

# TODO 5
acc = model.score(X_test, y_test)
print(f"Test Accuracy: {acc * 100:.2f}%")

# TODO 6
# Answer: As 'k' INCREASES, the boundary becomes SMOOTHER. 
# Small k (like k=1) follows every tiny noise point (overfitting). 
# Large k averages out the noise.

# CHALLENGE ANSWER
for k in [1, 3, 21]:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    print(f"k={k}, Accuracy={knn.score(X_test, y_test)*100:.2f}%")
# High 'k' can be bad because it might start including 
# neighbors from other classes that are far away, 
# leading to 'Underfitting'.

print("\n--- Why it works ---")
print("1. Intuiton: It is the most human-like algorithm. 'If it walks like a duck and quacks like a duck, it's a duck.'")
print("2. Multi-Class: k-NN handles 10 or 100 classes just as easily as 2, with no extra math required.")
print("3. No Assumptions: Unlike Linear models, k-NN doesn't assume your data follows a line. It just follows the data clusters.")
print("4. Online Learning: You can add new data points to the model instantly without retraining (since there is no training!).")

export {};
