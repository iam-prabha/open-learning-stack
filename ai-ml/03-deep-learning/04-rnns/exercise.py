# exercise.py - Practice with RNNs

import torch
import torch.nn as nn

# TODO 1: Create an RNN layer with:
# - input_size: 10
# - hidden_size: 20
# - batch_first: True
rnn = None # nn.RNN(...)

# TODO 2: Create a 'Many-to-One' RNN model that takes 
# a sequence of 10 words (each a vector of 5) and 
# predicts 1 output class (binary).

# TODO 3: What is the shape of the initial hidden 
# state 'h0' for a 1-layer RNN with batch_size=8 
# and hidden_size=20?
# Answer: (..., ..., ...)

# TODO 4: Why do RNNs struggle with sequences that 
# are hundreds of words long?
# Answer: ...

# TODO 5: If 'batch_first=True', what is the expected 
# shape of the input tensor X?
# Answer: (Batch, Seq, Feature) or (Seq, Batch, Feature)?

# TODO 6: Use 'torch.tanh' to manually update a 
# hidden state 'h_prev' given input 'x' and 
# weight 'Wh = 0.5', 'Wx = 1.0'.
h_prev = torch.tensor([0.1])
x = torch.tensor([1.0])
# h_new = ...

# CHALLENGE: Modify the 'SimpleRNN' from example.py 
# to be 'Many-to-Many'. It should return a prediction 
# for EVERY time step in the sequence.
# (Hint: Don't slice 'out[:, -1, :]')

# --- Verification ---
print("--- Results ---")
# Check your sequence logic vs the solution!
