import sqlite3

#Creates the table
def create_table():
    #this is what connects us to the customer database
    conn = sqlite3.connect('customer_management.db')
    
    #This creates a cursor
    c = conn.cursor()

    
    c.execute("""CREATE TABLE customer_management(
            first_name TEXT,
            last_name TEXT,
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
def all_customers():

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
def insert_info(first_name, last_name, vehicle, vehicle_id, phone_number, repair_history):

    conn = sqlite3.connect('customer_management.db')

    c = conn.cursor()

    c.execute("INSERT INTO customer_management VALUES (?,?,?,?,?,?)", (first_name, last_name, vehicle, vehicle_id, phone_number, repair_history))

    conn.commit()
    
    conn.close()

def show_customer_data(query):

    conn = sqlite3.connect('customer_management.db')

    c = conn.cursor()

    c.execute("SELECT * FROM customer_management WHERE phone_number LIKE (?)",(query,))

    list = c.fetchall()

    for info in list:
        print(info)

    conn.commit()
    
    conn.close()