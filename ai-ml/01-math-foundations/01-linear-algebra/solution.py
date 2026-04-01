# solution.py - Linear Algebra answers

import numpy as np

# TODO 1
v = np.array([10, 20, 30])

# TODO 2
M = np.zeros((2, 3))

# TODO 3
magnitude = np.linalg.norm(v)
print(f"Magnitude of v: {magnitude:.2f}")

# TODO 4
scaled_v = v * 0.5

# TODO 5
A = np.array([[1, 2], [3, 4]])
B = np.array([[1], [2]])
result = A @ B 
# result = [[1*1 + 2*2], [3*1 + 4*2]] = [[5], [11]]
print(f"Matrix Mult result shape: {result.shape}")

# TODO 6
# Answer: The Dot Product (specifically Cosine Similarity). 
# It tells you how much two arrows are pointing in the same direction.

# CHALLENGE ANSWER
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

v1 = np.array([1, 0])
v2 = np.array([1, 1])
print(f"Cosine Similarity: {cosine_similarity(v1, v2):.4f}")

print("\n--- Why it works ---")
print("1. Density: Matrices allow us to pack millions of numbers into a single object, making data manageable for computers.")
print("2. Parallelism: Modern GPUs are specifically designed to do one thing: matrix multiplication. This is why AI is so fast on GPUs.")
print("3. Foundations: Every single 'Weight' in a neural network is just an entry in a matrix.")
print("4. Transformations: When you rotate a 3D model in a video game or apply a filter on Instagram, you are doing Linear Algebra.")

export {};
