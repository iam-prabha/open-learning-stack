# solution.py - Optimization answers

import numpy as np

# TODO 1
# Gradient at w=0: 2(0) + 4 = 4
print(f"Gradient at 0: 4")

# TODO 2
# w_new = 0 - (0.1 * 4) = -0.4
print(f"Next Weight: -0.4")

# TODO 3
# Answer: SGD updates the model weights after seeing 
# ONLY ONE data point at a time, making it faster and 
# more 'noisy' than standard batch descent.

# TODO 4
# Answer: The model will take a very long time to 
# converge (reach the minimum), wasting compute power.

# TODO 5
# General logic: velocity = momentum * prev_velocity + lr * grad
# w = w - velocity

# TODO 6
# Answer: MSE is always positive and 'penalizes' large 
# errors more than small ones (due to the squaring), 
# making it very effective for optimization.

# CHALLENGE ANSWER
w = 10.0
lr = 0.1
steps = 0
while w**2 > 0.001:
    grad = 2*w
    w = w - lr * grad
    steps += 1
print(f"Converged at w={w:.4f} in {steps} steps")

print("\n--- Why it works ---")
print("1. Automation: Optimization is the 'Robot' that actually does the training while you sleep.")
print("2. Mathematical Elegance: It turns the subjective question 'is this a good model?' into a mathematical problem with a single best answer.")
print("3. Robustness: Modern optimizers (like Adam) can handle incredibly complex functions with millions of inputs and still find a good solution.")
print("4. Result Orientated: At the end of the day, AI only cares about minimizing error—Optimization is exactly how that happens.")

export {};
