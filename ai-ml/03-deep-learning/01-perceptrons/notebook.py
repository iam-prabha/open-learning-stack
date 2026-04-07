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
# # Visualizing the Perceptron
#
# How does a single neuron decide? Let's visualize the **Decision Boundary**.

# %%
import numpy as np
import matplotlib.pyplot as plt

# Weights and Bias
w1, w2 = 0.5, 0.5
b = -0.7

# Decision boundary equation: w1x1 + w2x2 + b = 0
# Solve for x2: x2 = (-w1x1 - b) / w2
x1 = np.linspace(-1, 2, 100)
x2 = (-w1 * x1 - b) / w2

plt.figure(figsize=(6,4))
plt.plot(x1, x2, 'r--', label='Decision Boundary')
plt.fill_between(x1, x2, 2, color='blue', alpha=0.1, label='Class 1')
plt.fill_between(x1, x2, -1, color='green', alpha=0.1, label='Class 0')
plt.scatter([1], [1], color='blue') # AND gate point (1,1)
plt.scatter([0, 1, 0], [0, 0, 1], color='green') # Other points
plt.title("AND Gate Separability")
plt.xlabel("x1")
plt.ylabel("x2")
plt.legend()
plt.grid(True)
plt.show()
