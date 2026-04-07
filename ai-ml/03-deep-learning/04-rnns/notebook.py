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
# # RNN 'Unrolling'
#
# How does a single cell process a sequence? By keeping a memory stick called the **Hidden State**.

# %%
import numpy as np
import matplotlib.pyplot as plt

# Simple manual RNN cell: h_t = tanh(W_h * h_t-1 + W_x * x_t)
Wx = 1.0
Wh = 0.5
h = 0.0

sequence = [1, 2, 0.5, -1, 3]
history_h = [h]

for x in sequence:
    h = np.tanh(Wh * h + Wx * x)
    history_h.append(h)

plt.figure(figsize=(8,3))
plt.plot(history_h, marker='o', label='Hidden State (Memory)')
plt.title("How the memory evolves word-by-word")
plt.xlabel("Time Step")
plt.ylabel("State Value")
plt.xticks(range(len(history_h)))
plt.legend()
plt.grid(True)
plt.show()
