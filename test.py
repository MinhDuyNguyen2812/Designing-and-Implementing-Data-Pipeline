# -*- coding: utf-8 -*-
"""
@author: JHy & Copilot
GPS single-iteration ECEF estimate from 4 satellites.
Task:
  1) Use the given satellites (ECEF m) and pseudoranges (m)
  2) Start from x0 = [0, 0, 6370e3] m, clock bias d0 = 0 s
  3) Do EXACTLY ONE linearized least-squares iteration
  4) Apply damping: position 0.1, bias 0.01
  5) Round x, y, z to integers and report them
"""

import numpy as np

# Speed of light (m/s)
c = 299792458.0

# --- Replace these with the new values provided in the question, if any ---
satellites = np.array([
    [15600000,   7540000, 20140000],
    [18760000,   2750000, 18610000],
    [17610000,  14630000, 13480000],
    [19170000,    610000, 18390000]
], dtype=float)

rho = np.array([20432000, 21141000, 22945000, 24145000])

# Initial guess
x = np.array([0.0, 0.0, 6370e3])  # m
d = 0.0  # s

# Build geometry at current state (one iteration)
r = np.linalg.norm(satellites - x, axis=1)
v = rho - (r + c*d)   # residuals

H = np.zeros((4, 4))
for i in range(4):
    H[i, 0] = -(satellites[i, 0] - x[0]) / r[i]
    H[i, 1] = -(satellites[i, 1] - x[1]) / r[i]
    H[i, 2] = -(satellites[i, 2] - x[2]) / r[i]
    H[i, 3] = -c

# Solve H * Δ = v (least squares)
Delta, *_ = np.linalg.lstsq(H, v, rcond=None)

# Apply damping (as specified)
damping_pos = 0.1
damping_bias = 0.01
x = x + damping_pos * Delta[:3]
d = d + damping_bias * Delta[3]

print("Coordinates:", x[0], x[1], x[2])