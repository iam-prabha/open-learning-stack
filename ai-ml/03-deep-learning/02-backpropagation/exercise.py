# exercise.py - Practice with Backpropagation

import torch

# TODO 1: Create a tensor 'x' with value 3.0 and 
# enable 'requires_grad=True'.

# TODO 2: Define a function y = (x + 2)^2.

# TODO 3: Calculate the gradient of y with respect 
# to x using .backward().

# TODO 4: Print the value of x.grad. 
# (Mathematical check: d/dx((x+2)^2) = 2*(x+2) = 2*(3+2) = 10)

# TODO 5: Why must we call 'optimizer.zero_grad()' 
# at the start of every training loop?
# Answer: ...

# TODO 6: What happens if you try to call .backward() 
# a second time on the same output without passing 
# 'retain_graph=True'? 
# Answer: ...

# CHALLENGE: Manually implement a single Step of 
# Gradient Descent for a model y = w*x.
# x=2.0, target=10.0, current_w=1.0, learning_rate=0.1.
# 1. Forward pass
# 2. Compute Loss (y - target)^2
# 3. Backward pass
# 4. Update w: w = w - lr * w.grad

# --- Verification ---
print("--- Results ---")
# Check your gradients vs the solution!
