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
# # Visualizing Optimization Path
#
# Let's watch the optimizer 'step' down the error hill.

# %%
import numpy as np
import matplotlib.pyplot as plt

def loss(w):
    return w**2

def grad(w):
    return 2*w

w_vals = np.linspace(-10, 10, 100)
l_vals = loss(w_vals)

plt.plot(w_vals, l_vals, 'b-', label='Error Surface')

w = 8.0
lr = 0.2
for _ in range(10):
    plt.scatter(w, loss(w), color='red')
    w = w - lr * grad(w)

plt.title("The path of Gradient Descent")
plt.xlabel("Parameter Weight")
plt.ylabel("Model Error (Loss)")
plt.legend()
plt.show()
