import tkinter as tk
from room import Roombooking
import tkinter as tk
from tkinter import messagebox
import os
from details import DetailsRoom



class CustomerDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer Dashboard")
        self.root.geometry("800x600")

        title = tk.Label(self.root, text="Customer Dashboard - Room Services", font=("Arial", 20, "bold"), bg="blue", fg="white")
        title.pack(side="top", fill="x")

        btn1 = tk.Button(self.root, text="Room Booking", command=self.open_room_booking, width=20, height=2, font=("Arial", 12, "bold"))
        btn1.place(x=100, y=100)

        btn2 = tk.Button(self.root, text="Room Details", command=self.open_room_details, width=20, height=2, font=("Arial", 12, "bold"))
        btn2.place(x=100, y=200)

    def open_room_booking(self):
        new_win = tk.Toplevel(self.root)
        Roombooking(new_win)

    def open_room_details(self):
        new_win = tk.Toplevel(self.root)
        DetailsRoom(new_win)
        (new_win)


