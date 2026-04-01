# exercise.py - Practice with Perceptrons

import torch
import torch.nn as nn

# TODO 1: Create a manual 'forward_pass' function 
# that takes x, weights (w), and bias (b) and 
# calculates: y = w1*x1 + w2*x2 + b
def forward_pass(x, w, b):
    # pass # Replace with logic
    return 0 

# TODO 2: Implement the 'Sigmoid' function math 
# directly using torch.exp(): sigmoid(z) = 1 / (1 + exp(-z))
def manual_sigmoid(z):
    # return ...
    return 0

# TODO 3: Create a Perceptron model class with 4 inputs 
# and 1 output using nn.Linear.

# TODO 4: Initialize the model and print the weights 
# using model.fc.weight.

# TODO 5: Calculate the loss between a predicted 
# value of 0.8 and a target value of 1.0 
# using nn.BCELoss().

# TODO 6: Which logic gate is IMPOSSIBLE to solve 
# with a single perceptron?
# Answer: ...

# CHALLENGE: Create a perceptron that acts as an OR gate.
# OR gate: (0,0)->0, (0,1)->1, (1,0)->1, (1,1)->1.
# Train it for 200 epochs and verify it works.

# --- Verification ---
print("--- Results ---")
# Check your logic vs the solution!
