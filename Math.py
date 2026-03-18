import numpy as np

u = np.array([[5],
              [5],
              [-4]])

v = np.array([[-1],
              [5],
              [2]])

w = np.array([[3],
              [-1],
              [-2]])

result = -2 * u + 4 * v - 3 * w
print(result)
