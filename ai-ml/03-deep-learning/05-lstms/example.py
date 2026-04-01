# example.py - Building an LSTM with PyTorch

import torch
import torch.nn as nn

# 1. Defining the LSTM
class MultiLayerLSTM(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers=1):
        super(MultiLayerLSTM, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        # The LSTM layer
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        # Final output
        self.fc = nn.Linear(hidden_size, 1)

    def forward(self, x):
        # Initial states (h0 and c0)
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(x.device)
        c0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(x.device)
        
        # out: [batch, seq, hidden]
        out, (hn, cn) = self.lstm(x, (h0, c0))
        
        # Take the last time step's output
        return self.fc(out[:, -1, :])

# 2. Simulated Sequence (10 steps)
X = torch.randn(2, 10, 5) # batch=2, seq=10, features=5

# 3. Model Inference
model = MultiLayerLSTM(5, 32, num_layers=2)
with torch.no_grad():
    prediction = model(X)

print("--- LSTM Output ---")
print(f"Prediction Shape: {prediction.shape}")
print(f"Sample Prediction: {prediction[0].item():.4f}")
