#Made by Tyler Joerendt & Samuel Windell 
#This file takes instances of the GUI, organizes them, and creates a database with them. 

import sqlite3
import GUI_v2
import Attributes


#Creates the table if it doesnt already exists
def create_table():
    #this is what connects us to the customer database
    conn = sqlite3.connect('customer_management.db')
    #This creates a cursor
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS customer_management(
            name TEXT,
            phone_number TEXT,
            repair_history TEXT     
    )""")

    c.execute("""CREATE TABLE IF NOT EXISTS vehicle(
            model_make TEXT,
            year TEXT,
            mileage TEXT,
            vin TEXT     
    )""")

    c.execute("""CREATE TABLE IF NOT EXISTS repairs(
            repair_description TEXT,
            repair_cost TEXT    
    )""")
    #commits our command
    conn.commit()
    #This closes our connection
    conn.close()
create_table()


def all_customers(): 

    conn = sqlite3.connect('customer_management.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM customer_management")
    list = c.fetchall()
    for info in list: 
        print(info)

    c.execute("SELECT rowid, * FROM vehicle")
    list = c.fetchall()
    for info in list: 
        print(info)

    c.execute("SELECT rowid, * FROM repairs")
    list = c.fetchall()
    for info in list: 
        print(info)

    conn.commit()
    conn.close()
all_customers()


#input new customer order
def insert_customer_info(name, phoneNumber, repairMaintenanceHistory): #vehicles will be a list, and repairMaintenanceHistory will be a list of lists.

    conn = sqlite3.connect('customer_management.db')

    c = conn.cursor()

    c.execute("INSERT INTO customer_management VALUES (?,?,?)", (name, phoneNumber, repairMaintenanceHistory))

    conn.commit()
    
    conn.close()

#input new customer order
def insert_vehicle_info(model_make, year, mileage, vin): 

    conn = sqlite3.connect('customer_management.db')

    c = conn.cursor()

    c.execute("INSERT INTO vehicle VALUES (?,?,?,?)", (model_make, year, mileage, vin))

    conn.commit()
    
    conn.close()

def insert_repair_info(repair_description, repair_cost): 
    conn = sqlite3.connect('customer_management.db')

    c = conn.cursor()

    c.execute("INSERT INTO repairs VALUES (?,?)", (repair_description, repair_cost))

    conn.commit()
    
    conn.close()

def show_customer_data(query): #Instead of collecting data from the database to show in the GUI textfield, we will be using re.match in 
#another file.  

    conn = sqlite3.connect('customer_management.db')

    c = conn.cursor()

    c.execute("SELECT * FROM customer_management WHERE phone_number LIKE (?)", (query))

    list = c.fetchall()

    for info in list:
        print(info)

    conn.commit()
    
    conn.close()


    #When INPUT buttons are pressed 