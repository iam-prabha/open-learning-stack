# solution.py - CNN answers

import torch
import torch.nn as nn

# TODO 1
conv = nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3, padding=1)

# TODO 2
pool = nn.MaxPool2d(kernel_size=2, stride=2)

# TODO 3
# Answer: 5x5 (The size is halved)

# TODO 4
# Answer: Stride is the number of pixels the filter 'jumps' 
# across the image. A larger stride reduces the output 
# size and computational cost but might miss fine details.

# TODO 5
class MiniCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = nn.Conv2d(1, 4, 3)
        self.flatten = nn.Flatten()
        self.fc = nn.Linear(4 * 26 * 26, 10) # 28-3+1 = 26
    def forward(self, x):
        return self.fc(self.flatten(self.conv(x)))

# TODO 6
# Answer: [B, 10, 32, 32] (Channels change to 10, Size stays 32)

# CHALLENGE ANSWER
x = torch.randn(1, 1, 10, 10)
m = nn.Sequential(
    nn.Conv2d(1, 2, kernel_size=3), # -> [1, 2, 8, 8]
    nn.MaxPool2d(2, 2),             # -> [1, 2, 4, 4]
    nn.Flatten()                    # -> [1, 2*4*4] = [1, 32]
)
print(f"Final shape: {m(x).shape}") # length 32

print("\n--- Why it works ---")
print("1. Translational Invariance: CNNs can detect a 'cat' whether it's in the top-left or bottom-right of the photo.")
print("2. Parameter Sharing: A filter that detects 'edges' is useful everywhere in the image, so we use the same filter for every pixel spot.")
print("3. Pooling: It makes the network robust to small movements or distortions in the input image.")
print("4. Hierarchical Learning: Deeper layers automatically combine simple features (lines) into complex ones (faces).")

export {};
