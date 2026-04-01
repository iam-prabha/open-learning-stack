# solution.py - SVM answers

from sklearn import svm
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler

# TODO 1 & 2
iris = load_iris()
X = iris.data[:, :2] # Only 2 features for easy viz
y = iris.target
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# TODO 3
model = svm.SVC(kernel='rbf', C=1.0)
model.fit(X_scaled, y)

# TODO 4
# Answer: C=0.01 is more regularized. A smaller C 
# creates a WIDER margin but allows more points 
# to be misclassified (Soft Margin).

# TODO 5
# Answer: Support Vectors are the data points located 
# closest to the decision boundary. They are 'supporting' 
# the position of the road; if you move them, the road moves.

# TODO 6
# Answer: To capture non-linear secrets in your data. 
# Some patterns are impossible to separate with a straight 
# line but easy with a curved boundary.

# CHALLENGE ANSWER
sv = model.support_vectors_
print(f"First 3 Support Vectors:\n{sv[:3]}")

print("\n--- Why it works ---")
print("1. Optimization: SVM is a 'Quadratic Programming' problem, which means it has a single Global Optimum. You don't get stuck in local minima.")
print("2. Memory Efficiency: Only the Support Vectors are stored in the final model, making it very compact.")
print("3. Curse of Dimensionality: SVM handles high-dimensional space (more features than data points) surprisingly well.")
print("4. Versatility: By choosing different Kernels, you can adapt SVM to almost any type of structured data.")

export {};
