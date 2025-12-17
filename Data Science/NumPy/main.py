# %% Load in Numpy
import numpy as np

# %% The Basics
# Array Creation
a = np.array([1, 2, 3], dtype='int32')
print(a)

b = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]], dtype='float32')
print(b)  

# Get Dimensions
print(a.ndim)  # 1
print(b.ndim)  # 2

# Get Shape
print(a.shape)  # (3) beacuese it's column vector with 3 elements
print(b.shape)  # (2, 3) because it's 2 rows and 3 columns

# Get Type
print(a.dtype)  # int64
print(b.dtype)   # float64

# Get Size
print(a.itemsize)  # int64 = 8 bytes per element, int32 = 4 bytes per element
print(b.itemsize)  # float64 = 8 bytes per element, float32 = 4 bytes per element

# Get Total Size
print(a.nbytes)  # 3 elements * 4 bytes = 12 bytes
print(b.nbytes)  # 6 elements * 4 bytes = 24 bytes

# %% Accessing/Changing specific elements, rows, columns, etc.
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)

# Get a specific element [r, c]
print(a[1, 2])  # 7
print(a[1, -3])  # 6

# Get a specific row
print(a[0, :])  # [1 2 3 4]

# Get a specific column
print(a[:, 2])  # [ 3  7 11]

# Getting a little fancy [startindex:endindex:stepsize]
print(a[0, 0:4:2])  # [1 3]