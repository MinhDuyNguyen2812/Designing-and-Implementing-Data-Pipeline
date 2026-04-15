import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation

class RocketMission2D:
    def __init__(self, root):
        self.root = root
        self.root.title("2D Rocket Launch Simulation")

        # --- 1. Cấu hình UI (Tkinter) ---
        control_frame = tk.Frame(root, padding="10")
        control_frame.pack(side=tk.TOP, fill=tk.X)

        tk.Label(control_frame, text="Mô phỏng 2 Tên lửa bay đến Mặt Trăng (2D)").pack()
        
        btn_start = tk.Button(control_frame, text="Bắt đầu phóng", command=self.start_animation)
        btn_start.pack(pady=5)

        # --- 2. Cấu hình Matplotlib Plot ---
        self.fig, self.ax = plt.subplots(figsize=(8, 6), facecolor='white') # BG màu trắng
        
        # Nhúng Matplotlib vào Tkinter
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        # --- 3. Khởi tạo các đối tượng đồ họa ---
        # Trái đất (gốc tọa độ)
        self.earth = self.ax.scatter([0], [0], color='blue', s=800, label='Trái Đất')
        # Mặt trăng (góc trên bên phải)
        self.moon = self.ax.scatter([100], [100], color='gray', s=400, label='Mặt Trăng')
        
        # Khởi tạo 2 tên lửa (dùng plot rỗng ban đầu)
        self.rocket_a, = self.ax.plot([], [], 'ro-', markersize=8, markevery=[-1], label='Tên lửa A (Bay thẳng)')
        self.rocket_b, = self.ax.plot([], [], 'yo-', markersize=8, markevery=[-1], label='Tên lửa B (Bay lượn sóng)')

        # Thiết lập quỹ đạo (để vẽ đường mờ phía sau)
        self.path_a_x, self.path_a_y = [], []
        self.path_b_x, self.path_b_y = [], []

        # --- 4. Cấu hình hệ tọa độ ---
        self.ax.set_xlim(-10, 110)
        self.ax.set_ylim(-10, 110)
        
        
        ticks = np.arange(0, 101, 20)
        self.ax.set_xticks(ticks)
        self.ax.set_yticks(ticks)
        self.ax.grid(True, linestyle='--', alpha=0.5) # Thêm lưới mờ

        
        self.ax.set_xlabel('Khoảng cách X')
        self.ax.set_ylabel('Khoảng cách Y')
        self.ax.set_title('Quỹ đạo tên lửa đến Mặt Trăng')

       
        self.ax.legend(loc='lower right', frameon=True, facecolor='white', edgecolor='black')

        
        self.ani = None
        self.step = 0

    def animate(self, i):
        """Hàm cập nhật từng frame của hoạt ảnh"""
        self.step = i
        t = i / 100 

        #
        pos_a_x = t * 100
        pos_a_y = t * 100
        
        self.path_a_x.append(pos_a_x)
        self.path_a_y.append(pos_a_y)
        self.rocket_a.set_data(self.path_a_x, self.path_a_y)

        
        pos_b_x = t * 100
        pos_b_y = t * 100 + np.sin(i / 5) * 15 # Biên độ sóng là 15
        
        self.path_b_x.append(pos_b_x)
        self.path_b_y.append(pos_b_y)
        self.rocket_b.set_data(self.path_b_x, self.path_b_y)

        return self.rocket_a, self.rocket_b

    def start_animation(self):
        """Hàm xử lý khi nhấn nút bắt đầu"""
        
        self.step = 0
        self.path_a_x, self.path_a_y = [], []
        self.path_b_x, self.path_b_y = [], []

        self.ani = animation.FuncAnimation(
            self.fig, self.animate, frames=101, interval=50, blit=True, repeat=False
        )
        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = RocketMission2D(root)
    root.mainloop()