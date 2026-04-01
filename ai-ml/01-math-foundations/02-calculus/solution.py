# solution.py - Calculus answers

import torch
import math

# TODO 1
x = torch.tensor(5.0, requires_grad=True)
f = 3*(x**2) + 10*x
f.backward()
print(f"Derivative at x=5: {x.grad.item()}")

# TODO 2
def g(x):
    return math.sin(x)
h = 0.0001
x_val = 0.0
approx_deriv = (g(x_val + h) - g(x_val)) / h
print(f"Approx derivative of sin(0): {approx_deriv:.4f}")

# TODO 3
# Answer: The Gradient vector (denoted by the 'nabla' symbol ∇)

# TODO 4
x = torch.tensor(1.0, requires_grad=True)
y = torch.tensor(2.0, requires_grad=True)
z = torch.tensor(3.0, requires_grad=True)
h_func = x*y + z
h_func.backward()
print(f"Gradient at (1,2,3): x={x.grad}, y={y.grad}, z={z.grad}")

# TODO 5
# Answer: If something affects something else through 
# a middle step, you just multiply their rates of 
# change together. (e.g. rate of change of y over x 
# = rate of change of y over u * rate of change of u over x)

# TODO 6
# Answer: DECREASE. A positive derivative means the 
# function is sloping UP. To go DOWN (lower the loss), 
# you move in the opposite direction of the slope.

# CHALLENGE ANSWER
# f(u) = u^2 -> f'(u) = 2u
# g(x) = x + 3 -> g'(x) = 1
# u = g(2) = 5
# Chain rule: f'(5) * g'(2) = 2(5) * 1 = 10
print(f"Chain rule result: {10}")

print("\n--- Why it works ---")
print("1. Directional Guidance: Without calculus, machine learning would just be 'guessing' random weights until it worked. Calculus gives us a compass.")
print("2. Optimization: We don't solve for the best weights once; we take thousands of small 'steps' down the gradient until the model stops failing.")
print("3. Universal Applicability: The chain rule allows us to calculate gradients for networks with billions of parameters by just stringing small derivatives together.")
print("4. Biological Inspiration: Our brains do something similar; when you burn your hand, the 'negative feedback' tells your brain to move your hand away from the source.")

export {};
