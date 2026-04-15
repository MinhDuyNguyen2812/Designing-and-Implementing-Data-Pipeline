import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def update(*args):
    ax.clear()
    # Chuyển đổi độ sang radian cho cả 3 trục
    rx, ry, rz = [np.radians(v.get()) for v in angles]
    
    # Ma trận xoay cho X, Y, Z
    Rx = [[1, 0, 0], [0, np.cos(rx), -np.sin(rx)], [0, np.sin(rx), np.cos(rx)]]
    Ry = [[np.cos(ry), 0, np.sin(ry)], [0, 1, 0], [-np.sin(ry), 0, np.cos(ry)]]
    Rz = [[np.cos(rz), -np.sin(rz), 0], [np.sin(rz), np.cos(rz), 0], [0, 0, 1]]
    
    # Xoay các đỉnh
    v_rot = vertices @ np.array(Rx).T @ np.array(Ry).T @ np.array(Rz).T
    
    # Vẽ các cạnh của khối lập phương
    for edge in edges:
        ax.plot(v_rot[edge, 0], v_rot[edge, 1], v_rot[edge, 2], 'b-')
    
    ax.set(xlim=(-2, 2), ylim=(-2, 2), zlim=(-2, 2))
    canvas.draw()

root = tk.Tk()
root.title("Rotate Cube 3D")

# Định nghĩa 8 đỉnh của khối lập phương
vertices = np.array([[i, j, k] for i in [-1, 1] for j in [-1, 1] for k in [-1, 1]])

# Danh sách các cặp đỉnh tạo thành cạnh
edges = [[0,1], [1,3], [3,2], [2,0], [4,5], [5,7], [7,6], [6,4], [0,4], [1,5], [2,6], [3,7]]

angles = [tk.DoubleVar(value=30) for _ in range(3)]
controls = tk.Frame(root, padx=10, pady=10)
controls.pack(side=tk.LEFT, fill=tk.Y)

labels = ["Rotate X", "Rotate Y", "Rotate Z"]
for i in range(3):
    tk.Scale(controls, label=labels[i], from_=0, to=360, orient=tk.HORIZONTAL, 
             variable=angles[i], command=update).pack(pady=5)

fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot(111, projection='3d')
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

update()
root.mainloop()