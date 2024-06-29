import re 
def matchingData(): #This function will be used to match data from the search field to the data in the database. 
    results = [] #This list ill contain all the matchins results to the data within the search field. 
    search = searchField.get() #This will capture th current data in the search field. 
    for data in database.db: #This loop will iterate through the contents of the database and 
        if re.match(data, search): #This if statement checks to see if the currently observed database element has the same data as what 
#currently resides in the serch field. 
            results.append(data) #This adds that data to a list called "results". 
    return results #This returns the list to be used in another file for showing the list in a text field for the user. 