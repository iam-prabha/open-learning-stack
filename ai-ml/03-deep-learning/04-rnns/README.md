# Recurrent Neural Networks (RNNs)

## What is it?

**RNNs** are a type of neural network designed for **sequential data**, where the order of information matters. Unlike standard networks that treat every input independently, RNNs have a "Hidden State" (a memory) that allows them to pass information from one step of the sequence to the next.

## Real-world analogy

Think of an RNN like **someone reading a sentence**:
- **Wait, why?**: To understand the word "it" in the sentence "The cat sat on the mat, it was happy," you have to **remember** the word "cat" from earlier.
- **Hidden State (The Memory)**: As you read each word, you update your mental image of the sentence.
- **Input**: The current word you are looking at.
- **Output**: Your understanding of the sentence so far.
- **Limitation**: If the sentence is extremely long (like a whole book), you might forget the beginning by the time you reach the end (Vanishing Gradient).

## When to use it

| Feature | Use when... | Avoid when... |
|---|---|---|
| **RNN** | Time-series forecasting (Stock prices, weather data) | Static data like image classification (CNNs are better) |
| **RNN** | Simple text generation or Part-of-Speech tagging | Extremely long documents (LSTMs or Transformers are better) |

## Common mistakes

1. **Exploding/Vanishing Gradients** — The "gradient" used to update weights shrinks or grows exponentially as it's multiplied through many time steps.
2. **Hidden State Management** — Forgetting that the hidden state needs to be "reset" between different sequences during training.
3. **Many-to-Many vs. Many-to-One** — Choosing the wrong architecture for your problem (e.g., trying to use a "Many-to-One" network to translate a sentence word-by-word).

## Files in this folder

| File | Purpose |
|---|---|
| `example.py` | Simple RNN for time-series prediction |
| `notebook.ipynb` | Visualizing Hidden States and Unrolling |
| `exercise.py` | 6 TODOs + 1 challenge |
| `solution.py` | Answers with WHY comments |

## Go deeper

- [The Unreasonable Effectiveness of RNNs — Andrej Karpathy](http://karpathy.github.io/2015/05/21/rnn-effectiveness/)
- [Understanding RNNs — PyTorch Docs](https://pytorch.org/docs/stable/generated/torch.nn.RNN.html)
