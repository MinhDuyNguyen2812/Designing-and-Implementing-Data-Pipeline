import tkinter as tk
from database import create_tables
from gui import TaskApp

def main():
    create_tables()
    root = tk.Tk()
    app = TaskApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()