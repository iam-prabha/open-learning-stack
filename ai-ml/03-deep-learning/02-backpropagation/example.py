# example.py - Backpropagation Mechanics

import torch

# 1. Manual Chain Rule (The Logic)
# Let's say we have y = x^2 * 3
# Step 1: a = x^2
# Step 2: y = a * 3
# Gradient of y with respect to x (dy/dx) = (dy/da) * (da/dx)
# dy/da = 3
# da/dx = 2x
# Result = 3 * 2x = 6x

x_val = 2.0
manual_gradient = 6 * x_val # = 12.0
print(f"Manual Gradient: {manual_gradient}")

# 2. PyTorch Autograd (The Automation)
x = torch.tensor(2.0, requires_grad=True)
a = x**2
y = a * 3

y.backward()
print(f"PyTorch Gradient: {x.grad.item()}")

# 3. Real-world example (Simple Linear regression update)
# Loss = (pred - target)^2
w = torch.tensor(1.0, requires_grad=True)
b = torch.tensor(0.5, requires_grad=True)
input_data = torch.tensor(1.5)
target = torch.tensor(2.5)

# Forward pass
pred = w * input_data + b
loss = (pred - target)**2

# Backward pass
loss.backward()

print("\n--- Model Gradients ---")
print(f"dL/dw: {w.grad}")
print(f"dL/db: {b.grad}")

# Weight update (manual implementation of SGD step)
with torch.no_grad():
    w -= 0.1 * w.grad
    b -= 0.1 * b.grad
    print(f"\nUpdated w: {w.item():.4f}")
    print(f"Updated b: {b.item():.4f}")
