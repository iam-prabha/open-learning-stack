# Optimization: Finding the Minimum Error

## What is it?

**Optimization** is the final step where all the math comes together. We use Linear Algebra to store data, Calculus to find the slope of the error, and Probability to handle uncertainty. Optimization is the actual process of adjusting the model's weights to find the "Global Minimum" — the point where the error (Loss) is as low as possible.

## Real-world analogy

Think of Optimization like **tuning a radio in a car**:
- **Loss Function**: How much "Static" (Noise) you hear.
- **Weights**: The knobs you turn. 
- **Learning Rate**: How fast you turn the knobs. 
    - Too fast, and you skip over the clear station. 
    - Too slow, and it takes an hour to find it.
- **Gradient Descent**: The strategy of turning the knob in the direction that reduces the static.

## When to use it

| Feature | Use when... | Avoid when... |
|---|---|---|
| **Gradient Descent** | Training any deep neural network | The problem is tiny enough for an "Exact" solution (like simple Linear Regression) |
| **SGD** | Working with massive datasets that don't fit in memory | You have a small dataset (Batch GD is more stable) |
| **Adam/RMSprop** | Dealing with complex, non-linear loss landscapes | You want the simplest possible implementation |

## Common mistakes

1. **Learning Rate too high** — The weights "bounce" back and forth, never settling into the minimum. The loss might even start to increase!
2. **Getting trapped in a Local Minimum** — Thinking you've found the best possible version of your model, when a much better one exists on the other side of an "error hill."
3. **Plateaus** — The gradient becomes very small, making the optimizer feel like it's done even though it's still far from the goal.

## Files in this folder

| File | Purpose |
|---|---|
| `example.py` | Implementation of Gradient Descent from scratch |
| `notebook.ipynb` | Visualizing the "Loss Landscape" and Optimization path |
| `exercise.py` | 6 TODOs + 1 challenge |
| `solution.py` | Answers with WHY comments |

## Go deeper

- [Visualizing Gradient Descent — Distill.pub](https://distill.pub/2017/momentum/)
- [Optimization Algorithms in Deep Learning — Stanford CS231n](https://cs231n.github.io/neural-networks-3/#sgd)
