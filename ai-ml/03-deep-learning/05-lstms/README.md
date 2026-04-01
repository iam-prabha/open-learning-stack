# Long Short-Term Memory (LSTMs)

## What is it?

**LSTMs** are a more advanced version of Recurrent Neural Networks (RNNs) designed to solve the "Short-term Memory" problem. While standard RNNs lose track of information from the beginning of a long sequence, LSTMs use a specialized internal structure called **Gates** to decide which information is important to "Remember" and which can be "Forgotten."

## Real-world analogy

Think of an LSTM like **a professional researcher taking notes on a long book**:
- **Cell State (The Notebook)**: The core record of the story. It flows through the whole process with only minor changes.
- **Forget Gate (The Eraser)**: The researcher decides what's no longer relevant ("The character we just met died; forget their eye color").
- **Input Gate (The Pen)**: The researcher adds new important facts to the notebook ("The hero found a magic sword").
- **Output Gate (The Summary)**: At any point, if you ask "What's happening?", the researcher looks at the notebook and his current thoughts to give you a summary.

## When to use it

| Feature | Use when... | Avoid when... |
|---|---|---|
| **LSTM** | Long-form text generation (e.g., writing a story) | Very short sequences (standard RNNs are faster) |
| **LSTM** | Complex time-series with long-term seasonal patterns (e.g., yearly energy consumption) | Data with no temporal structure (e.g., identifying a cat in a photo) |

## Common mistakes

1. **Over-parameterization** — LSTMs have 4x the parameters of an RNN. For small datasets, they can overfit very easily.
2. **Hidden State Initialization** — Not resetting the `h0` and `c0` states between unrelated batches, causing "Memory Leak" from the previous data.
3. **Using too many layers** — Stacking 10 LSTM layers. This makes the model extremely hard to train and slow to run. Usually, 2-3 layers are enough.

## Files in this folder

| File | Purpose |
|---|---|
| `example.py` | Building and running an LSTM in PyTorch |
| `notebook.ipynb` | Visualizing the Forget/Input/Output gates |
| `exercise.py` | 6 TODOs + 1 challenge |
| `solution.py` | Answers with WHY comments |

## Go deeper

- [Understanding LSTM Networks — Colah's Blog](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)
- [PyTorch LSTM Documentation](https://pytorch.org/docs/stable/generated/torch.nn.LSTM.html)
