# exercise.py - Practice with LSTMs

import torch
import torch.nn as nn

# TODO 1: Create an LSTM layer with:
# - input_size: 16
# - hidden_size: 32
# - num_layers: 2
# - batch_first: True

# TODO 2: What are the two states maintained by an 
# LSTM during its forward pass?
# Answer: ... and ...

# TODO 3: What is the purpose of the 'Forget Gate'?
# Answer: ...

# TODO 4: Initialize the initial states 'h0' and 'c0' 
# for a batch of 4 sequences, with 32 hidden units 
# and 1 layer.

# TODO 5: Why is the 'Cell State' (c_t) called the 
# 'Memory Highway'?
# Answer: ...

# TODO 6: Given an input [2, 10, 16], what is the 
# shape of the 'out' variable from an LSTM?
# Answer: (..., ..., ...)

# CHALLENGE: Create a bidirectional LSTM and print 
# the shape of its hidden state. How does it differ 
# from a single-directional one?

# --- Verification ---
print("--- Results ---")
# Check your architecture logic vs the solution!
