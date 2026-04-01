# example.py - Vectors & Matrices in NumPy

import numpy as np

# 1. Vectors (1D Arrays)
# A vector represents a single data point
v = np.array([1, 2, 3])
print(f"Vector v: {v}")

# 2. Matrices (2D Arrays)
# A matrix represents a collection of data points
M = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(f"Matrix M:\n{M}")
print(f"Shape of M: {M.shape}") # (Rows, Columns)

# 3. Transpose (Flip rows and columns)
print(f"Transpose of M:\n{M.T}")

# 4. Dot Product (Weighted Sum)
# a . b = (a1*b1 + a2*b2 + ...)
a = np.array([1, 2])
b = np.array([3, 4])
dot_prod = np.dot(a, b) # 1*3 + 2*4 = 11
print(f"Dot product of a and b: {dot_prod}")

# 5. Matrix Multiplication (@)
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
# [1*5+2*7, 1*6+2*8] -> [19, 22]
# [3*5+4*7, 3*6+4*8] -> [43, 50]
result = A @ B 
print(f"Matrix Multiplication (A @ B):\n{result}")

# 6. Element-wise Multiplication (*)
# [1*5, 2*6] -> [5, 12]
# [3*7, 4*8] -> [21, 32]
element_wise = A * B
print(f"Element-wise multiplication (A * B):\n{element_wise}")
