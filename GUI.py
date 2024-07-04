#Made by Donivan Hawkins 

#This file holds the GUI. 

from tkinter import * #importing everything from tkinter

vehicleList = [] #Making a list to display back to the user at the end, can be changed later to write it to a file
customerList = [] #Making a list to display back to the user at the end, can be changed later to write it to a file
repairList = [] #Making a list to display back to the user at the end, can be changed later to write it to a file


#IN THE SEARCH GUI AT THE BOTTOM REPLACE THE COMMENT WITH THE DATA YOU HAVE FOUND

class RedirectGUI:
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

        type.window.mainloop() #This is what makes the window run VERY IMPORTANT DO NOT REMOVE, if you need to make a new GUI follow this main guideline and it should work


class CustomerGUI:
    def __init__(type):
        type.window = Tk()
        type.window.title("Customer")
        type.window.geometry('1150x600')
        type.window.minsize(1150, 600)

        type.name = Label(type.window, fg = 'red', text = "Name Of Customer?", height = 1, width = 70, bd =5, font=('Times New Roman', 18)) #Text saying what to do
        type.name.grid(padx=30, pady=15, column = 1, row = 1, sticky = 'EW')

        type.customer = Text(type.window, height = 1, width = 75, bd =5, font=('Times New Roman', 18)) #Text input area for the user to answer
        type.customer.grid(padx=30, pady=15, column = 1, row = 2, sticky = 'EW')

        type.id = Label(type.window, fg = 'red', text = "Identification Number?", height = 1, width = 70, bd =5, font=('Times New Roman', 18))
        type.id.grid(padx=30, pady=15, column = 1, row = 3, sticky = 'EW')

        type.id = Text(type.window, height = 1, width = 75, bd =5, font=('Times New Roman', 18))
        type.id.grid(padx=30, pady=15, column = 1, row = 4, sticky = 'EW')

        type.phone = Label(type.window, fg = 'red', text = "Phone Number?", height = 1, width = 70, bd =5, font=('Times New Roman', 18))
        type.phone.grid(padx=30, pady=15, column = 1, row = 5, sticky = 'EW')

        type.number = Text(type.window, height = 1, width = 75, bd =5, font=('Times New Roman', 18))
        type.number.grid(padx=30, pady=15, column = 1, row = 6, sticky = 'EW')

        type.repairs = Label(type.window, fg = 'red', text = "List Of Repairs Customer Has Had?", height = 1, width = 70, bd =5, font=('Times New Roman', 18))
        type.repairs.grid(padx=30, pady=15, column = 1, row = 7, sticky = 'EW')

        type.repair = Text(type.window, height = 1, width = 75, bd =5, font=('Times New Roman', 18))
        type.repair.grid(padx=30, pady=15, column = 1, row = 8, sticky = 'EW')

        type.done = Button(type.window, fg = 'red', state = 'normal', text = "INPUT", bd =5, font=('Times New Roman', 18), command = lambda: [customerList.append(type.customer.get(1.0, "end-1c")), customerList.append(type.id.get(1.0, "end-1c") ), customerList.append(type.number.get(1.0, "end-1c") ), customerList.append(type.repair.get(1.0, "end-1c") ), type.window.destroy() , InputGUI()])
        type.done.grid(padx=30, pady=15, column = 2, row = 4, sticky = 'EW') #Input button to put everything into the list

        type.search = Button(type.window, fg = 'red', state = 'normal', text = "SEARCH", bd =5, font=('Times New Roman', 18), command = lambda: [customerList.append(type.customer.get(1.0, "end-1c") ), customerList.append(type.id.get(1.0, "end-1c") ), customerList.append(type.number.get(1.0, "end-1c") ), customerList.append(type.repair.get(1.0, "end-1c") ), type.window.destroy() , SearchGUI()])
        type.search.grid(padx=30, pady=15, column = 2, row = 5, sticky = 'EW') #Search button to put everything into the list

       #We now need a text area to display search results and a field to input search data. 

        type.window.mainloop()

class VehicleGUI:
    def __init__(type):
        type.window = Tk()
        type.window.title("Vehicle")
        type.window.geometry('1150x600')
        type.window.minsize(1150, 600)

        type.whatType = Label(type.window, fg = 'blue', text = "What Type Of Vehicle?", height = 1, width = 70, bd =5, font=('Times New Roman', 18)) #Text saying what to do
        type.whatType.grid(padx=30, pady=15, column = 1, row = 1, sticky = 'EW')

        type.vehicle = Text(type.window, height = 1, width = 75, bd =5, font=('Times New Roman', 18)) #Text input area for the user to answer
        type.vehicle.grid(padx=30, pady=15, column = 1, row = 2, sticky = 'EW')

        type.whatYear = Label(type.window, fg = 'blue', text = "What Year?", height = 1, width = 70, bd =5, font=('Times New Roman', 18))
        type.whatYear.grid(padx=30, pady=15, column = 1, row = 3, sticky = 'EW')

        type.year = Text(type.window, height = 1, width = 75, bd =5, font=('Times New Roman', 18))
        type.year.grid(padx=30, pady=15, column = 1, row = 4, sticky = 'EW')

        type.whatMiles = Label(type.window, fg = 'blue', text = "How Many Miles Are On The Vehicle?", height = 1, width = 70, bd =5, font=('Times New Roman', 18))
        type.whatMiles.grid(padx=30, pady=15, column = 1, row = 5, sticky = 'EW')

        type.miles = Text(type.window, height = 1, width = 75, bd =5, font=('Times New Roman', 18))
        type.miles.grid(padx=30, pady=15, column = 1, row = 6, sticky = 'EW')

        type.vehicleID = Label(type.window, fg = 'blue', text = "Vehicle Identification Number?", height = 1, width = 70, bd =5, font=('Times New Roman', 18))
        type.vehicleID.grid(padx=30, pady=15, column = 1, row = 7, sticky = 'EW') #I don't think we need this in the customer window. 

        type.vin = Text(type.window, height = 1, width = 75, bd =5, font=('Times New Roman', 18))
        type.vin.grid(padx=30, pady=15, column = 1, row = 8, sticky = 'EW')

        type.done = Button(type.window, fg = 'blue', state = 'normal', text = "INPUT", bd =5, font=('Times New Roman', 18), command = lambda: [vehicleList.append(type.vehicle.get(1.0, "end-1c") ), vehicleList.append(type.year.get(1.0, "end-1c") ), vehicleList.append(type.miles.get(1.0, "end-1c") ), vehicleList.append(type.vin.get(1.0, "end-1c") ), type.window.destroy(),  InputGUI()])
        type.done.grid(padx=30, pady=15, column = 2, row = 4, sticky = 'EW') 

        type.search = Button(type.window, fg = 'blue', state = 'normal', text = "SEARCH", bd =5, font=('Times New Roman', 18), command = lambda: [vehicleList.append(type.vehicle.get(1.0, "end-1c") ), vehicleList.append(type.year.get(1.0, "end-1c") ), vehicleList.append(type.miles.get(1.0, "end-1c") ), vehicleList.append(type.vin.get(1.0, "end-1c") ), type.window.destroy() , SearchGUI()])
        type.search.grid(padx=30, pady=15, column = 2, row = 5, sticky = 'EW') 

        #We now need a text area to display search results and a field to input search data. 

        type.window.mainloop()

class RepairsGUI:
    def __init__(type):
        type.window = Tk()
        type.window.title("Customer")
        type.window.geometry('1150x600')
        type.window.minsize(1150, 600)

        type.VIN = Label(type.window, fg = 'green', text = "Vehicle Identification Number?", height = 1, width = 70, bd =5, font=('Times New Roman', 18)) #Text saying what to do
        type.VIN.grid(padx=30, pady=15, column = 1, row = 1, sticky = 'EW')

        type.vin = Text(type.window, height = 1, width = 75, bd =5, font=('Times New Roman', 18)) #Text input area for the user to answer
        type.vin.grid(padx=30, pady=15, column = 1, row = 2, sticky = 'EW')

        type.repairs = Label(type.window, fg = 'green', text = "What Repairs Have Been Done?", height = 1, width = 70, bd =5, font=('Times New Roman', 18))
        type.repairs.grid(padx=30, pady=15, column = 1, row = 3, sticky = 'EW')

        type.repair = Text(type.window, height = 1, width = 75, bd =5, font=('Times New Roman', 18))
        type.repair.grid(padx=30, pady=15, column = 1, row = 4, sticky = 'EW')

        #Lets also add a date completed

        type.done = Button(type.window, fg = 'green', state = 'normal', text = "INPUT", bd =5, font=('Times New Roman', 18), command = lambda: [repairList.append(type.vin.get(1.0, "end-1c") ), repairList.append(type.repair.get(1.0, "end-1c") ), type.window.destroy(), InputGUI()])
        type.done.grid(padx=30, pady=15, column = 2, row = 4, sticky = 'EW') 

        type.done = Button(type.window, fg = 'green', state = 'normal', text = "SEARCH", bd =5, font=('Times New Roman', 18), command = lambda: [repairList.append(type.vin.get(1.0, "end-1c") ), repairList.append(type.repair.get(1.0, "end-1c") ), type.window.destroy(), SearchGUI()])
        type.done.grid(padx=30, pady=15, column = 2, row = 4, sticky = 'EW') 

        #We now need a text area to display search results and a field to input search data. 

        type.window.mainloop()

class InputGUI:
    def __init__(type):
        type.window = Tk()
        type.window.title("Customer")
        type.window.geometry('1150x600')
        type.window.minsize(1150, 600)

        type.INPUT = Label(type.window, text = "Your Data Has Been Entered", height = 1, width = 70, bd =5, font=('Times New Roman', 18)) #Text saying it was entered
        type.INPUT.grid(padx=30, pady=15, column = 1, row = 1, sticky = 'EW')

class SearchGUI: #Instead of this we want the results to be displayed in a text area within the corresponding window. 
    def __init__(type):
        type.window = Tk()
        type.window.title("Customer")
        type.window.geometry('1150x600')
        type.window.minsize(1150, 600)

        type.SEARCH = Label(type.window, text = "Data Found Is: "'''#+DATA FOUND''', height = 1, width = 70, bd =5, font=('Times New Roman', 18)) #Text saying it was entered
        type.SEARCH.grid(padx=30, pady=15, column = 1, row = 1, sticky = 'EW')



RedirectGUI() #This is to run the first GUI that sends the user to the next GUI as needed 
print(customerList) #These lists are here just to make sure the inputs are working properly
print(vehicleList)
print(repairList)