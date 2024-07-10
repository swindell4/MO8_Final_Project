#Made by David Matz 

'''=======================
Vehicle Class Information
======================='''
#This file takes information from the GUI and creates instances of inputted information. 

import GUI_v3

class Vehicle:
    def __init__(self, id: int, make: str, model: str, year: int) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.maintenance_history = []

    def add_maintenance(self, maintenance: dict) -> None:

        self.maintenance_history.append(maintenance)

    def get_vehicle_info(self) -> str:

        return f"{self.year} {self.make} {self.model}"

'''=======================
Customer Class Information
======================='''

class Customer:
    def __init__(self,id: int, name: str, phone: str, vehicle: str) -> None:
        self.id = id
        self.name = name
        self.phone = phone
        self.vehicles = [vehicle]
        self.spent = 0.0
        self.history = []

    def add_vehicle(self, vehicle: Vehicle) -> None:

        self.vehicles.append(vehicle)

    def add_maintenance(self, vehicle: Vehicle, maintenance: dict) -> None:

        if vehicle in self.vehicles:
            vehicle.add_maintenance(maintenance)
            self.spent += maintenance['cost']
            self.history.append(maintenance)

    def get_info(self) -> dict:

        return {
            "ID": self.id,
            "Name": self.name,
            "Phone": self.phone,
            "Vehicles": self.vehicles,
            "Spent": self.spent,
            "History": self.history
        }

'''=======================
Repair / Maintenance Class Information
======================='''

class RepairMaintenanceOptions:

    #list of maintenance and repair options
    #may have too many, but whatevs
    repair_maintenance_options = {
    "Oil Change": {
        "Description": "",
        "Cost": 29.99
    },
    "Tire Rotation": {
        "Description": "",
        "Cost": 19.99
    },
    "Brake Inspection": {
        "Description": "",
        "Cost": 49.99
    },
    "Battery Check": {
        "Description": "",
        "Cost": 19.99
    },
    "Wheel Alignment": {
        "Description": "",
        "Cost": 79.99
    },
    "Transmission Fluid Change": {
        "Description": "",
        "Cost": 89.99
    },
    "Coolant Flush": {
        "Description": "",
        "Cost": 59.99
    },
    "Air Filter Replacement": {
        "Description": "",
        "Cost": 24.99
    },
    "Spark Plug Replacement": {
        "Description": "",
        "Cost": 49.99
    },
    "Timing Belt Replacement": {
        "Description": "",
        "Cost": 299.99
    },
    "Suspension Inspection": {
        "Description": "",
        "Cost": 39.99
    },
    "Exhaust System Inspection": {
        "Description": "",
        "Cost": 29.99
    },
    "Fuel System Cleaning": {
        "Description": "",
        "Cost": 89.99
    },
    "Headlight Restoration": {
        "Description": "",
        "Cost": 19.99
    },
    "Wiper Blade Replacement": {
        "Description": "",
        "Cost": 14.99
    },
    "Brake Fluid Change": {
        "Description": "",
        "Cost": 69.99
    },
    "AC System Service": {
        "Description": "",
        "Cost": 99.99
    },
    "Detailing": {
        "Description": "",
        "Cost": 149.99
    },
    "Engine Diagnostic": {
        "Description": "",
        "Cost": 79.99
    }
}

    def __init__(self) -> None:

        pass

    #add options that are not there just in case
    def add_option(self, name: str, description: str, cost: float) -> None:

        if name in self.repair_maintenance_options:
            print(f"Option '{name}' already exists. Use update_option_cost to change the cost.")

        else:
            self.repair_maintenance_options[name] = {"Description": description, "Cost": cost}

    #changes the cost of an option
    def update_option_cost(self, name: str, new_cost: float) -> None:

        if name in self.repair_maintenance_options:

            self.repair_maintenance_options[name]["Cost"] = new_cost

            for option in self.repair_maintenance_options:

                if option["name"] == name:
                    option["cost"] = new_cost

        else:
            print(f"Option '{name}' not found.")

    #lists all options available
    def get_all_options(self) -> None:

        #name is the option name, detailes is the description/cost
        for name, details in self.repair_maintenance_options.items():

            print(f"Name: {name}")
            print(f"  Description: {details['Description']}")
            print(f"  Cost: ${details['Cost']:.2f}\n")#format two decimals for USD
    
    def returnOptions(self):
        return self.repair_maintenance_options

'''=======================
UI Class Information
======================='''
