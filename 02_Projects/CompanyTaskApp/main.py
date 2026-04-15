import tkinter as tk
from app.database import create_tables
from app.gui import TaskApp

def main():
    create_tables()

    root = tk.Tk()
    app = TaskApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()