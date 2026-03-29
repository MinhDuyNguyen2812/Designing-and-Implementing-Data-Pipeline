import numpy as np
import pandas as pd

# ---------------------------------------------------------
# SOURCES & REFERENCES (Academic/Industry Standards):
# 1. Goodfellow, I. (2016). "Deep Learning" - Ch. 5: Machine Learning Basics (Noise & Generalization).
# 2. Géron, A. (2019). "Hands-On Machine Learning" - Ch. 4: Gradient Descent & Normalization.
# 3. Stanford CS229: Logistic Regression & Probabilistic Decision Boundaries (Sigmoid).
# ---------------------------------------------------------

# 1. DATASET INITIALIZATION WITH GAUSSIAN NOISE
# Why: Normal(0, 2) simulates real-world "Uncertainty" (luck, health, exam difficulty).
np.random.seed(42)
n_students = 100 

X_raw = np.random.uniform(1, 12, size=(n_students, 1))

# Noise Mechanism: Mean=0, StdDev=2. Creates "overlapping classes" (Pass/Fail overlap).
noise = np.random.normal(0, 2, size=(n_students, 1))
y = ((X_raw + noise) > 7).astype(int) 

# 2. STANDARDIZATION (Z-Score Normalization)
# Why: Neural networks converge faster when features have Mean=0 and StdDev=1.
X_mean, X_std = np.mean(X_raw), np.std(X_raw)
X = (X_raw - X_mean) / X_std

# 3. HYPERPARAMETERS & NEURONS
# 10 Hidden Neurons: Provides enough "capacity" to filter noise and find the trend.
W1 = np.random.randn(1, 10) * 0.1
b1 = np.zeros((1, 10))
W2 = np.random.randn(10, 1) * 0.1
b2 = np.zeros((1, 1))

def relu(z): return np.maximum(0, z)
def sigmoid(z): return 1 / (1 + np.exp(-z))

# 4. TRAINING LOOP (10,000 Epochs)
# Why: Noisy data requires more iterations for the "Weights" to settle on a trend.
learning_rate = 0.05
for epoch in range(10000): 
    # Forward Propagation
    a1 = relu(np.dot(X, W1) + b1)
    a2 = sigmoid(np.dot(a1, W2) + b2)

    # Backward Propagation (Gradient Descent)
    dz2 = a2 - y
    dW2 = (1/n_students) * np.dot(a1.T, dz2)
    db2 = (1/n_students) * np.sum(dz2, axis=0)
    dz1 = np.dot(dz2, W2.T) * (a1 > 0)
    dW1 = (1/n_students) * np.dot(X.T, dz1)
    db1 = (1/n_students) * np.sum(dz1, axis=0)

    # Update Parameters
    W1 -= learning_rate * dW1
    b1 -= learning_rate * db1
    W2 -= learning_rate * dW2
    b2 -= learning_rate * db2

# 5. PREDICTION (Probabilistic Output)
def get_prob(hours):
    x_scaled = (hours - X_mean) / X_std
    a1 = relu(np.dot(x_scaled, W1) + b1)
    return sigmoid(np.dot(a1, W2) + b2)[0][0]

# --- RESULTS ---
print(f"--- RESULT ---")
print(f"Study 4h: {get_prob(4)*100:.1f}% Pass")
print(f"Study 7h: {get_prob(7)*100:.1f}% Pass")
print(f"Study 10h: {get_prob(10)*100:.1f}% Pass")