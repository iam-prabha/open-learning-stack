# Probability: Measuring Uncertainty

## What is it?

Machine Learning is never 100% certain. When an AI says "this is a cat," it actually means "there is a 98% **probability** that this is a cat." Probability is the mathematical study of uncertainty and the likelihood of different events occurring.

## Real-world analogy

Think of Probability like **the weather forecast**:
- **Event**: "It will rain tomorrow."
- **Probability**: 30% chance.
- **Conditional Probability**: "If I see dark clouds (Observation), how does that change the chance of rain?"
- **Bayes' Theorem**: Updating your beliefs based on new evidence. You thought it wouldn't rain (Prior), you saw clouds (Evidence), now you think it probably will rain (Posterior).

## When to use it

| Feature | Use when... | Avoid when... |
|---|---|---|
| **Bayes' Theorem** | Building a spam filter (given these words, what is the probability this is spam?) | You have a simple "If-Else" rule that never changes |
| **Normal Dist** | Modeling continuous data like heights, weights, or stock returns | The data is binary (Yes/No) or sparse (mostly zeros) |
| **Bernoulli Dist** | Modeling binary outcomes like coin flips or clicking an ad | The outcome has many categories |

## Common mistakes

1. **Confusing 'P(A|B)' with 'P(B|A)'** — The probability that someone has a disease given they test positive is NOT the same as the probability they test positive given they have the disease. (This is the "Prosecutor's Fallacy").
2. **Ignoring the Prior** — Thinking a rare disease is likely just because a test is 99% accurate. If only 1 in 1M people have it, the test is likely a false positive.
3. **Independent vs Dependent** — Assuming two events don't affect each other (like two coin flips) when they actually do (like drawing two cards from a deck without replacement).

## Files in this folder

| File | Purpose |
|---|---|
| `example.py` | Bayes' Theorem and Coin Flip Simulations |
| `notebook.ipynb` | Visualizing Distributions (Normal vs Uniform) |
| `exercise.py` | 6 TODOs + 1 challenge |
| `solution.py` | Answers with WHY comments |

## Go deeper

- [Probability Theory — Khan Academy](https://www.khanacademy.org/math/probability)
- [Bayes' Theorem Visualized — 3Blue1Brown](https://www.youtube.com/watch?v=HZGCoVF3YvM)
