# Hotel-Management
A Python + Tkinter + MySQL based project designed to simplify hotel operations.
This system allows staff to manage customers, bookings, rooms, and billing with ease.

🌟 Key Features

🔹 Customer Management – Add, update, delete customer details
🔹 Room Booking – Allocate rooms, manage availability, checkout system
🔹 Billing System – Automatic total calculation based on stay duration & room type
🔹 Database Integration – MySQL backend ensures reliable storage
🔹 Reports – Track bookings and generate reports with timestamps
🔹 Login System – Separate login for Admin and Customers

⚙️ Tech Stack

🖥️ Frontend (GUI): Tkinter
🛠️ Backend: Python
🗄️ Database: MySQL

Libraries Used:

tkinter → GUI

pillow → Image handling

mysql-connector-python → Database connectivity

🚀 Getting Started
🔧 Installation

Clone the repo:

git clone https://github.com/ishita3120/HotelManagementSystem.git
cd HotelManagementSystem


Install dependencies:

pip install -r requirements.txt

🗄️ Database Setup

Run the following in MySQL:

CREATE DATABASE hotel_management;


(Import your .sql file if provided for tables)

▶️ Run the App
python hotel.py

📂 Project Structure
HotelManagementSystem/
│-- hotel.py          # Main file (launches the system)
│-- customer2.py      # Customer window & logic
│-- db.py             # MySQL connection details
│-- images/           # Images used in GUI
│-- requirements.txt  # Python dependencies
│-- README.md         # Project documentation

🔮 Future Roadmap

✨ Add online booking system (Flask/Django backend)
✨ Export billing reports as PDF/CSV
✨ Add role-based access (Receptionist, Manager, Admin)

⭐ If you found this project useful, don’t forget to star this repo on GitHub!
