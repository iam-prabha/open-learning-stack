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
# # The Central Limit Theorem (CLT)
#
# No matter what your data looks like, if you take enough samples, the **Distribution of Sample Means** will always be a Normal distribution (Bell Curve).

# %%
import numpy as np
import matplotlib.pyplot as plt

# Create non-normal data (Uniform)
data = np.random.uniform(0, 1, 10000)

# Take 500 samples of size 30 each and record their means
means = [np.mean(np.random.choice(data, 30)) for _ in range(500)]

plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.hist(data, bins=30, color='green', alpha=0.5)
plt.title("Original Data (Uniform)")

plt.subplot(1, 2, 2)
plt.hist(means, bins=30, color='blue', alpha=0.5)
plt.title("Distribution of Sample Means (Normal!)")

plt.tight_layout()
plt.show()
