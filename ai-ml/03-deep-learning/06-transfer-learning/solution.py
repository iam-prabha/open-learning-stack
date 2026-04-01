# solution.py - Transfer Learning answers

import torch
import torch.nn as nn
from torchvision import models

# TODO 1 & 2
vgg = models.vgg16(pretrained=True)
print(f"VGG Classifier: {vgg.classifier}")

# TODO 3
for param in vgg.parameters():
    param.requires_grad = False

# TODO 4
# Answer: Catastrophic Forgetting. A high learning rate 
# will cause the model to rapidly overwrite the 
# carefully-tuned ImageNet weights, losing the general 
# features (edges, shapes) it already knows.

# TODO 5
# Answer: Most pre-trained models (ResNet, VGG, etc.) 
# were trained on ImageNet using 224x224 crops. Using 
# the same size ensures the filters 'see' the data 
# at the scale they expect.

# TODO 6
resnet = models.resnet18(pretrained=True)
resnet.fc = nn.Linear(resnet.fc.in_features, 5)

# CHALLENGE ANSWER
def count_trainable(m):
    return sum(p.numel() for p in m.parameters() if p.requires_grad)

print(f"Frozen ResNet: {count_trainable(resnet)}") # Only the head
for p in resnet.parameters():
    p.requires_grad = True # Unfreeze
print(f"Unfrozen ResNet: {count_trainable(resnet)}") # Full model

print("\n--- Why it works ---")
print("1. Knowledge Reuse: Visual concepts like 'edges' and 'circles' are universal; they work for identifying cells in a microscope just as well as cars on a street.")
print("2. Accessibility: Transfer learning allows individuals to build world-class AI models without needing an $8,000 GPU or a million-image dataset.")
print("3. Speed: Fine-tuning usually takes minutes or hours, whereas training from scratch takes days or weeks.")
print("4. Robustness: Pre-trained models are often more robust to noise because they've seen such a massive variety of data during their first training phase.")
