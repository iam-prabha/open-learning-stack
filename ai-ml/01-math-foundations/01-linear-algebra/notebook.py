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
# # Visualizing Vectors
#
# A vector is just an arrow in space. Let's visualize **Vector Addition**.

# %%
import numpy as np
import matplotlib.pyplot as plt

v1 = np.array([1, 2])
v2 = np.array([2, 1])
v3 = v1 + v2

origin = [0], [0]

plt.quiver(*origin, v1[0], v1[1], color='r', angles='xy', scale_units='xy', scale=1, label='v1 (1,2)')
plt.quiver(v1[0], v1[1], v2[0], v2[1], color='b', angles='xy', scale_units='xy', scale=1, label='v2 (2,1)')
plt.quiver(*origin, v3[0], v3[1], color='g', angles='xy', scale_units='xy', scale=1, label='v1 + v2 (3,3)')

plt.xlim(-1, 5)
plt.ylim(-1, 5)
plt.grid(True)
plt.title("The Triangle Law of Vector Addition")
plt.legend()
plt.show()
