# solution.py - Perceptron answers

import torch
import torch.nn as nn

# TODO 1
def forward_pass(x, w, b):
    # x is tensor of [x1, x2], w is [w1, w2]
    return torch.dot(x, w) + b

# TODO 2
def manual_sigmoid(z):
    return 1 / (1 + torch.exp(-z))

# TODO 3
class MultiInputPerceptron(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = nn.Linear(4, 1)
    def forward(self, x):
        return torch.sigmoid(self.fc(x))

# TODO 4
model = MultiInputPerceptron()
print(f"Weights: {model.fc.weight}")

# TODO 5
loss_fn = nn.BCELoss()
pred = torch.tensor([0.8])
target = torch.tensor([1.0])
print(f"Loss: {loss_fn(pred, target)}")

# TODO 6
# Answer: The XOR gate. It is not linearly separable, 
# meaning you cannot draw a single straight line to 
# separate the '0' results from the '1' results.

# CHALLENGE ANSWER
X_or = torch.tensor([[0., 0.], [0., 1.], [1., 0.], [1., 1.]])
y_or = torch.tensor([[0.], [1.], [1.], [1.]])

m = nn.Sequential(nn.Linear(2, 1), nn.Sigmoid())
opt = torch.optim.SGD(m.parameters(), lr=0.1)

for _ in range(200):
    opt.zero_grad()
    loss = nn.BCELoss()(m(X_or), y_or)
    loss.backward()
    opt.step()

print("\n--- OR Gate Results ---")
print(m(X_or))

print("\n--- Why it works ---")
print("1. Linearity: Perceptrons create a linear decision boundary (a hyperplane in high dimensions).")
print("2. Activation: The nonlinear activation function (like Sigmoid) allows the network to represent probabilities.")
print("3. Learning: By calculating the gradient of the loss, we know exactly how to nudge each weight to make the error smaller.")
print("4. Foundation: Every complex Deep Learning model in existence is just many perceptrons stacked and connected together.")
