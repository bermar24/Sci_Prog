import numpy as np

# Creating matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
C = np.array([[9, 10], [11, 12], [13, 14]])

# Matrix addition
print("Addition:\n", A + B)

# Matrix multiplication
print("Matrix Multiplication:\n", np.dot(A, B))

# Transpose
print("matrix:\n", C)
print("Transpose:\n", C.T)

# TODO: Broadcasting allows NumPy to perform operations on arrays of different shapes by "stretching" them to match compatible dimensions.
# Broadcasting in action
b = np.array([10, 20])
print("Result:\n", A + b)

