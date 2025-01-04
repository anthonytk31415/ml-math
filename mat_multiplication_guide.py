import numpy as np
import pandas as pd
from math import sqrt



# Set random seed for reproducibility
np.random.seed(42)

# Define x and y as 3x1 vectors with random values
# x = np.random.rand(3, 1)
x = np.random.randint(0, 10, size=(3, 1))
y = np.random.rand(3, 1)

# Define A as a 3x3 matrix with random values
A = np.random.rand(3, 3)

# Calculate inner product (x transpose * y)
# Result is a scalar (1x1)
inner_product = x.T @ y  # alternatively: np.dot(x.T, y)

ip = np.dot(x.T, y)

# Calculate outer product (x * x transpose)
# Result is a 3x3 matrix
outer_product = x @ x.T  # alternatively: np.outer(x.flatten(), x.flatten())
op = np.outer(x, x.T)

# Calculate matrix-vector product (A * x)
# Result is a 3x1 vector
matrix_vector_product = A @ x  # alternatively: np.dot(A, x)


print("ip: ", ip)
print("op: ", op)