# Convolutional Neural Networks (CNNs)

## What is it?

**CNNs** are a specialized type of neural network designed to process data that has a grid-like topology, such as images (2D grid of pixels). Instead of looking at every pixel individually, CNNs use **Convolutional Layers** to slide small filters across the image to detect patterns like edges, textures, and eventually complex objects.

## Real-world analogy

Think of a CNN like **a detective examining a crime scene with a magnifying glass**:
- **The Filter (The Glass)**: The detective doesn't look at the whole room at once. He slides a small glass over specific spots.
- **Feature Map**: If he sees a "Fingerprint," he makes a note of its location.
- **Pooling (Summarizing)**: Instead of remembering every single detail, he summarizes: "There's a thumbprint in the Northwest corner." 
- **Hierarchy**: 
    - Layer 1 sees **Lines** (edges).
    - Layer 2 sees **Loops** (circles).
    - Layer 3 sees the **Full Fingerprint** (object).

## When to use it

| Feature | Use when... | Avoid when... |
|---|---|---|
| **CNN Layer** | Image classification, object detection, or face recognition | The data is tabular (like a spreadsheet) or sequential (like text) |
| **Max Pooling** | Reducing the dimensionality of features while keeping the most important signals | You are working on "Generative" models where every pixel detail matters |
| **Padding** | Preserving the pixels at the edges of the image | You have very high-resolution images and want to shrink them quickly |

## Common mistakes

1. **Input Shape Mismatch** — CNNs are very picky about input dimensions (Height x Width x Channels). Forgetting to resize your images can crash the model.
2. **Too many filters** — Using hundreds of filters in the first layer. This creates a massive parameter count and usually leads to overfitting.
3. **Ignoring Stride** — Using a large skip (stride) too early, which causes the network to "miss" small objects in the image.

## Files in this folder

| File | Purpose |
|---|---|
| `example.py` | Simple CNN for image classification |
| `notebook.ipynb` | Visualizing Filters and Feature Maps |
| `exercise.py` | 6 TODOs + 1 challenge |
| `solution.py` | Answers with WHY comments |

## Go deeper

- [A Visual Guide to Convolution — Setosa](https://setosa.io/ev/image-kernels/)
- [CS231n: Convolutional Neural Networks for Visual Recognition](https://cs231n.github.io/convolutional-networks/)
