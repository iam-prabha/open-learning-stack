# example.py - Building a CNN with PyTorch

import torch
import torch.nn as nn
import torch.nn.functional as F

# 1. Defining a Simple CNN (LeNet-inspired)
class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        # Conv Layer 1: 1 input channel (Gray), 6 output filters, 5x5 kernel
        self.conv1 = nn.Conv2d(1, 6, 5)
        # Pooling: 2x2 window
        self.pool = nn.MaxPool2d(2, 2)
        # Conv Layer 2: 6 inputs, 16 outputs, 5x5 kernel
        self.conv2 = nn.Conv2d(6, 16, 5)
        # Fully connected layers (FC)
        # 16 filters * 4x4 image size (after pooling twice)
        self.fc1 = nn.Linear(16 * 4 * 4, 120)
        self.fc2 = nn.Linear(120, 10) # 10 classes

    def forward(self, x):
        # x shape: [batch, 1, 28, 28]
        x = self.pool(F.relu(self.conv1(x))) # [batch, 6, 12, 12]
        x = self.pool(F.relu(self.conv2(x))) # [batch, 16, 4, 4]
        # Flatten before FC layer
        x = x.view(-1, 16 * 4 * 4)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# 2. Simulated Input (Single 28x28 grayscale image)
batch_img = torch.randn(1, 1, 28, 28)

# 3. Model Inference
model = SimpleCNN()
with torch.no_grad():
    output = model(batch_img)

print("--- CNN Output ---")
print(f"Shape: {output.shape}")
print(f"Probabilities (Logits): {output[0]}")
print(f"Predicted Class: {torch.argmax(output).item()}")
