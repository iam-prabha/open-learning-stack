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
# # Visualizing the Derivative
#
# A derivative is just the 'slope' at a single point.

# %%
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2

def df(x):
    return 2*x

x = np.linspace(-5, 5, 100)
y = f(x)

x_point = 2.0
y_point = f(x_point)
slope = df(x_point)

# Tangent line equation: y - y1 = m(x - x1) -> y = m(x - x1) + y1
tangent_y = slope * (x - x_point) + y_point

plt.figure(figsize=(8,3))
plt.plot(x, y, 'b-', label='f(x) = x^2')
plt.plot(x, tangent_y, 'r--', label=f'Tangent at x={x_point}')
plt.scatter([x_point], [y_point], color='red')
plt.ylim(-1, 25)
plt.grid(True)
plt.title("Slope as a Tangent Line")
plt.legend()
plt.show()
