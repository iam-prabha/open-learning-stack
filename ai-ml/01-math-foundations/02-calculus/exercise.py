# exercise.py - Practice with Calculus

import torch

# TODO 1: Find the derivative of f(x) = 3x^2 + 10x 
# at the point x = 5.
# (Calculus check: f'(x) = 6x + 10 = 6*5 + 10 = 40)

# TODO 2: Create a function g(x) = sin(x) and use 
# a tiny 'h' (e.g. 0.0001) to approximate its 
# derivative at x = 0.
def g(x):
    # return ...
    return 0

# TODO 3: Which math concept allows us to find 
# the 'Direction of Steepest Ascent' for a multi-input function?
# Answer: ...

# TODO 4: Find the gradient of h(x, y, z) = x*y + z 
# at the point (1, 2, 3) using PyTorch.

# TODO 5: What is the 'Chain Rule' in plain English?
# Answer: ...

# TODO 6: If the derivative of our Loss function 
# with respect to a weight is POSITIVE, should we 
# INCREASE or DECREASE that weight to lower the loss?
# Answer: ...

# CHALLENGE: Manually calculate the derivative of 
# f(g(x)) where f(u) = u^2 and g(x) = x + 3 
# at x = 2.
# (Hint: Use the Chain Rule: f'(g(x)) * g'(x))

# --- Verification ---
print("--- Results ---")
# Check your calculus logic vs the solution!
