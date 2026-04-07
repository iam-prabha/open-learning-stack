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
# # Visualizing Distributions
#
# Let's see the 'Bell Curve' (Normal Distribution) in action.

# %%
import numpy as np
import matplotlib.pyplot as plt

# Sample data
samples = np.random.normal(100, 15, 1000)

plt.figure(figsize=(10,4))
plt.hist(samples, bins=50, color='skyblue', edgecolor='black', alpha=0.7)
plt.axvline(100, color='red', linestyle='--', label='Mean (100)')
plt.title("The Bell Curve (IQ, Heights, Errors)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()
