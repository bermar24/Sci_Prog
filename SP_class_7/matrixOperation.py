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

# TODO
D = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Determinant (only for square matrices)
det_D = np.linalg.det(D)
print("\nDeterminant of D:", det_D)

# Inverse (if determinant is not zero)
try:
    D_inv = np.linalg.inv(D)
    print("\nInverse of D:\n", D_inv)
except np.linalg.LinAlgError:
    print("\nMatrix D is not invertible (det = 0).")

# Todo Define the coefficient matrix (E) and constants (F)
E = np.array([[2, 1], [1, 3]])
F = np.array([8, 13])

# Solve for X
X = np.linalg.solve(E, F)
print("\nSolution to the linear system (x, y):", X)

# Visualize a matrix using matplotlib
import matplotlib.pyplot as plt

plt.matshow(E, cmap="coolwarm")
plt.title("Matrix Visualization")
plt.colorbar()
plt.show()