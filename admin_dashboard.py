import tkinter as tk
from tkinter import messagebox

class AdminDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin Dashboard")
        self.root.geometry("1550x800+0+0")

        # Header
        header = tk.Label(self.root, text="Admin Dashboard", font=("Arial", 30, "bold"), bg="blue", fg="white")
        header.pack(fill=tk.X)

        # Buttons for Admin Actions
        self.manage_rooms_btn = tk.Button(self.root, text="Manage Rooms", font=("Arial", 14), command=self.manage_rooms)
        self.manage_rooms_btn.place(x=50, y=100, width=200, height=50)

        self.manage_users_btn = tk.Button(self.root, text="Manage Users", font=("Arial", 14), command=self.manage_users)
        self.manage_users_btn.place(x=50, y=180, width=200, height=50)

        self.view_reports_btn = tk.Button(self.root, text="View Reports", font=("Arial", 14), command=self.view_reports)
        self.view_reports_btn.place(x=50, y=260, width=200, height=50)

        self.logout_btn = tk.Button(self.root, text="Logout", font=("Arial", 14), command=self.logout)
        self.logout_btn.place(x=50, y=340, width=200, height=50)

    def manage_rooms(self):
        # Open room management window (could be a new Toplevel window)
        messagebox.showinfo("Manage Rooms", "Room Management is under construction")

    def manage_users(self):
        # Open user management window (could be a new Toplevel window)
        messagebox.showinfo("Manage Users", "User Management is under construction")

    def view_reports(self):
        # Open reports window (could be a new Toplevel window)
        messagebox.showinfo("View Reports", "Reports View is under construction")

    def logout(self):
        # Logout action, going back to the login page
        self.root.destroy()
        new_window = tk.Tk()
        from image.login_window import LoginWindow
        LoginWindow(new_window)
        new_window.mainloop()
