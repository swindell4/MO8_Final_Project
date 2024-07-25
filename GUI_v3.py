import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, Scrollbar
import sqlite3
import re
import Database_Maker

'''=======================
Function for adding information
======================='''

def add_customer():

    # Retrieve customer information
    customer_id = customer_id_entry.get()
    name = name_entry.get()
    phone = phone_entry.get()

    # Retrieve vehicle information
    make = make_entry.get()
    model = model_entry.get()
    year = year_entry.get()

    # Input validation as funciton to be able to minimize to make code more readable
    def input_validation()-> bool:
        if not customer_id.isdigit():
            messagebox.showerror("Invalid Input", "Customer ID must be a number")
            return False
        if not name:
            messagebox.showerror("Invalid Input", "Name is required")
            return False
        if not re.match(r"^\d{3}-\d{3}-\d{4}$", phone):
            messagebox.showerror("Invalid Input", "Phone number must be in xxx-xxx-xxxx format")
            return False
        if not make:
            messagebox.showerror("Invalid Input", "Vehicle make is required")
            return False
        if not model:
            messagebox.showerror("Invalid Input", "Vehicle model is required")
            return False
        if not year.isdigit() or len(year) != 4:
            messagebox.showerror("Invalid Input", "Vehicle year must be a 4-digit number")
            return False
        return True

    if not input_validation():
        return

    #connect to database
    conn = sqlite3.connect('customer_management.db')
    c = conn.cursor()

    #add to database, function to minimize to make code more readable
    def insert_customer():

        # Insert vehicle information into the vehicle table and retrieve the auto-generated vehicle ID
        c.execute("INSERT INTO vehicle (make, model, year) VALUES (?, ?, ?)", (make, model, year))
        vehicle_id: int = int(c.lastrowid)

        # Insert customer information into the customer_management table with the vehicle ID
        try:
            c.execute("INSERT INTO customer_management (id, name, phone_number, vehicles) VALUES (?, ?, ?, ?)",
                    (customer_id, name, phone, vehicle_id))
        except sqlite3.IntegrityError:
            messagebox.showerror("Database Error", "Customer ID already exists")
            conn.close()
            return

        # Commit changes and close the connection
        conn.commit()
        conn.close()
    insert_customer()

    # Display the information
    info_display.insert(tk.END, f"Customer ID: {customer_id}\n")
    info_display.insert(tk.END, f"Name: {name}\n")
    info_display.insert(tk.END, f"Phone: {phone}\n")
    info_display.insert(tk.END, f"Vehicle Make: {make}\n")
    info_display.insert(tk.END, f"Vehicle Model: {model}\n")
    info_display.insert(tk.END, f"Vehicle Year: {year}\n")
    info_display.insert(tk.END, "-"*30 + "\n")

def add_service():
    # Retrieve selected repair and vehicle ID
    selected_repair = repairs_listbox.curselection()
    if not selected_repair:
        messagebox.showerror("Invalid Input", "Please select a repair from the list")
        return

    repair_id = repairs_listbox.get(selected_repair).split()[0]
    vehicle_id = vehicle_id_entry.get()

    if not vehicle_id.isdigit():
        messagebox.showerror("Invalid Input", "Vehicle ID must be a number")
        return

    # Connect to the database
    conn = sqlite3.connect('customer_management.db')
    c = conn.cursor()
    repair_cost = 0

    def insert_service() -> None:

        #retrieve repair cost
        c.execute("SELECT cost FROM repairs WHERE id = ?", (int(repair_id),))
        repair_cost = c.fetchone()[0]
        print(repair_cost)
        
        #retieve and add to vihicle history
        c.execute("SELECT maintenance FROM vehicle WHERE id = ?", (int(vehicle_id),))
        repair_history = c.fetchone()[0]
        new_repair_history = (repair_history or "") + f"{repair_id} "
        c.execute("UPDATE vehicle SET maintenance = ? WHERE id = ?", (new_repair_history, int(vehicle_id)))

        #Update money spent by customer in database
        c.execute("SELECT id FROM customer_management WHERE vehicles LIKE ?", (f"%{vehicle_id}%",))
        customer_id = c.fetchone()[0]
        c.execute("UPDATE customer_management SET spent = spent + ? WHERE id = ?", (float(repair_cost), customer_id))

        # Update the info display
        info_display.insert(tk.END, f"Added repair ID {repair_id} to vehicle ID {vehicle_id}\n")
        info_display.insert(tk.END, f"Updated vehicle ID {vehicle_id} with repair cost ${repair_cost} \n")
        info_display.insert(tk.END, "-"*30 + "\n")
        print(repair_cost)

    insert_service()

    print(repair_cost)

    # Commit changes and close the connection
    conn.commit()
    conn.close()

    

    # Clear the input fields
    vehicle_id_entry.delete(0, tk.END)

'''=======================
Functions to populate fields on tabs
======================='''

#========================================Add Service
def populate_repairs_listbox():
    # Connect to the database
    conn = sqlite3.connect('customer_management.db')
    c = conn.cursor()

    # Retrieve all repairs
    c.execute("SELECT id, name, description, cost FROM repairs")
    repairs = c.fetchall()

    # Insert repairs into the listbox
    for repair in repairs:
        repairs_listbox.insert(tk.END, f"{repair[0]} : {repair[1]} - {repair[2]} - {repair[3]}")

    # Close the connection
    conn.close()

#========================================Customer View
def populate_customers_listbox():
    # Connect to the database
    conn = sqlite3.connect('customer_management.db')
    c = conn.cursor()

    # Retrieve all customers
    c.execute("SELECT id, name, phone_number FROM customer_management")
    customers = c.fetchall()

    # Insert customers into the listbox
    for customer in customers:
        customers_listbox.insert(tk.END, f"{customer[0]} : {customer[1]} - {customer[2]}")

    # Close the connection
    conn.close()

def populate_vehicles_listbox(customer_id):
    # Connect to the database
    conn = sqlite3.connect('customer_management.db')
    c = conn.cursor()
    print(customer_id)

    #query1 = f"SELECT vehicles FROM {customer_management} WHERE id = ?"
    #query2 = f"SELECT * FROM {vehicle} WHERE id = ?"

    try:
        #execute the query to get related key
        c.execute(f"SELECT vehicles FROM customer_management WHERE id = ?",(int(customer_id),))
        vehicle_id = c.fetchone()
        print(vehicle_id)

        if vehicle_id:
            vehicle_id = vehicle_id[0] #extract vehicle key

            #use key to search vehicle table
            c.execute(f"SELECT * FROM vehicle WHERE id = ?", (int(vehicle_id),))
            result = c.fetchone()

            #check if a result was found
            if result:
                print("Record found:", result)
                vehicles_listbox.delete(0, tk.END)
                vehicles_listbox.insert('end',result)
            else:
                print("No matching record found")
        else:
            print("No vehicle found in customer data")

    #print sqlite3 error
    except sqlite3.Error as e:
        print("SQL ERROR: ",e)
    
    #make sure connection closed
    finally:
        conn.close()

def populate_repairs_for_vehicle(vehicle_id):
    # Connect to the database
    conn = sqlite3.connect('customer_management.db')
    c = conn.cursor()

    # Retrieve the repair history for the vehicle
    c.execute("SELECT maintenance FROM vehicle WHERE id = ?", (int(vehicle_id),))
    repair_history = c.fetchone()[0]

    # Clear the repairs listbox
    repairs_for_vehicle_listbox.delete(0, tk.END)

    if repair_history:
        repair_ids = repair_history.split()
        try:

            for repair_id in repair_ids:
                c.execute("SELECT id, name, description, cost FROM repairs WHERE id = ?", (repair_id,))
                repair = c.fetchone()
                repairs_for_vehicle_listbox.insert(tk.END, f"{repair[0]} : {repair[1]} - {repair[2]} - {repair[3]}")
        except:
            print("nope")

    # Close the connection
    conn.close()

def refresh_data():

    customers_listbox.delete(0,tk.END)
    populate_customers_listbox()
    repairs_listbox.delete(0, tk.END)
    populate_repairs_listbox()

'''=======================
Tabs in program window
======================='''

#adding new customer information
def create_new_customer_tab(notebook):
    new_customer_frame = ttk.Frame(notebook, width=400, height=280)
    new_customer_frame.pack(fill='both', expand=True)
    notebook.add(new_customer_frame, text='New Customer')

    # Create and place the text fields for customer information
    tk.Label(new_customer_frame, text="Customer ID:").grid(row=0, column=0, padx=10, pady=5)
    global customer_id_entry
    customer_id_entry = tk.Entry(new_customer_frame)
    customer_id_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(new_customer_frame, text="Name:").grid(row=1, column=0, padx=10, pady=5)
    global name_entry
    name_entry = tk.Entry(new_customer_frame)
    name_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(new_customer_frame, text="Phone:").grid(row=2, column=0, padx=10, pady=5)
    global phone_entry
    phone_entry = tk.Entry(new_customer_frame)
    phone_entry.grid(row=2, column=1, padx=10, pady=5)
    tk.Label(new_customer_frame, text="XXX-XXX-XXXX").grid(row=2, column=2, padx=10, pady=5)

    # Create and place the text fields for vehicle information
    tk.Label(new_customer_frame, text="Vehicle Make:").grid(row=3, column=0, padx=10, pady=5)
    global make_entry
    make_entry = tk.Entry(new_customer_frame)
    make_entry.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(new_customer_frame, text="Vehicle Model:").grid(row=4, column=0, padx=10, pady=5)
    global model_entry
    model_entry = tk.Entry(new_customer_frame)
    model_entry.grid(row=4, column=1, padx=10, pady=5)

    tk.Label(new_customer_frame, text="Vehicle Year:").grid(row=5, column=0, padx=10, pady=5)
    global year_entry
    year_entry = tk.Entry(new_customer_frame)
    year_entry.grid(row=5, column=1, padx=10, pady=5)

    # Create and place the 'Add' button
    add_button = tk.Button(new_customer_frame, text="Add", command=add_customer)
    add_button.grid(row=6, columnspan=2, pady=10)

#adding a new service charge
def create_add_service_tab(notebook):
    add_service_frame = ttk.Frame(notebook, width=400, height=280)
    add_service_frame.pack(fill='both', expand=True)
    notebook.add(add_service_frame, text='Add Service')

    # Scrollable listbox for repairs
    global repairs_listbox
    repairs_listbox = tk.Listbox(add_service_frame, width=40, height=15)
    repairs_listbox.grid(row=0, column=0, padx=10, pady=10, rowspan=4)

    scrollbar = Scrollbar(add_service_frame, orient="vertical")
    scrollbar.config(command=repairs_listbox.yview)
    repairs_listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.grid(row=0, column=1, rowspan=4, sticky='ns')

    # Text field for vehicle ID
    tk.Label(add_service_frame, text="Vehicle ID:").grid(row=0, column=2, padx=10, pady=5)
    global vehicle_id_entry
    vehicle_id_entry = tk.Entry(add_service_frame)
    vehicle_id_entry.grid(row=0, column=3, padx=10, pady=5)

    # Button to add service
    add_service_button = tk.Button(add_service_frame, text="Add Service", command=add_service)
    add_service_button.grid(row=1, column=2, columnspan=2, pady=10)

    # Populate the repairs listbox
    populate_repairs_listbox()

#Vie customer information
def create_view_customer_info_tab(notebook):
    view_customer_info_frame = ttk.Frame(notebook, width=400, height=280)
    view_customer_info_frame.pack(fill='both', expand=True)
    notebook.add(view_customer_info_frame, text='View Customer Info')

    # Scrollable listbox for customers
    global customers_listbox
    customers_listbox = tk.Listbox(view_customer_info_frame, width=30, height=20)
    customers_listbox.grid(row=0, column=0, padx=10, pady=10, rowspan=4)

    customers_scrollbar = Scrollbar(view_customer_info_frame, orient="vertical")
    customers_scrollbar.config(command=customers_listbox.yview)
    customers_listbox.config(yscrollcommand=customers_scrollbar.set)
    customers_scrollbar.grid(row=0, column=1, rowspan=4, sticky='ns')

    customers_listbox.bind("<<ListboxSelect>>", on_customer_select)

    # Scrollable listbox for vehicles
    global vehicles_listbox
    vehicles_listbox = tk.Listbox(view_customer_info_frame, width=30, height=20)
    vehicles_listbox.grid(row=0, column=2, padx=10, pady=10, rowspan=4)

    vehicles_scrollbar = Scrollbar(view_customer_info_frame, orient="vertical")
    vehicles_scrollbar.config(command=vehicles_listbox.yview)
    vehicles_listbox.config(yscrollcommand=vehicles_scrollbar.set)
    vehicles_scrollbar.grid(row=0, column=3, rowspan=4, sticky='ns')

    vehicles_listbox.bind("<<ListboxSelect>>", on_vehicle_select)

    # Scrollable listbox for repairs
    global repairs_for_vehicle_listbox
    repairs_for_vehicle_listbox = tk.Listbox(view_customer_info_frame, width=30, height=20)
    repairs_for_vehicle_listbox.grid(row=0, column=4, padx=10, pady=10, rowspan=4)

    repairs_for_vehicle_scrollbar = Scrollbar(view_customer_info_frame, orient="vertical")
    repairs_for_vehicle_scrollbar.config(command=repairs_for_vehicle_listbox.yview)
    repairs_for_vehicle_listbox.config(yscrollcommand=repairs_for_vehicle_scrollbar.set)
    repairs_for_vehicle_scrollbar.grid(row=0, column=5, rowspan=4, sticky='ns')

    # Populate the customers listbox
    populate_customers_listbox()

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

#when a customer is selected on the customer view tab
def on_customer_select(event):
    # Get selected customer
    selected_customer = customers_listbox.curselection()
    if not selected_customer:
        return
    customer_id = customers_listbox.get(selected_customer).split()[0]

    # Populate vehicles for the selected customer
    populate_vehicles_listbox(customer_id)

    # Display total spent by the customer
    display_total_spent(customer_id)

    # Clear the repairs listbox
    repairs_for_vehicle_listbox.delete(0, tk.END)

#when the vehicle is selected
def on_vehicle_select(event):
    selected_vehicle = vehicles_listbox.curselection()

    if selected_vehicle:
        vehicle_data = vehicles_listbox.get(selected_vehicle)

        if isinstance(vehicle_data, tuple):
            vehicle_data = vehicle_data[0]  # Get the first element of the tuple if it is a tuple
        
        if isinstance(vehicle_data, int):
            vehicle_id = vehicle_data  # Directly use vehicle_data if it is an integer
        
        else:
            vehicle_id = vehicle_data.split()[0]  # Otherwise, assume it's a string and split to get vehicle_id
        
        populate_repairs_for_vehicle(vehicle_id)

#display total money spent on customer view
def display_total_spent(customer_id):
    # Connect to the database
    conn = sqlite3.connect('customer_management.db')
    c = conn.cursor()

    # Retrieve the total spent by the customer
    c.execute("SELECT spent FROM customer_management WHERE id = ?", (customer_id,))
    result = c.fetchone()

    if result:
        total_spent = result[0]
        info_display.insert(tk.END, f"Total spent by customer ID {customer_id}: {total_spent}\n")
    else:
        info_display.insert(tk.END, f"No record found for customer ID {customer_id}\n")

    info_display.insert(tk.END, "-"*30 + "\n")

    # Close the connection
    conn.close()


'''=======================
Staring the program
======================='''

def main():
    # Create the main window
    root = tk.Tk()
    root.title("Customer Management System")
    root.geometry("800x600")

    # Create a notebook (tab holder)
    notebook = ttk.Notebook(root)
    notebook.pack(pady=10, expand=True)

    # Create tabs
    create_new_customer_tab(notebook)
    create_add_service_tab(notebook)
    create_view_customer_info_tab(notebook)

    # Create and place the text area to display information
    global info_display
    info_display = tk.Text(root, height=10, width=80)
    info_display.pack(pady=10)

    # Add a refresh button
    refresh_button = tk.Button(root, text="Refresh", command=refresh_data)
    refresh_button.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10)

    # Run the main loop
    root.mainloop()

if __name__ == "__main__":
    Database_Maker.create_table
    main()