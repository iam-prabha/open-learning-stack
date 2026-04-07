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
# # Visualizing the Sigmoid
#
# Let's see how our model turns a line into an 'S' shape probability curve.

# %%
import numpy as np
import matplotlib.pyplot as plt

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

z = np.linspace(-10, 10, 100)
p = sigmoid(z)

plt.figure(figsize=(8,3))
plt.plot(z, p, color='green', label='Sigmoid Curve')
plt.axvline(0, color='red', linestyle='--', label='Decision Boundary (0.5)')
plt.axhline(0.5, color='gray', linestyle=':')
plt.title("The Binary Bridge (0 or 1)")
plt.xlabel("Input Score (z)")
plt.ylabel("Probability (p)")
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()
