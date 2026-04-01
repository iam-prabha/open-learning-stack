# example.py - Derivatives & Gradients in Python

# 1. Manual Derivative (Approximation)
# f'(x) = [f(x + h) - f(x)] / h  (where h is tiny)
def f(x):
    return x**2

def get_derivative(func, x, h=0.0001):
    return (func(x + h) - func(x)) / h

x_val = 3.0
approx_grad = get_derivative(f, x_val)
# Math: f'(x) = 2x, f'(3) = 6.0
print(f"Approximated Derivative of x^2 at x=3: {approx_grad:.4f}")

# 2. Partial Derivatives (Gradient)
# f(x, y) = x^2 + y^3
# Gradient at (x,y) is [df/dx, df/dy]
# df/dx = 2x, df/dy = 3y^2

def partial_x(x, y): return 2*x
def partial_y(x, y): return 3*(y**2)

x, y = 2.0, 1.0
grad = [partial_x(x, y), partial_y(x, y)] # [4.0, 3.0]
print(f"\nGradient of x^2 + y^3 at (2, 1): {grad}")

# 3. Using Autograd (The Modern Way)
import torch
x_tensor = torch.tensor(2.0, requires_grad=True)
y_tensor = torch.tensor(1.0, requires_grad=True)

func = x_tensor**2 + y_tensor**3
func.backward()

print(f"\nPyTorch result:")
print(f"df/dx: {x_tensor.grad.item()}")
print(f"df/dy: {y_tensor.grad.item()}")
