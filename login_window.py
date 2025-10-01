import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector


# ---------- DATABASE CONNECTION ----------
def create_db_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ishitaipshita@31",
            database="management1"
        )
        return connection
    except mysql.connector.Error as e:
        messagebox.showerror("Database Error", f"Error connecting to MySQL: {e}")
        return None


# ---------- LOGIN WINDOW ----------
class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management Login")
        self.root.geometry("1550x800+0+0")

        frame = tk.Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=340, height=430)

        tk.Label(frame, text="Get Started", font=("times new roman", 12, "bold"), fg="white", bg="black").place(x=95, y=85)

        tk.Label(frame, text="Username", font=("times new roman", 12, "bold"), fg="white", bg="black").place(x=70, y=125)
        self.txtuser = ttk.Entry(frame, font=("times new roman", 12, "bold"))
        self.txtuser.place(x=40, y=150, width=270)

        tk.Label(frame, text="Password", font=("times new roman", 12, "bold"), fg="white", bg="black").place(x=70, y=195)
        self.txtpass = ttk.Entry(frame, font=("times new roman", 12, "bold"), show='*')
        self.txtpass.place(x=40, y=220, width=270)

        tk.Button(frame, text="Login", command=self.login, font=("times new roman", 12, "bold"), bd=3,
                  relief=tk.RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")\
            .place(x=110, y=280, width=120, height=35)

        # Register and Forgot Buttons
        tk.Button(frame, text="New User? Register", command=self.register_window, borderwidth=0,
                  font=("times new roman", 10), fg="white", bg="black", cursor="hand2").place(x=15, y=330)

        tk.Button(frame, text="Forgot Password?", command=self.forgot_password_window, borderwidth=0,
                  font=("times new roman", 10), fg="white", bg="black", cursor="hand2").place(x=15, y=355)

    # ---------- LOGIN ----------
    def login(self):
        username = self.txtuser.get().strip()
        password = self.txtpass.get().strip()

        if not username or not password:
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return

        connection = create_db_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
            user = cursor.fetchone()
            if user:
                role = user[2]
                messagebox.showinfo("Login Successful", f"Welcome {role}", parent=self.root)

                self.root.destroy()
                import hotel1
                new_win = tk.Tk()
                hotel1.HotelManagementSystem(new_win)
                new_win.mainloop()
            else:
                messagebox.showerror("Error", "Invalid credentials", parent=self.root)

            cursor.close()
            connection.close()

    # ---------- REGISTER ----------
    def register_window(self):
        reg_win = tk.Toplevel(self.root)
        reg_win.title("Register New User")
        reg_win.geometry("400x400")

        tk.Label(reg_win, text="Username").pack(pady=5)
        reg_user = tk.Entry(reg_win)
        reg_user.pack()

        tk.Label(reg_win, text="Password").pack(pady=5)
        reg_pass = tk.Entry(reg_win, show="*")
        reg_pass.pack()

        tk.Label(reg_win, text="Confirm Password").pack(pady=5)
        reg_conf_pass = tk.Entry(reg_win, show="*")
        reg_conf_pass.pack()

        tk.Label(reg_win, text="Role (admin/customer)").pack(pady=5)
        reg_role = tk.Entry(reg_win)
        reg_role.pack()

        def register():
            user = reg_user.get().strip()
            pwd = reg_pass.get().strip()
            conf_pwd = reg_conf_pass.get().strip()
            role = reg_role.get().strip()

            if not user or not pwd or not conf_pwd or not role:
                messagebox.showerror("Error", "All fields are required", parent=reg_win)
                return
            if pwd != conf_pwd:
                messagebox.showerror("Error", "Passwords do not match", parent=reg_win)
                return

            conn = create_db_connection()
            if conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM users WHERE username=%s", (user,))
                if cursor.fetchone():
                    messagebox.showerror("Error", "Username already exists", parent=reg_win)
                else:
                    cursor.execute("INSERT INTO users (username, password, role) VALUES (%s, %s, %s)", (user, pwd, role))
                    conn.commit()
                    messagebox.showinfo("Success", "User registered successfully", parent=reg_win)
                cursor.close()
                conn.close()

        tk.Button(reg_win, text="Register", command=register, bg="green", fg="white").pack(pady=20)

    # ---------- FORGOT PASSWORD ----------
    def forgot_password_window(self):
        forgot_win = tk.Toplevel(self.root)
        forgot_win.title("Reset Password")
        forgot_win.geometry("400x250")

        tk.Label(forgot_win, text="Enter Username").pack(pady=5)
        username_entry = tk.Entry(forgot_win)
        username_entry.pack()

        tk.Label(forgot_win, text="New Password").pack(pady=5)
        new_pass_entry = tk.Entry(forgot_win, show="*")
        new_pass_entry.pack()

        def reset_password():
            username = username_entry.get().strip()
            new_password = new_pass_entry.get().strip()

            if not username or not new_password:
                messagebox.showerror("Error", "All fields are required", parent=forgot_win)
                return

            conn = create_db_connection()
            if conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
                if cursor.fetchone():
                    cursor.execute("UPDATE users SET password=%s WHERE username=%s", (new_password, username))
                    conn.commit()
                    messagebox.showinfo("Success", "Password updated successfully", parent=forgot_win)
                else:
                    messagebox.showerror("Error", "Username not found", parent=forgot_win)
                cursor.close()
                conn.close()

        tk.Button(forgot_win, text="Reset Password", command=reset_password, bg="blue", fg="white").pack(pady=20)


# ---------- RUN ----------
def main():
    root = tk.Tk()
    app = LoginWindow(root)
    root.mainloop()


if __name__ == "__main__":
    main()
