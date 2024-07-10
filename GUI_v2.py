from tkinter import * #importing everything from tkinter
import Database_Maker
import sqlite3

vehicleList = [] #Making a list to display back to the user at the end, can be changed later to write it to a file
customerList = [] #Making a list to display back to the user at the end, can be changed later to write it to a file
repairList = [] #Making a list to display back to the user at the end, can be changed later to write it to a file


#IN THE SEARCH GUI AT THE BOTTOM REPLACE THE COMMENT WITH THE DATA YOU HAVE FOUND

'''class RedirectGUI:
    def __init__(type):
        type.window = Tk()
        type.window.title("Redirect") #This is the title of the window
        type.window.geometry('1150x300') #This is the size the window is set to
        type.window.minsize(1150, 300) #This is the minimum size the window can be adjusted to, can become larger

        #type is just saying that it is referencing the whole class, label is for typing text to show to the user, Button is for buttons, the name after type. does not matter entirely it is just there to make it easier to know what is what.
        #The type.any name.grid is telling it where to put what it is referencing for example it will put the label in column one row one
        #Most of these comments apply to the later GUI classes

        type.whatType = Label (type.window , text = "What Information Would You Like To Input?", height = 1, width = 40, bd =5, font=('Times New Roman', 18) ) #Text saying what to do
        type.whatType.grid(padx=30, pady=15, column = 1, row = 1, sticky = 'EW')

        type.customer = Button(type.window, fg = 'red', state = 'normal', text = "Customer", bd =5, font=('Times New Roman', 18), command = lambda: [ type.window.destroy(), CustomerGUI()])
        type.customer.grid(padx=30, pady=15, column = 2, row = 1, sticky = 'EW')

        type.vehicle = Button(type.window, fg = 'blue' , state = 'normal', text = "Vehicle", bd =5, font=('Times New Roman', 18), command = lambda: [ type.window.destroy(), VehicleGUI()])
        type.vehicle.grid(padx=30, pady=15, column = 3, row = 1, sticky = 'EW')

        type.repairs = Button(type.window, fg = 'green' , state = 'normal', text = "Repairs", bd =5, font=('Times New Roman', 18), command = lambda: [ type.window.destroy(), RepairsGUI()])
        type.repairs.grid(padx=30, pady=15, column = 4, row = 1, sticky = 'EW')

        type.window.mainloop() #This is what makes the window run VERY IMPORTANT DO NOT REMOVE, if you need to make a new GUI follow this main guideline and it should work '''

class CustomerGUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Customer")
        self.window.geometry('1150x600')
        self.window.minsize(1150, 600)

        self.name_label = Label(self.window, fg='red', text="Name Of Customer?", height=1, width=70, bd=5, font=('Times New Roman', 18))
        self.name_label.grid(padx=30, pady=15, column=1, row=1, sticky='EW')

        self.customer_entry = Text(self.window, height=1, width=75, bd=5, font=('Times New Roman', 18))
        self.customer_entry.grid(padx=30, pady=15, column=1, row=2, sticky='EW')

        self.phone_label = Label(self.window, fg='red', text="Phone Number?", height=1, width=70, bd=5, font=('Times New Roman', 18))
        self.phone_label.grid(padx=30, pady=15, column=1, row=3, sticky='EW')

        self.number_entry = Text(self.window, height=1, width=75, bd=5, font=('Times New Roman', 18))
        self.number_entry.grid(padx=30, pady=15, column=1, row=4, sticky='EW')

        self.repairs_label = Label(self.window, fg='red', text="How Many Repairs Customer Has Had?", height=1, width=70, bd=5, font=('Times New Roman', 18))
        self.repairs_label.grid(padx=30, pady=15, column=1, row=5, sticky='EW')

        self.repair_entry = Text(self.window, height=1, width=75, bd=5, font=('Times New Roman', 18))
        self.repair_entry.grid(padx=30, pady=15, column=1, row=6, sticky='EW')

        self.done_button = Button(self.window, fg='red', state='disabled', text="DONE", bd=5, font=('Times New Roman', 18), command=self.on_done)
        self.done_button.grid(padx=30, pady=15, column=2, row=4, sticky='EW')

        self.nullcheck_button = Button(self.window, fg='red', state='normal', text="CHECK", bd=5, font=('Times New Roman', 18), command=self.nullCheck)
        self.nullcheck_button.grid(padx=30, pady=15, column=2, row=3, sticky='EW')

        self.window.mainloop()

    def on_done(self):
        customer_name = self.customer_entry.get(1.0, "end-1c")
        phone_number = self.number_entry.get(1.0, "end-1c")
        repairs_amount = self.repair_entry.get(1.0, "end-1c")

        Database_Maker.insert_customer_info(customer_name, phone_number, repairs_amount)
    
        customerList.append(customer_name)
        customerList.append(phone_number)
        customerList.append(repairs_amount)

        self.window.destroy()
        VehicleGUI()

    def nullCheck(self):
        customer_name = self.customer_entry.get(1.0, "end-1c")
        phone_number = self.number_entry.get(1.0, "end-1c")
        repairs_amount = self.repair_entry.get(1.0, "end-1c")

        if customer_name and phone_number and repairs_amount:
            self.done_button.config(state='normal')
        else:
            self.done_button.config(state='disabled')

class VehicleGUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Vehicle")
        self.window.geometry('1150x600')
        self.window.minsize(1150, 600)

        self.whatType = Label(self.window, fg='blue', text="What Type Of Vehicle?", height=1, width=70, bd=5, font=('Times New Roman', 18))
        self.whatType.grid(padx=30, pady=15, column=1, row=1, sticky='EW')

        self.vehicle_entry = Text(self.window, height=1, width=75, bd=5, font=('Times New Roman', 18))
        self.vehicle_entry.grid(padx=30, pady=15, column=1, row=2, sticky='EW')

        self.whatYear = Label(self.window, fg='blue', text="What Year?", height=1, width=70, bd=5, font=('Times New Roman', 18))
        self.whatYear.grid(padx=30, pady=15, column=1, row=3, sticky='EW')

        self.year_entry = Text(self.window, height=1, width=75, bd=5, font=('Times New Roman', 18))
        self.year_entry.grid(padx=30, pady=15, column=1, row=4, sticky='EW')

        self.whatMiles = Label(self.window, fg='blue', text="How Many Miles Are On The Vehicle?", height=1, width=70, bd=5, font=('Times New Roman', 18))
        self.whatMiles.grid(padx=30, pady=15, column=1, row=5, sticky='EW')

        self.miles_entry = Text(self.window, height=1, width=75, bd=5, font=('Times New Roman', 18))
        self.miles_entry.grid(padx=30, pady=15, column=1, row=6, sticky='EW')

        self.vehicleID = Label(self.window, fg='blue', text="Vehicle Identification Number?", height=1, width=70, bd=5, font=('Times New Roman', 18))
        self.vehicleID.grid(padx=30, pady=15, column=1, row=7, sticky='EW')

        self.vin_entry = Text(self.window, height=1, width=75, bd=5, font=('Times New Roman', 18))
        self.vin_entry.grid(padx=30, pady=15, column=1, row=8, sticky='EW')

        self.done_button = Button(self.window, fg='blue', state='disabled', text="DONE", bd=5, font=('Times New Roman', 18), command=self.on_done)
        self.done_button.grid(padx=30, pady=15, column=2, row=4, sticky='EW')

        self.nullcheck_button = Button(self.window, fg='blue', state='normal', text="CHECK", bd=5, font=('Times New Roman', 18), command=self.nullCheck)
        self.nullcheck_button.grid(padx=30, pady=15, column=2, row=3, sticky='EW')

        self.window.mainloop()

    def on_done(self):
        vehicle_type = self.vehicle_entry.get(1.0, "end-1c")
        year = self.year_entry.get(1.0, "end-1c")
        miles = self.miles_entry.get(1.0, "end-1c")
        vin = self.vin_entry.get(1.0, "end-1c")

        Database_Maker.insert_vehicle_info(vehicle_type, year, miles, vin)

        vehicleList.append(vehicle_type)
        vehicleList.append(year)
        vehicleList.append(miles)
        vehicleList.append(vin)

        self.window.destroy()
        RepairsGUI()

    def nullCheck(self):
        vehicle_type = self.vehicle_entry.get(1.0, "end-1c")
        year = self.year_entry.get(1.0, "end-1c")
        miles = self.miles_entry.get(1.0, "end-1c")
        vin = self.vin_entry.get(1.0, "end-1c")

        if vehicle_type and year and miles and vin:
            self.done_button.config(state='normal')
        else:
            self.done_button.config(state='disabled')


class RepairsGUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Repairs")
        self.window.geometry('1150x600')
        self.window.minsize(1150, 600)

        self.repairs_label = Label(self.window, fg='green', text="What Repairs Have Been Done?", height=1, width=70, bd=5, font=('Times New Roman', 18))
        self.repairs_label.grid(padx=30, pady=15, column=1, row=1, sticky='EW')

        self.repair_entry = Text(self.window, height=1, width=75, bd=5, font=('Times New Roman', 18))
        self.repair_entry.grid(padx=30, pady=15, column=1, row=2, sticky='EW')

        self.cost_label = Label(self.window, fg='green', text="How Much Did The Repairs Cost?", height=1, width=70, bd=5, font=('Times New Roman', 18))
        self.cost_label.grid(padx=30, pady=15, column=1, row=3, sticky='EW')

        self.repair_cost_entry = Text(self.window, height=1, width=75, bd=5, font=('Times New Roman', 18))
        self.repair_cost_entry.grid(padx=30, pady=15, column=1, row=4, sticky='EW')

        self.done_button = Button(self.window, fg='green', state='disabled', text="INPUT", bd=5, font=('Times New Roman', 18), command=self.on_done)
        self.done_button.grid(padx=30, pady=15, column=2, row=2, sticky='EW')

        self.search_button = Button(self.window, fg='green', state='disabled', text="SEARCH", bd=5, font=('Times New Roman', 18), command=self.on_search)
        self.search_button.grid(padx=30, pady=15, column=2, row=3, sticky='EW')

        self.nullcheck_button = Button(self.window, fg='green', state='normal', text="CHECK", bd=5, font=('Times New Roman', 18), command=self.nullCheck)
        self.nullcheck_button.grid(padx=30, pady=15, column=2, row=1, sticky='EW')

        self.window.mainloop()

    def on_done(self):
        repair = self.repair_entry.get(1.0, "end-1c")
        repair_cost = self.repair_cost_entry.get(1.0, "end-1c")

        Database_Maker.insert_repair_info(repair, repair_cost)

        repairList.append(repair)
        repairList.append(repair_cost)

        self.window.destroy()
        InputGUI()

    def on_search(self):
        repair = self.repair_entry.get(1.0, "end-1c")

        repairList.append(repair)

        self.window.destroy()
        SearchGUI()

    def nullCheck(self):
        repair = self.repair_entry.get(1.0, "end-1c")
        repair_cost = self.repair_cost_entry.get(1.0, "end-1c")

        if repair and repair_cost:
            self.done_button.config(state='normal')
        else:
            self.done_button.config(state='disabled')

        if repair:
            self.search_button.config(state='normal')
        else:
            self.search_button.config(state='disabled')


class InputGUI:
    def __init__(type):
        type.window = Tk()
        type.window.title("Input")
        type.window.geometry('1150x600')
        type.window.minsize(1150, 600)

        type.INPUT = Label(type.window, text = "Your Data Has Been Entered", height = 1, width = 70, bd =5, font=('Times New Roman', 18)) #Text saying it was entered
        type.INPUT.grid(padx=30, pady=15, column = 1, row = 1, sticky = 'EW')

        type.window.mainloop()

class SearchGUI:
    def __init__(type):
        type.window = Tk()
        type.window.title("Search")
        type.window.geometry('1150x600')
        type.window.minsize(1150, 600)

        type.SEARCH = Label(type.window, text = "Data Found Is: "'''#+DATA FOUND''', height = 1, width = 70, bd =5, font=('Times New Roman', 18)) #Text saying it was entered
        type.SEARCH.grid(padx=30, pady=15, column = 1, row = 1, sticky = 'EW')

        type.window.mainloop()

'''class ErrorGUI:
    def __init__(type):
        type.window = Tk()
        type.window.title("Error")
        type.window.geometry('1150x600')
        type.window.minsize(1150, 600)

        type.ERROR = Label(type.window, text = "Please Fill In Required Data", height = 1, width = 70, bd =5, font=('Times New Roman', 18)) #Text saying what was entered is invalid
        type.ERROR.grid(padx=30, pady=15, column = 1, row = 1, sticky = 'EW')

        type.done = Button(type.window, fg = 'green', state = 'normal', text = "DONE", bd =5, font=('Times New Roman', 18), command = type.window.destroy())
        type.done.grid(padx=30, pady=15, column = 2, row = 1, sticky = 'EW') 

        type.window.mainloop() ###I WAS TRYING TO TEST AND SEE IF I COULD USE THIS FOR ERRORS, IGNORE THIS. I AM KEEPING IT JUST IN CASE'''


CustomerGUI() #This is to run the first GUI that sends the user to the next GUI as needed 
print(customerList) #These lists are here just to make sure the inputs are working properly
print(vehicleList)
print(repairList)