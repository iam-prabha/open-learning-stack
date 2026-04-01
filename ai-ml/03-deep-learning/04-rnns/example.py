# example.py - Building an RNN with PyTorch

import torch
import torch.nn as nn

# 1. Defining the RNN
class SimpleRNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleRNN, self).__init__()
        self.hidden_size = hidden_size
        # The RNN layer
        self.rnn = nn.RNN(input_size, hidden_size, batch_first=True)
        # Final output layer
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        # x shape: [batch, sequence_length, input_size]
        # h0: Initial hidden state [num_layers, batch, hidden_size]
        h0 = torch.zeros(1, x.size(0), self.hidden_size).to(x.device)
        
        # out: [batch, sequence_length, hidden_size]
        out, _ = self.rnn(x, h0)
        
        # We only care about the LAST output of the sequence (Many-to-One)
        out = self.fc(out[:, -1, :])
        return out

# 2. Simulated Sequential Data (Stock Price over 5 days)
# batch=1, seq_len=5, features=1 (price)
X = torch.randn(1, 5, 1)

# 3. Model Inference
model = SimpleRNN(input_size=1, hidden_size=10, output_size=1)
with torch.no_grad():
    prediction = model(X)

print("--- RNN Output ---")
print(f"Predicted value for day 6: {prediction.item():.4f}")
print(f"Final shape: {prediction.shape}")
