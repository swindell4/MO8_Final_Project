from tkinter import * #importing everything from tkinter

vehicleList = [] #Making a list to display back to the user at the end, can be changed later to write it to a file
customerList = [] #Making a list to display back to the user at the end, can be changed later to write it to a file
repairList = [] #Making a list to display back to the user at the end, can be changed later to write it to a file


class RedirectGUI:
    def __init__(type):
        type.window = Tk()
        type.window.title("Redirect")
        type.window.geometry('1150x300')
        type.window.minsize(1150, 300)

        type.whatType = Label(type.window, text = "What Information Would You Like To Input?", height = 1, width = 40, bd =5, font=('Times New Roman', 18)) #Text saying what to do
        type.whatType.grid(padx=30, pady=15, column = 1, row = 1, sticky = 'EW')

        type.customer = Button(type.window, state = 'normal', text = "Customer", bd =5, font=('Times New Roman', 18), command = lambda: [ type.window.destroy(), CustomerGUI()])
        type.customer.grid(padx=30, pady=15, column = 2, row = 1, sticky = 'EW')

        type.vehicle = Button(type.window, state = 'normal', text = "Vehicle", bd =5, font=('Times New Roman', 18), command = lambda: [ type.window.destroy(), VehicleGUI()])
        type.vehicle.grid(padx=30, pady=15, column = 3, row = 1, sticky = 'EW')

        type.repairs = Button(type.window, state = 'normal', text = "Repairs", bd =5, font=('Times New Roman', 18), command = lambda: [ type.window.destroy(), RepairsGUI()])
        type.repairs.grid(padx=30, pady=15, column = 4, row = 1, sticky = 'EW')

        type.window.mainloop()


class CustomerGUI:
    def __init__(type):
        type.window = Tk()
        type.window.title("Customer")
        type.window.geometry('1150x600')
        type.window.minsize(1150, 600)

        type.name = Label(type.window, text = "Name Of Customer?", height = 1, width = 70, bd =5, font=('Times New Roman', 18)) #Text saying what to do
        type.name.grid(padx=30, pady=15, column = 1, row = 1, sticky = 'EW')

        type.customer = Text(type.window, height = 1, width = 75, bd =5, font=('Times New Roman', 18)) #Text input area for the user to answer
        type.customer.grid(padx=30, pady=15, column = 1, row = 2, sticky = 'EW')

        type.id = Label(type.window, text = "Identification Number?", height = 1, width = 70, bd =5, font=('Times New Roman', 18))
        type.id.grid(padx=30, pady=15, column = 1, row = 3, sticky = 'EW')

        type.id = Text(type.window, height = 1, width = 75, bd =5, font=('Times New Roman', 18))
        type.id.grid(padx=30, pady=15, column = 1, row = 4, sticky = 'EW')

        type.phone = Label(type.window, text = "Phone Number?", height = 1, width = 70, bd =5, font=('Times New Roman', 18))
        type.phone.grid(padx=30, pady=15, column = 1, row = 5, sticky = 'EW')

        type.number = Text(type.window, height = 1, width = 75, bd =5, font=('Times New Roman', 18))
        type.number.grid(padx=30, pady=15, column = 1, row = 6, sticky = 'EW')

        type.repairs = Label(type.window, text = "List Of Repairs Customer Has Had?", height = 1, width = 70, bd =5, font=('Times New Roman', 18))
        type.repairs.grid(padx=30, pady=15, column = 1, row = 7, sticky = 'EW')

        type.repair = Text(type.window, height = 1, width = 75, bd =5, font=('Times New Roman', 18))
        type.repair.grid(padx=30, pady=15, column = 1, row = 8, sticky = 'EW')

        type.done = Button(type.window, state = 'normal', text = "DONE", bd =5, font=('Times New Roman', 18), command = lambda: [customerList.append(type.name.get(1.0, "end-1c") ), customerList.append(type.id.get(1.0, "end-1c") ), customerList.append(type.phone.get(1.0, "end-1c") ), customerList.append(type.repairs.get(1.0, "end-1c") ), type.window.destroy() ]) #, nextGUI()])
        type.done.grid(padx=30, pady=15, column = 2, row = 4, sticky = 'EW') #Finish button to put everything into the list

        type.window.mainloop()

class VehicleGUI:
    def __init__(type):
        type.window = Tk()
        type.window.title("Vehicle")
        type.window.geometry('1150x600')
        type.window.minsize(1150, 600)

        type.whatType = Label(type.window, text = "What Type Of Vehicle?", height = 1, width = 70, bd =5, font=('Times New Roman', 18)) #Text saying what to do
        type.whatType.grid(padx=30, pady=15, column = 1, row = 1, sticky = 'EW')

        type.vehicle = Text(type.window, height = 1, width = 75, bd =5, font=('Times New Roman', 18)) #Text input area for the user to answer
        type.vehicle.grid(padx=30, pady=15, column = 1, row = 2, sticky = 'EW')

        type.whatYear = Label(type.window, text = "What Year?", height = 1, width = 70, bd =5, font=('Times New Roman', 18))
        type.whatYear.grid(padx=30, pady=15, column = 1, row = 3, sticky = 'EW')

        type.year = Text(type.window, height = 1, width = 75, bd =5, font=('Times New Roman', 18))
        type.year.grid(padx=30, pady=15, column = 1, row = 4, sticky = 'EW')

        type.whatMiles = Label(type.window, text = "How Many Miles Are On The Vehicle?", height = 1, width = 70, bd =5, font=('Times New Roman', 18))
        type.whatMiles.grid(padx=30, pady=15, column = 1, row = 5, sticky = 'EW')

        type.miles = Text(type.window, height = 1, width = 75, bd =5, font=('Times New Roman', 18))
        type.miles.grid(padx=30, pady=15, column = 1, row = 6, sticky = 'EW')

        type.vehicleID = Label(type.window, text = "Vehicle Identification Number?", height = 1, width = 70, bd =5, font=('Times New Roman', 18))
        type.vehicleID.grid(padx=30, pady=15, column = 1, row = 7, sticky = 'EW')

        type.vin = Text(type.window, height = 1, width = 75, bd =5, font=('Times New Roman', 18))
        type.vin.grid(padx=30, pady=15, column = 1, row = 8, sticky = 'EW')

        type.done = Button(type.window, state = 'normal', text = "DONE", bd =5, font=('Times New Roman', 18), command = lambda: [vehicleList.append(type.vehicle.get(1.0, "end-1c") ), vehicleList.append(type.year.get(1.0, "end-1c") ), vehicleList.append(type.miles.get(1.0, "end-1c") ), vehicleList.append(type.vin.get(1.0, "end-1c") ), type.window.destroy() ]) #, nextGUI()])
        type.done.grid(padx=30, pady=15, column = 2, row = 4, sticky = 'EW') #Finish button to put everything into the list

        type.window.mainloop()

class RepairsGUI:
    def __init__(type):
        type.window = Tk()
        type.window.title("Customer")
        type.window.geometry('1150x600')
        type.window.minsize(1150, 600)

        type.VIN = Label(type.window, text = "Vehicle Identification Number?", height = 1, width = 70, bd =5, font=('Times New Roman', 18)) #Text saying what to do
        type.VIN.grid(padx=30, pady=15, column = 1, row = 1, sticky = 'EW')

        type.vin = Text(type.window, height = 1, width = 75, bd =5, font=('Times New Roman', 18)) #Text input area for the user to answer
        type.vin.grid(padx=30, pady=15, column = 1, row = 2, sticky = 'EW')

        type.repairs = Label(type.window, text = "What Repairs Have Been Done?", height = 1, width = 70, bd =5, font=('Times New Roman', 18))
        type.repairs.grid(padx=30, pady=15, column = 1, row = 3, sticky = 'EW')

        type.repair = Text(type.window, height = 1, width = 75, bd =5, font=('Times New Roman', 18))
        type.repair.grid(padx=30, pady=15, column = 1, row = 4, sticky = 'EW')

        type.done = Button(type.window, state = 'normal', text = "DONE", bd =5, font=('Times New Roman', 18), command = lambda: [repairList.append(type.vin.get(1.0, "end-1c") ), repairList.append(type.repair.get(1.0, "end-1c") ), type.window.destroy() ]) #, nextGUI()])
        type.done.grid(padx=30, pady=15, column = 2, row = 4, sticky = 'EW') #Finish button to put everything into the list

        type.window.mainloop()


RedirectGUI()
print(vehicleList)