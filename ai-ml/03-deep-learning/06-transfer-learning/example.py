# example.py - Using Pre-trained Models with PyTorch

import torch
import torch.nn as nn
from torchvision import models

# 1. Loading a Pre-trained Model (ResNet-18)
# ResNet-18 is trained on ImageNet (1000 categories)
model = models.resnet18(pretrained=True)

# 2. Freezing the base layers
# This prevents the pre-trained weights from being updated
for param in model.parameters():
    param.requires_grad = False

# 3. Replacing the Final Layer (Head)
# ResNet-18 has 512 input features in the last layer
num_ftrs = model.fc.in_features
# Let's say we only have 2 classes (Cat or Dog)
model.fc = nn.Linear(num_ftrs, 2)

# 4. Check what we are training
# Only the parameters of the final layer will have grad=True
print("--- Transfer Learning Setup ---")
print(f"Total Parameters: {len(list(model.parameters()))}")
print(f"Trainable Parameters: {len([p for p in model.parameters() if p.requires_grad])}")

# 5. Simulated Inference
# batch=1, RGB=3, Size=224x224 (ResNet default)
X = torch.randn(1, 3, 224, 224)
with torch.no_grad():
    output = model(X)

print("\n--- Model Output ---")
print(f"Output Shape: {output.shape}") # [1, 2]
print(f"Predicted logits: {output}")
