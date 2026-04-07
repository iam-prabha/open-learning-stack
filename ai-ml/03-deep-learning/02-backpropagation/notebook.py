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
# # Visualizing Gradient Descent
#
# Backpropagation gives us the 'slope'. Optimization uses it to 'walk down' the hill.

# %%
import numpy as np
import matplotlib.pyplot as plt

def loss_func(w):
    return w**2

def gradient(w):
    return 2*w

w = np.linspace(-10, 10, 100)
l = loss_func(w)

plt.plot(w, l, 'b-', label='Loss Curve')

# Simulate 5 steps of gradient descent
current_w = 8.0
history_w = []
for _ in range(5):
    history_w.append(current_w)
    grad = gradient(current_w)
    current_w = current_w - 0.2 * grad # learning rate = 0.2

history_l = [loss_func(x) for x in history_w]
plt.scatter(history_w, history_l, color='red', label='GD Steps')
plt.quiver(history_w[:-1], history_l[:-1], 
           np.array(history_w[1:]) - np.array(history_w[:-1]), 
           np.array(history_l[1:]) - np.array(history_l[:-1]), 
           scale_units='xy', angles='xy', scale=1, color='red', alpha=0.5)

plt.title("The path to Minimum Loss")
plt.xlabel("Weight (w)")
plt.ylabel("Loss (L)")
plt.legend()
plt.show()
