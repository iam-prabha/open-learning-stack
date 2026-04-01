# example.py - Building a Perceptron with PyTorch

import torch
import torch.nn as nn

# 1. Defining the Perceptron
# In PyTorch, a single perceptron is a Linear layer with 1 output
class Perceptron(nn.Module):
    def __init__(self, input_size):
        super(Perceptron, self,"" ).__init__()
        # 1 output neuron, with a bias term enabled by default
        self.fc = nn.Linear(input_size, 1)
        # Activation function (Sigmoid for binary probability)
        self.activation = nn.Sigmoid()

    def forward(self, x):
        return self.activation(self.fc(x))

# 2. Simulated Data (binary logic gate: AND)
# In an AND gate, output is 1 only if both inputs are 1
X = torch.tensor([[0., 0.], [0., 1.], [1., 0.], [1., 1.]])
y = torch.tensor([[0.], [0.], [0.], [1.]])

# 3. Training Loop (Overview)
model = Perceptron(input_size=2)
criterion = nn.BCELoss() # Binary Cross Entropy Loss
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)

print("--- Initial Predictions ---")
with torch.no_grad():
    print(model(X))

# 4. Train for 100 epochs
for epoch in range(100):
    # Zero gradients
    optimizer.zero_grad()
    # Forward pass
    outputs = model(X)
    loss = criterion(outputs, y)
    # Backward pass
    loss.backward()
    # Update weights
    optimizer.step()

print("\n--- Final Predictions (After Training) ---")
with torch.no_grad():
    final_out = model(X)
    print(final_out)
    print("Interpretation: values > 0.5 are 'True'")
