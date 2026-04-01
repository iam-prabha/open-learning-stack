# solution.py - LSTM answers

import torch
import torch.nn as nn

# TODO 1
lstm = nn.LSTM(16, 32, num_layers=2, batch_first=True)

# TODO 2
# Answer: The Hidden State (h_t) and the Cell State (c_t)

# TODO 3
# Answer: The Forget Gate decides which information from 
# the previous cell state should be discarded (using a 
# Sigmoid function that outputs 0-1).

# TODO 4
h0 = torch.zeros(1, 4, 32)
c0 = torch.zeros(1, 4, 32)

# TODO 5
# Answer: Because the Cell State allows information to flow 
# through the entire sequence with very few linear updates, 
# preventing gradients from vanishing even over long distances.

# TODO 6
# Answer: (2, 10, 32) -> (Batch, Seq, Hidden)

# CHALLENGE ANSWER
m = nn.LSTM(16, 32, bidirectional=True, batch_first=True)
x = torch.randn(2, 10, 16)
out, (hn, cn) = m(x)
print(f"Bidirectional Output Shape: {out.shape}") # [2, 10, 64]
print(f"Bidirectional Hidden State Shape: {hn.shape}") # [2, 2, 32]
# Answer: The hidden size is effectively doubled in 'out' 
# because it combines the forward and backward passes.

print("\n--- Why it works ---")
print("1. Control: Gates give the network 'agency' over its memory, allowing it to preserve long-term context.")
print("2. Stability: By additive updates to the cell state, LSTMs avoid the exponential gradient problems of vanilla RNNs.")
print("3. Versatility: LSTMs power many real systems today, from machine translation to predictive maintenance.")
print("4. Legacy: Even though Transformers are now the state-of-the-art, LSTMs remain crucial for edge devices and low-latency apps.")
