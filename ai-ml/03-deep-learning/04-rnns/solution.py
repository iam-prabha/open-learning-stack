# solution.py - RNN answers

import torch
import torch.nn as nn

# TODO 1
rnn = nn.RNN(input_size=10, hidden_size=20, batch_first=True)

# TODO 2
class ManyToOneRNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.rnn = nn.RNN(5, 16, batch_first=True)
        self.fc = nn.Linear(16, 1)
    def forward(self, x):
        _, h_n = self.rnn(x) # h_n is the final hidden state
        return torch.sigmoid(self.fc(h_n.squeeze(0)))

# TODO 3
# Answer: (1, 8, 20) -> (num_layers, batch, hidden_size)

# TODO 4
# Answer: Due to the Vanishing Gradient problem. Multiplying 
# gradients across hundreds of layers causes them to shrink 
# to effectively zero, stopping the early weights from learning.

# TODO 5
# Answer: (Batch, Seq, Feature)

# TODO 6
h_prev = torch.tensor([0.1])
x = torch.tensor([1.0])
Wh, Wx = 0.5, 1.0
h_new = torch.tanh(Wh * h_prev + Wx * x)
print(f"New Hidden State: {h_new.item():.4f}")

# CHALLENGE ANSWER
class ManyToManyRNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.rnn = nn.RNN(input_size=1, hidden_size=10, batch_first=True)
        self.fc = nn.Linear(10, 1)
    def forward(self, x):
        out, _ = self.rnn(x)
        # Apply the Linear layer to EVERY time step output
        return self.fc(out)

print("\n--- Why it works ---")
print("1. Context: RNNs keep a 'rolling average' of what they've seen, allowing them to process context like 'The cat... it'.")
print("2. Shared Weights: The same RNN cell is used for every time step, reducing the number of parameters significantly.")
print("3. Flexibility: RNNs can handle inputs of any length (though they struggle with long ones).")
print("4. Foundation: RNN concepts paved the way for advanced sequence models like LSTMs and eventually Transformers.")
