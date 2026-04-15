import tkinter as tk
from tkinter import messagebox, ttk
from app.database import login_user, register_user, get_tasks, add_task, update_task, delete_task

class TaskApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Corporate Task Manager v1.0")
        self.root.geometry("600x500")

        self.current_user_id = None

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill="both", expand=True)

        self.show_login_screen()

    def clear_screen(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def show_login_screen(self):
        self.clear_screen()
        frame = tk.Frame(self.main_frame)
        frame.pack(pady=50)

        tk.Label(frame, text="EMPLOYMENT LOGIN", font=("Times New Roman", 20, "bold")).pack(pady=20)

        tk.Label(frame, text="Username:").pack()
        self.ent_user = tk.Entry(frame)
        self.ent_user.pack(pady=5)

        tk.Label(frame, text="Password:").pack()
        self.ent_pass = tk.Entry(frame, show="*")
        self.ent_pass.pack(pady=5)

        tk.Button(frame, text="Login", width=15, bg="#4CAF50", fg="white",
                  command=self.handle_login).pack(side="right", pady=20)
        
        tk.Button(frame, text="Register", width=15, bg="#2196F3", fg="white", 
                  command=self.handle_register).pack(side="left", padx=1)
        
    def handle_login(self):
        u = self.ent_user.get()
        p = self.ent_pass.get()
        user_id = login_user(u, p)

        if not u or not p:
            messagebox.showwarning("Input Error", "Username and password cannot be empty!")
            return
        
        if user_id:
            self.current_user_id = user_id
            self.show_dashboard()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password!")

    def handle_register(self):
        u = self.ent_user.get()
        p = self.ent_pass.get()

        if not u or not p:
            messagebox.showwarning("Input Error", "Username and password cannot be empty!")
            return 
        
        success = register_user(u, p)
        if success:
            messagebox.showinfo("Congratulations", f"Account '{u}' has been created!")
        else:
            messagebox.showerror("Error", "Username has been used!")

    def show_dashboard(self):
        self.clear_screen()
        
        top_bar = tk.Frame(self.main_frame, bg="#eee", pady=10)
        top_bar.pack(fill="x")
        tk.Button(top_bar, text="Logout", command=self.show_login_screen).pack(side="right", padx=10)

        input_frame = tk.Frame(self.main_frame)
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="New Task:").grid(row=0, column=0)
        self.ent_task = tk.Entry(input_frame, width=15)
        self.ent_task.grid(row=0, column=1, padx=5)
        tk.Label(input_frame, text="Description:").grid(row=0, column=2)
        self.ent_desc = tk.Entry(input_frame, width=15)
        self.ent_desc.grid(row=0, column=3, padx=5)
        tk.Button(input_frame, text="Add", command=self.handle_add).grid(row=0, column=4)

        columns = ("id", "title", "desc", "status")
        self.tree = ttk.Treeview(self.main_frame, columns=columns, show="headings")

        self.tree.heading("id", text="ID")
        self.tree.heading("title", text="Task")
        self.tree.heading("desc", text="Description")
        self.tree.heading("status", text="Status")

        self.tree.column("id", width=50, anchor="center")
        self.tree.column("status", width=100, anchor="center")

        self.tree.pack(fill="both", expand=True, padx=20, pady=10)

        tk.Button(self.main_frame, text="Delete Selected", bg="#f44336", fg="white",
                  command=self.handle_delete).pack(pady=5)
        
        self.refresh_list()

    def refresh_list(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        tasks = get_tasks(self.current_user_id)
        for t in tasks:
            self.tree.insert("", "end", values=(t[0], t[1], t[2], t[3]))

    def handle_add(self):
        title = self.ent_task.get()
        desc = self.ent_desc.get()
        if title:
            add_task(self.current_user_id, title, desc)
            self.ent_task.delete(0, tk.END)
            self.ent_desc.delete(0, tk.END)
            self.refresh_list()
        else:
            messagebox.showwarning("Input Error", "Task title cannot be empty")

    def handle_delete(self):
        selected = self.tree.selection()
        if not selected:
            return
        
        task_id = self.tree.item(selected[0])['values'][0]
        if messagebox.askyesno("Confirm", "Are you sure you want to delete this task?"):
            delete_task(task_id)
            self.refresh_list()

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskApp(root)
    root.mainloop()