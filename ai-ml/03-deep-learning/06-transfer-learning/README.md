# Transfer Learning

## What is it?

**Transfer Learning** is a technique where you take a model that has already been trained on a massive dataset (like **ImageNet**, which has millions of labeled images) and "re-purpose" it for your own research. Instead of training a model from scratch, you "transfer" the knowledge it has gained about low-level features (lines, shapes, textures) to save time and compute power.

## Real-world analogy

Think of transfer learning like **hiring a professional chef to cook at your specific restaurant**:
- **Standard Training**: Hiring someone who has never cooked and teaching them what "Salt" is (Training from scratch).
- **Transfer Learning**: Hiring a Gordon Ramsay-level chef who already knows how to bake, fry, and grill. 
- **Fine-tuning**: You only need to teach the chef your specific "Secret Recipe" (The new classification layer). 
- **Benefit**: The chef already knows how to handle a knife and use an oven; you save months of training.

## When to use it

| Feature | Use when... | Avoid when... |
|---|---|---|
| **Transfer Learning**| You have a small dataset (e.g., only 100 photos of local birds) | You have millions of images that are completely different from the pre-trained data (e.g., satellite imagery vs. standard photos) |
| **Freezing** | You want to prevent the pre-trained weights from changing at all | You have a large enough dataset to "fine-tune" the early layers for better accuracy |
| **Fine-tuning** | You want to improve the model by slightly adjusting the pre-trained weights | You are in a rush or have very limited compute power |

## Common mistakes

1. **Incorrect Normalization** — Pre-trained models expect their inputs to be normalized in a specific way (usually based on ImageNet stats). Forgetting this leads to poor performance.
2. **Replacing too much** — Deleting too many layers from the pre-trained model, losing the "knowledge" you were trying to transfer.
3. **High Learning Rate** — Using a high learning rate during fine-tuning, which "forgets" the pre-trained features too quickly (known as "Catastrophic Forgetting").

## Files in this folder

| File | Purpose |
|---|---|
| `example.py` | Using ResNet-18 with PyTorch for a custom task |
| `notebook.ipynb` | Visualizing Feature extraction vs Fine-tuning |
| `exercise.py` | 6 TODOs + 1 challenge |
| `solution.py` | Answers with WHY comments |

## Go deeper

- [Transfer Learning for Computer Vision — PyTorch Tutorial](https://pytorch.org/tutorials/beginner/transfer_learning_tutorial.html)
- [How to Fine-tune a Pre-trained Model](https://pytorch.org/tutorials/beginner/finetuning_torchvision_models_tutorial.html)
