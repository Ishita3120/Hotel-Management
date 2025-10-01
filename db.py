# db.py
import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Ishitaipshita@31",
        database="management1"
    )
