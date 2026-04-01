# Calculus: The Engine of Learning

## What is it?

If Linear Algebra is the "language" of AI, **Calculus** is the "engine." Specifically, we use **Differential Calculus** to figure out how a small change in one number (like a weight) affects another number (like the error). This allows us to "optimize" our models by nudging them in the right direction.

## Real-world analogy

Think of Calculus like **an altimeter on a foggy mountain**:
- **The Mountain**: The "Loss Landscape" (how wrong your model is).
- **The Peak**: Maximum error.
- **The Valley**: Minimum error (where you want to be).
- **The Derivative**: The slope of the ground right beneath your feet. Even if the fog is thick and you can't see the valley, you can feel if the ground is sloping *down* or *up*.
- **The Gradient**: A vector that points in the direction of the steepest *upward* slope. To learn, we walk in the *opposite* direction.

## When to use it

| Feature | Use when... | Avoid when... |
|---|---|---|
| **Derivative** | You want to know how fast a value is changing | You are only interested in a snapshot of a static value |
| **Partial Derivative**| Your function has multiple inputs (like a model with 1B weights) | You only have one input variable |
| **Chain Rule** | You need to find the impact of a change at the very beginning of a long process | Your process is a single, simple step |

## Common mistakes

1. **Local Minima** — Getting stuck in a small "dip" on the mountain and thinking you've reached the valley, when the real minimum is further down.
2. **Learning Rate Errors** — Walking too fast (stepping over the valley) or too slow (taking forever to reach it) based on the slope.
3. **Vanishing Gradients** — The slope becomes so flat that you stop moving entirely, even if you are nowhere near the valley.

## Files in this folder

| File | Purpose |
|---|---|
| `example.py` | Calculating Derivatives and Gradients in Code |
| `notebook.ipynb` | Visualizing Slope and Tangent Lines |
| `exercise.py` | 6 TODOs + 1 challenge |
| `solution.py` | Answers with WHY comments |

## Go deeper

- [Essence of Calculus — 3Blue1Brown](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)
- [Calculus for Machine Learning — Khan Academy](https://www.khanacademy.org/math/multivariable-calculus)
