#Made by Tyler Joerendt & Samuel Windell 
#This file takes instances of the GUI, organizes them, and creates a database with them. 

import sqlite3
import GUI_v3
import Attributes
from Attributes import RepairMaintenanceOptions

def create_table():
    # Connect to the customer management database
    conn = sqlite3.connect('customer_management.db')
    
    # Create a cursor
    c = conn.cursor()

    # Create customer table with the required fields
    c.execute("""CREATE TABLE IF NOT EXISTS customer_management(
            id INTEGER PRIMARY KEY NOT NULL,
            name TEXT NOT NULL,
            phone_number TEXT NOT NULL,
            vehicles INTEGER NOT NULL,
            spent REAL DEFAULT 0.0
    )""")

    # Create vehicle table with the required fields
    c.execute("""CREATE TABLE IF NOT EXISTS vehicle(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            make TEXT NOT NULL,
            model TEXT NOT NULL,
            year INTEGER NOT NULL,
            maintenance TEXT
    )""")

    # Create repairs table with the required fields
    c.execute("""CREATE TABLE IF NOT EXISTS repairs(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT NOT NULL,
            cost REAL NOT NULL
    )""")
    
    #add repair options to database
    insert_repair_options(conn,c)

    # Commit the command
    conn.commit()

    # Close the connection
    conn.close()

#insert list of repair options from class to database
def insert_repair_options(co, cur) -> None:
    repair_options = RepairMaintenanceOptions().returnOptions()
    for name, details in repair_options.items():
        cur.execute("INSERT INTO repairs (name, description, cost) VALUES (?, ?, ?)",
                    (name, details["Description"], details["Cost"]))

create_table()