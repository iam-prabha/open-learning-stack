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
# # Pre-trained Knowledge
#
# Let's visualize the **Filters** inside a pre-trained ResNet to see what it 'knows'.

# %%
import torch
import matplotlib.pyplot as plt
from torchvision import models

model = models.resnet18(pretrained=True)
kernels = model.conv1.weight.detach()

fig, axes = plt.subplots(8, 8, figsize=(8,8))
for i, ax in enumerate(axes.flat):
    # Normalize kernel to 0-1 for plotting
    k = kernels[i].cpu().numpy().transpose(1, 2, 0)
    k = (k - k.min()) / (k.max() - k.min())
    ax.imshow(k)
    ax.axis('off')

plt.suptitle("ResNet-18 Early Layer Filters (Edge Detectors)")
plt.show()
