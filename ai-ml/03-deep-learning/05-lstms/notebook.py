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
# # How LSTM Gates Work
#
# Visualization of the **Sigmoid** gates that control information flow.

# %%
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)
f = 1 / (1 + np.exp(-x)) # Sigmoid function

plt.figure(figsize=(6,3))
plt.plot(x, f, 'b-', label='Gate Response')
plt.title("Sigmoid Activation (The 'Gate Keeper')")
plt.axhline(1.0, color='r', linestyle='--', label='Let Everything Through')
plt.axhline(0.0, color='g', linestyle='--', label='Forget Everything')
plt.xlabel("Signal Strength")
plt.ylabel("Flow Control")
plt.legend()
plt.grid(True)
plt.show()
