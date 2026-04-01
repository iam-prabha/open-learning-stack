# Backpropagation & The Chain Rule

## What is it?

**Backpropagation** is the way neural networks learn from their mistakes. It's a method for calculating the "gradient" (slope) of the loss function with respect to every single weight in the network. By using the **Chain Rule** from calculus, we can trace the error from the output layer all the way back to the input layer, figuring out exactly which weights caused the error.

## Real-world analogy

Think of backpropagation like **a supervisor giving feedback at a pizza shop**:
- **Output (The Pizza)**: The pizza arrives cold and salty (The Error/Loss).
- **Forward Pass**: The dough was made, the sauce added, and it was baked in that order.
- **Backpropagation (The Supervisor)**: The supervisor works backward. 
    1. He tells the Delivery Person: "Drive faster" (Adjusting output weights).
    2. He tells the Baker: "Check the oven temperature" (Adjusting middle weights).
    3. He tells the Chef: "Use less salt" (Adjusting input weights).
- **Optimization**: Next time, the kitchen works slightly differently to produce a better pizza.

## When to use it

| Feature | Use when... | Avoid when... |
|---|---|---|
| **Backprop** | Training any multi-layer neural network (MLP, CNN, Transformer) | Using simple algorithms like Linear Regression or KNN (they have simpler ways to calculate parameters) |
| **Autograd** | Using frameworks like PyTorch or TensorFlow to handle the math automatically | You want to build a customized, high-performance specialized layer from scratch (manual gradients might be faster) |

## Common mistakes

1. **Vanishing Gradients** — In very deep networks, the gradients can become so small that the weights at the early layers never change. This is often solved by using ReLU or LSTM architectures.
2. **Exploding Gradients** — The opposite of vanishing; the gradients become so large they cause the weights to "orbit" around infinity, crashing the training.
3. **Forgetting to Zero Grads** — In PyTorch, gradients accumulate by default. If you don't call `optimizer.zero_grad()`, your new gradient adds to the old one, leading to nonsensical results.

## Files in this folder

| File | Purpose |
|---|---|
| `example.py` | Manual backprop in NumPy vs. Auto-grad in PyTorch |
| `notebook.ipynb` | Visualizing the Gradient Descent path |
| `exercise.py` | 6 TODOs + 1 challenge |
| `solution.py` | Answers with WHY comments |

## Go deeper

- [Backpropagation — 3Blue1Brown (Video)](https://www.youtube.com/watch?v=Ilg3gGewQ5U)
- [PyTorch Autograd Tutorial](https://pytorch.org/tutorials/beginner/blitz/autograd_tutorial.html)
