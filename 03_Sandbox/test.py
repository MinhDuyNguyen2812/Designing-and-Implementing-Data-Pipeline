import numpy as np

# 1. Dataset Initialization
# Input: Hours studied (X), Output: Pass/Fail (y)
X = np.array([[2], [3], [5], [7], [8], [11], [4], [4], [2]], dtype=float)
y = np.array([[0], [0], [0], [1], [1], [1], [1], [0], [1]], dtype=float)

# 2. Standardization
# Scales features to have a mean of 0 and standard deviation of 1
# Reference: Géron, A. 2019. Hands-On Machine Learning, 2nd edn. p. 72.
X_mean = np.mean(X, axis=0)
X_std = np.std(X, axis=0)
X = (X - X_mean) / X_std

# 3. Parameter Initialization
# Initializing weights and biases for Hidden Layer (3 neurons) and Output Layer (1 neuron)
# Reference: He, K. et al. 2015. Delving Deep into Rectifiers. (He Initialization principle)
np.random.seed(42)
W1 = np.random.randn(1, 5) * 0.01  # Weights for Hidden Layer
b1 = np.zeros((1, 5))             # Bias for Hidden Layer
W2 = np.random.randn(5, 1) * 0.01  # Weights for Output Layer
b2 = np.zeros((1, 1))             # Bias for Output Layer

# 4. Activation Functions
# ReLU for hidden layers, Sigmoid for binary output
# Reference: Ramachandran, P. et al. 2017. Searching for Activation Functions.
def relu(z):
    return np.maximum(0, z)

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# 5. Training Loop (Gradient Descent)
# Reference: Ruder, S. 2016. An overview of gradient descent optimization algorithms.
learning_rate = 0.01
epochs = 5000

for epoch in range(epochs):
    # Forward Propagation
    z1 = np.dot(X, W1) + b1
    a1 = relu(z1)
    z2 = np.dot(a1, W2) + b2
    a2 = sigmoid(z2)
    
    # Cost Function (Binary Cross-Entropy)
    m = y.shape[0]
    loss = -np.mean(y * np.log(a2) + (1 - y) * np.log(1 - a2))
    
    # Backward Propagation (Chain Rule)
    dz2 = a2 - y
    dW2 = (1 / m) * np.dot(a1.T, dz2)
    db2 = (1 / m) * np.sum(dz2, axis=0, keepdims=True)
    
    da1 = np.dot(dz2, W2.T)
    dz1 = da1 * (z1 > 0) # ReLU derivative
    dW1 = (1 / m) * np.dot(X.T, dz1)
    db1 = (1 / m) * np.sum(dz1, axis=0, keepdims=True)
    
    # Parameter Update
    W2 -= learning_rate * dW2
    b2 -= learning_rate * db2
    W1 -= learning_rate * dW1
    b1 -= learning_rate * db1

# 6. Prediction
# Output values > 0.5 are classified as 1 (Pass)
predictions = (a2 > 0.5).astype(int)
print(f"Final Predictions:\n{predictions}")
a2_short = np.round(a2, 3)
print(f"Probabilities:\n{a2_short}")