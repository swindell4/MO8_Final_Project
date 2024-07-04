import ProjectSQLite3_Table_Creation

#ProjectSQLite3_Table_Creation.create_table()

main_menu = int(input(" 1. Input New Customer\n 2. Update existing customer\n 3. View existing customer\n 4. View all customers\n"))

while main_menu != 9:

    if main_menu == 1:
        first = str(input("What is your first name? "))
        last = str(input("what is your last name? "))
        vehicle = str(input("What is your vehicle (Model, Make, Year)? "))
        vehicle_id = str(input("What is your license plate number? "))
        phone = str(input("What is your phone number? "))
        repair = str(input("When is the last time you had a repair with us? "))


        ProjectSQLite3_Table_Creation.insert_info(first, last, vehicle, vehicle_id, phone, repair)

        print("\n")

        main_menu = int(input(" 1. Input New Customer\n 2. Update existing customer\n 3. View existing customer\n 4. View all customers\n"))

    #if main_menu == 2:
        #main_menu = int(input(" 1. Input New Customer\n 2. Update existing customer\n 3. View existing customer\n 4. View all customers\n"))

    if main_menu == 3:
        PN = str(input("What is your Phone Number? "))

        ProjectSQLite3_Table_Creation.show_customer_data(PN)

        print("\n")

        main_menu = int(input(" 1. Input New Customer\n 2. Update existing customer\n 3. View existing customer\n 4. View all customers\n"))


    if main_menu == 4:
        ProjectSQLite3_Table_Creation.all_customers()

        print("\n")

        main_menu = int(input(" 1. Input New Customer\n 2. Update existing customer\n 3. View existing customer\n 4. View all customers\n"))

