import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def update(*args):
    ax.clear()
    # 1. Convert degrees to radians
    rx, ry, rz = np.radians([angle_x.get(), angle_y.get(), angle_z.get()])
    
    # 2. Rotation Matrices
    Rx = [[1, 0, 0], [0, np.cos(rx), -np.sin(rx)], [0, np.sin(rx), np.cos(rx)]]
    Ry = [[np.cos(ry), 0, np.sin(ry)], [0, 1, 0], [-np.sin(ry), 0, np.cos(ry)]]
    Rz = [[np.cos(rz), -np.sin(rz), 0], [np.sin(rz), np.cos(rz), 0], [0, 0, 1]]
    
    # 3. Apply rotation to the vector coordinates
    # Matrix order: Square * Rx * Ry * Rz
    rotated = square @ np.array(Rx).T @ np.array(Ry).T @ np.array(Rz).T
    
    ax.plot(rotated[:, 0], rotated[:, 1], rotated[:, 2], 'r-')
    ax.set(xlim=(-2, 2), ylim=(-2, 2), zlim=(-2, 2))
    canvas.draw()

root = tk.Tk()
root.title("Vector Rotation")

# Define the square geometry
square = np.array([[-1,-1,0], [1,-1,0], [1,1,0], [-1,1,0], [-1,-1,0]])


controls = tk.Frame(root, padx=10)
controls.pack(side=tk.LEFT)

angle_x, angle_y, angle_z = tk.DoubleVar(), tk.DoubleVar(), tk.DoubleVar()

for label, var in [("X Angle", angle_x), ("Y Angle", angle_y), ("Z Angle", angle_z)]:
    tk.Scale(controls, label=label, from_=0, to=360, orient="horizontal", 
             variable=var, command=update).pack()

fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

update()
root.mainloop()