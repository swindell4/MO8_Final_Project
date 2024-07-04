import sqlite3
import re
import RepairMaintenanceOptions

'''
matchingData function gets results from  what was typed
'''
def matchingData(search):
    results = []
    for option in repair_options:
        if re.match(f".*{search}.*", option, re.IGNORECASE):
            results.append(option)
    return results

'''
updateTextField() updates text field with the matched results of matchingData()
'''
def updateSearch():
    search = searchField.get()
    matches = matchingData(search)
    textField.config(state=NORMAL)
    textField.delete(1.0, END)
    for match in matches:
        textField.insert(END, match + "\n")
    textField.config(state=DISABLED)

'''
searching customer data
'''
def search_customers(search_term: str) -> list:
    conn: sqlite3.Connection = sqlite3.connect('customer_management.db')
