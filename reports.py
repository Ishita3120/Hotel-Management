import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ishitaipshita@31"
)
cursor = conn.cursor()

# Create database and table
cursor.execute("CREATE DATABASE IF NOT EXISTS hotel_db")
cursor.execute("USE hotel_db")
cursor.execute('''
    CREATE TABLE IF NOT EXISTS reports (
        report_id INT AUTO_INCREMENT PRIMARY KEY,
        customer_name VARCHAR(100),
        room_number INT,
        check_in_date DATETIME,
        check_out_date DATETIME,
        total_amount DECIMAL(10, 2),
        report_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="hotel_db"
)
cursor = conn.cursor()

# Insert sample data into the reports table
insert_query = """
INSERT INTO reports (
    customer_name,
    room_number,
    check_in_date,
    check_out_date,
    total_amount
) VALUES (%s, %s, %s, %s, %s)
"""

data = (
    "Jane Smith",
    102,
    "2025-04-01 14:00:00",
    "2025-04-04 11:00:00",
    3000.00
)

cursor.execute(insert_query, data)
conn.commit()
conn.close()


conn.commit()
conn.close()

