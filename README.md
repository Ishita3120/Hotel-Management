# Hotel-Management
A full-fledged Hotel Management System built using Python (Tkinter GUI) and MySQL for database management.
This project provides hotel staff with a simple yet powerful interface to handle customer bookings, room management, and billing.

📌 Features

✅ Customer Management – Add, update, delete customer details
✅ Room Booking – Allocate rooms, manage availability, checkout system
✅ Billing System – Auto-calculate total bills based on room type & duration
✅ Database Integration – MySQL used for persistent data storage
✅ Reports – View all bookings and generate reports with timestamps
✅ Login System – Admin & customer login with authentication

⚙️ Tech Stack

Frontend (GUI): Tkinter (Python)

Backend: Python

Database: MySQL

Libraries Used:

tkinter – GUI

pillow – Image handling

mysql-connector-python – MySQL connectivity

🚀 How to Run

Clone the Repository

git clone https://github.com/ishita3120/HotelManagementSystem.git
cd HotelManagementSystem


Install Dependencies
Make sure Python is installed (>=3.8). Then run:

pip install -r requirements.txt


Setup MySQL Database

Open MySQL Workbench or CLI.

Create a new database:

CREATE DATABASE hotel_management;


Import the tables (you can provide your .sql file here if you export it).

Run the Application

python hotel.py

📂 Project Structure
HotelManagementSystem/
│-- hotel.py              # Main file (launches the system)
│-- customer2.py          # Customer window & logic
│-- db.py                 # MySQL connection details
│-- images/               # Images used in GUI
│-- requirements.txt      # Python dependencies
│-- README.md             # Project documentation

📸 Screenshots

Add screenshots here if possible (GUI windows, booking screen, etc.)
Example:

🔮 Future Enhancements

✅ Online booking system with Flask/Django

✅ PDF report export for billing

✅ Role-based access (Receptionist, Manager, Admin)

👩‍💻 Author

Ishita Sahay
💼 LinkedIn

📧 Email
