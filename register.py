import tkinter as tk
from tkinter import ttk, messagebox
from db import connect_db

class RegisterWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("400x400")

        # Labels and Entry widgets
        tk.Label(root, text="Username").pack(pady=5)
        self.username_entry = ttk.Entry(root)
        self.username_entry.pack(pady=5)

        tk.Label(root, text="Email").pack(pady=5)
        self.email_entry = ttk.Entry(root)
        self.email_entry.pack(pady=5)

        tk.Label(root, text="Password").pack(pady=5)
        self.password_entry = ttk.Entry(root, show="*")
        self.password_entry.pack(pady=5)

        tk.Label(root, text="Confirm Password").pack(pady=5)
        self.confirm_password_entry = ttk.Entry(root, show="*")
        self.confirm_password_entry.pack(pady=5)

        ttk.Button(root, text="Register", command=self.register_user).pack(pady=20)

    def register_user(self):
        username = self.username_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if not username or not email or not password or not confirm_password:
            messagebox.showerror("Error", "All fields are required")
            return

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match")
            return

        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
            if cursor.fetchone():
                messagebox.showerror("Error", "Username already exists")
                return

            cursor.execute(
                "INSERT INTO users (username, password, email, user_type) VALUES (%s, %s, %s, %s)",
                (username, password, email, 'customer')
            )
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Registration Successful")
            self.root.destroy()

        except Exception as e:
            messagebox.showerror("Error", f"Database error: {str(e)}")

# To run standalone
if __name__ == "__main__":
    root = tk.Tk()
    app = RegisterWindow(root)
    root.mainloop()
