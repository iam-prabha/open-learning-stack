# example.py - Decision Tree Classification

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split

# 1. Load Data (Classic Iris Dataset)
iris = load_iris()
X, y = iris.data, iris.target

# 2. Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# 3. Training the Model
# max_depth=3 prevents overfitting
model = DecisionTreeClassifier(max_depth=3)
model.fit(X_train, y_train)

# 4. Visualizing the Tree as Text
tree_rules = export_text(model, feature_names=iris.feature_names)
print("--- The Decision Tree Rules ---")
print(tree_rules)

# 5. Predictions
sample = [[5.1, 3.5, 1.4, 0.2]] # Should be Setosa (0)
pred = model.predict(sample)
print(f"Prediction for sample: {iris.target_names[pred[0]]}")

# 6. Feature Importance
for name, importance in zip(iris.feature_names, model.feature_names_in_):
    print(f"Feature: {name}, Importance: {model.feature_importances_[0]:.4f}")
