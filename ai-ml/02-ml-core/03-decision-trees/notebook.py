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
# # Visualizing Decision Splits
#
# Trees don't use diagonal lines; they use horizontal and vertical 'cuts' through the data.

# %%
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier

# Create some non-linear data
X = np.random.rand(100, 2)
y = (X[:, 0] > 0.5) & (X[:, 1] > 0.5)
y = y.astype(int)

model = DecisionTreeClassifier(max_depth=2)
model.fit(X, y)

# Color the background
xx, yy = np.meshgrid(np.linspace(0, 1, 100), np.linspace(0, 1, 100))
Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.figure(figsize=(8,4))
plt.contourf(xx, yy, Z, alpha=0.3, cmap='viridis')
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis', edgecolors='k')
plt.title("The Rectangle World of Decision Trees")
plt.show()
