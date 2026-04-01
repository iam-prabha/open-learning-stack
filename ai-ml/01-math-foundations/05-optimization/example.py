# example.py - Gradient Descent from Scratch

import numpy as np

# 1. Defining the Loss Function (Equation: f(w) = w^2 - 10w + 25)
# Note: This is (w - 5)^2, so the minimum is at w=5.
def loss_func(w):
    return w**2 - 10*w + 25

def get_gradient(w):
    return 2*w - 10

# 2. Gradient Descent Loop
def optimize(start_w, lr, epochs):
    current_w = start_w
    print(f"Starting at w = {current_w}, Loss = {loss_func(current_w):.4f}")
    
    for i in range(epochs):
        # Calculate slope
        grad = get_gradient(current_w)
        # Nudge w in the opposite direction of the slope
        current_w = current_w - (lr * grad)
        
        if (i + 1) % 10 == 0:
            print(f"Epoch {i+1}: w = {current_w:.4f}, Loss = {loss_func(current_w):.4f}")
            
    return current_w

# 3. Running the Optimizer
# Start at 0, walk with lr of 0.1
final_w = optimize(start_w=0.0, lr=0.1, epochs=50)

print(f"\nFinal optimized w: {final_w:.4f} (Goal was 5.0)")
print("--- Result achieved! ---")
