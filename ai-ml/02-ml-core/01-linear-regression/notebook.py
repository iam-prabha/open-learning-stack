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
# # Visualizing Linear Regression
#
# Let's see how well a line fits these points.

# %%
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

X = np.array([10, 15, 20, 25, 30]).reshape(-1, 1)
y = np.array([21, 29, 42, 51, 58])

model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

plt.figure(figsize=(8,3))
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, y_pred, color='red', label='Line of Best Fit')
plt.title("Predicting y from x")
plt.xlabel("Input (x)")
plt.ylabel("Output (y)")
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()
