# exercise.py - Practice with Transfer Learning

import torch
import torch.nn as nn
from torchvision import models

# TODO 1: Load a pre-trained 'VGG16' model. 
# (Check torchvision.models for the exact name)

# TODO 2: Print the 'classifier' section of the VGG16 model. 
# How many layers does it have?

# TODO 3: Freeze every parameter in the model so that 
# they don't update during training.

# TODO 4: What is the risk of using a very high 
# learning rate when fine-tuning a pre-trained model?
# Answer: ...

# TODO 5: Why do we often resize images to 224x224 
# before sending them to a pre-trained model?
# Answer: ...

# TODO 6: Replace the last layer of a ResNet-18 
# (model.fc) to predict 5 different types of flowers.

# CHALLENGE: Compare the number of trainable 
# parameters in a 'Frozen' ResNet-18 vs an 
# 'Unfrozen' one. Print both counts.

# --- Verification ---
print("--- Results ---")
# Check your transfer logic vs the solution!
