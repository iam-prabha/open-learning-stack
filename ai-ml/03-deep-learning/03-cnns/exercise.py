# exercise.py - Practice with CNNs

import torch
import torch.nn as nn

# TODO 1: Create a Convolutional layer with:
# - 3 input channels (RGB)
# - 16 output filters
# - 3x3 kernel size
# - 1 pixel of padding
conv = None # nn.Conv2d(...)

# TODO 2: Create a MaxPool2d layer with a 2x2 kernel 
# and a stride of 2.

# TODO 3: If you have an input image of 10x10 and 
# apply the pooling layer from TODO 2, what will 
# be the size of the output image?
# Answer: ... x ...

# TODO 4: What is 'Stride' and why do we use it?
# Answer: ...

# TODO 5: Define a simple model 'MiniCNN' that has 
# one Conv layer followed by a Flatten layer and 
# one Linear layer.

# TODO 6: Given an image of 3x32x32, what is the output 
# shape after a Conv2d(3, 10, kernel=3, padding=1) filter?
# (Hint: Padding=1 keeps the Size the same)
# Answer: ...

# CHALLENGE: Trace a [1, 1, 10, 10] image through:
# 1. Conv2d(1, 2, kernel=3, padding=0) -> 8x8 image
# 2. MaxPool2d(2, 2) -> 4x4 image
# 3. Flatten() -> a vector of length? (Channels * H * W)
# Print the final shape using a mock forward code.

# --- Verification ---
print("--- Results ---")
# Check your architecture logic vs the solution!
