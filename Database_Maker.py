#Made by Tyler Joerendt & Samuel Windell 
#This file takes instances of the GUI, organizes them, and creates a database with them. 

import sqlite3
import GUI 
import Attributes 

#Creates the table
def create_table():
    #this is what connects us to the customer database
    conn = sqlite3.connect('customer_management.db')
    
    #This creates a cursor
    c = conn.cursor()

    
    c.execute("""CREATE TABLE customer_management(
            name TEXT,
            vehicle TEXT,
            vehicle_id TEXT,
            phone_number TEXT,
            repair_history TEXT     
    )""")

    #commits our command
    conn.commit()
    #This closes our connection
    conn.close()
#Shows all current customers that are in table
def all_customers(): #I don't think we need this here. 

    conn = sqlite3.connect('customer_management.db')

    c = conn.cursor()

    c.execute("SELECT rowid, * FROM customer_management")
    list = c.fetchall()

#This will print out all of the information that is in the table
    for info in list: 
        print(info)

    conn.commit()
    
    conn.close()
#input new customer order
def insert_customer_info(name, id, phoneNumber, vehicles, repairMaintenanceHistory): #vehicles will be a list, and repairMaintenanceHistory 
#will be a list of lists. 

    conn = sqlite3.connect('customer_management.db')

    c = conn.cursor()

    c.execute("INSERT INTO customer_management VALUES (?,?,?,?,?)", (name, id, phoneNumber, vehicles, repairMaintenanceHistory))

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