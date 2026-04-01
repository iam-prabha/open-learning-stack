# solution.py - Backpropagation answers

import torch

# TODO 1 & 2
x = torch.tensor(3.0, requires_grad=True)
y = (x + 2)**2

# TODO 3
y.backward()

# TODO 4
print(f"Gradient dy/dx at x=3: {x.grad}")

# TODO 5
# Answer: Gradients in PyTorch are accumulated (summed up) 
# by default. If we don't zero them, the gradient for the 
# next step will include the gradient from the previous 
# step, leading to incorrect updates.

# TODO 6
# Answer: It will throw a 'RuntimeError'. Once .backward() 
# is called, the computation graph is usually destroyed 
# to save memory.

# CHALLENGE ANSWER
w = torch.tensor(1.0, requires_grad=True)
x_val = torch.tensor(2.0)
target = torch.tensor(10.0)

# Step
pred = w * x_val
loss = (pred - target)**2
loss.backward()

with torch.no_grad():
    w -= 0.1 * w.grad
    print(f"\nUpdated w: {w.item():.4f}")
    # Math: L = (2w - 10)^2, dL/dw = 2*(2w - 10)*2 = 4(2w - 10)
    # at w=1: 4(2-10) = -32.0
    # w = 1.0 - 0.1*(-32.0) = 1.0 + 3.2 = 4.2

print("\n--- Why it works ---")
print("1. Connectivity: Backpropagation allows us to calculate how much a single pixel in an image 'caused' a mistake in the final classification.")
print("2. Scalability: The chain rule works just as well for 10 weights as it does for 10 billion weights in a large language model.")
print("3. Automation: Thanks to computational graphs, developers no longer have to manually solve high-dimensional derivative equations.")
print("4. Efficiency: By moving backward, we only visit each 'node' in the graph once, making the process O(N).")
