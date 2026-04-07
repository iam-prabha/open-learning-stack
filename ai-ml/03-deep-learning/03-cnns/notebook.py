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
# # Visualizing Convolutions
#
# What does a 'kernel' actually see? Let's apply an edge-detection filter to an image.

# %%
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Create a simple image (a square)
img = np.zeros((20, 20))
img[5:15, 5:15] = 1

# Vertical Edge Detection Filter (Sobel)
kernel = np.array([[-1, 0, 1], 
                   [-2, 0, 2], 
                   [-1, 0, 1]])

# Apply Convolution
grad = signal.convolve2d(img, kernel, mode='same')

plt.figure(figsize=(10, 4))
plt.subplot(1, 3, 1)
plt.imshow(img, cmap='gray')
plt.title("Original Image")

plt.subplot(1, 3, 2)
plt.imshow(kernel, cmap='gray')
plt.title("Vertical Kernel")

plt.subplot(1, 3, 3)
plt.imshow(grad, cmap='gray')
plt.title("Detected Edges")
plt.show()
