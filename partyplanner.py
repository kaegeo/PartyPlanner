#!/usr/bin/env python3
# Brett Fowler, November 23, 2022, CPT168-W47, Final Exam Project (Party Planner)

#The Party Planner program accepts user input to add attendees to a stored list
# that is saved to the partyplanner.csv file. Users can list, add, edit, and delete
# to and from the list to update the file.


# import csv module to store data as csv file
import csv
# import sys module to support closing program
import sys
# import locale module to format numerical data
import locale

# set locale based on system settings
locale.setlocale(locale.LC_ALL, "")

# establish filename variable for csv file to be utilized
FILENAME = "partyplanner.csv"

# set menu options
MENU = ["Chicken Entree", "Beef Entree", "Vegetarian Meal",
        "Fish Entree", "Pork Entree", "Duck Entree", "Gluten-free Meal"]

# set attendee types
ATTENDEE_TYPES = ["Member", "Guest", "VIP",
                 "Staff(Off-duty)", "Staff(On-duty)", "Volunteer"]

# establish attendee data categories
LIST_CATEGORIES = ["Attendee Name", "Attendee Type", "Menu Choice", "Fee Paid"]

# function for validating user input of integers
def validate_input(user_input, num):
    while True:
        user_input = input("Input option: ")
        if user_input.isdigit() == True:
            if int(user_input) > 0 and int(user_input) < num:
                return user_input
            else:
                print()
                print("Please select a valid option.")
        else:
            print()
            print("Please select a valid option.")

# function for validating user input of float numbers
def validate_float(user_input):
    while True:
        user_input = input("Input fee paid: ")
        try:
            user_input = float(user_input)
            return user_input
        except ValueError:
            print("Please input a valid number.")

# function for easy exiting from within program
def exit_program():
    print("Closing program. Goodbye!")
    sys.exit()

# function to list attendee types for user selection
def list_attendee_types():
    for i, type in enumerate(ATTENDEE_TYPES, start=1):
        print(f"{i}. {type}")
    print()

# function to list menu choices for user selection
def list_menu_choices():
    for i, choice in enumerate(MENU, start=1):
        print(f"{i}. {choice}")
    print()

# function to save list additions and changes to csv file   
def write_attendee_list(attendees):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(attendees)

# function to open and read csv file of attendee list
# and create a new file if the file does not exist
def read_attendee_list():
    try:
        attendees = []
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                attendees.append(row)
        return attendees
    except FileNotFoundError:
        return attendees

# function to enumerate and display attendee data rows
def list_attendees(attendees):
    print()
    print(f"     {LIST_CATEGORIES[0]}\t  {LIST_CATEGORIES[1]}\t\t{LIST_CATEGORIES[2]}\t{LIST_CATEGORIES[3]}")
    print(f"     -------------\t  -------------\t\t-----------\t--------")
    for i, attendee in enumerate(attendees, start=1):
        i = str(i) + "."
        print(f"{i:<4} {attendee[0]:<21}{attendee[1]:<22}{attendee[2]:<18}{float(attendee[3]):>6,.2f}")

# function to display total number of each attendee type
def attendee_totals(attendee_count_dict):
    for item in attendee_count_dict:
        print(f"\t\t\t{item[0]:<16}{item[1]:>3}")

# function to display total number of each menu choice
def menu_totals(menu_count_dict):
    for item in menu_count_dict:
        print(f"{item[0]:<20}{item[1]:>3}")

# function to calculate total amount of fees
def calculate_fees(attendees, total_fees):
    for attendee in attendees:
        total_fees += float(attendee[3])
    return(total_fees)

# function to calculate total number of each attendee type
def attendee_count(attendees, attendee_count_dict):
    total_members = 0
    total_guests = 0
    total_vip = 0
    total_staff_off = 0
    total_staff_on = 0
    total_volunteers = 0
    for attendee in attendees:
        if attendee[1] == "Member":
            total_members += 1
        elif attendee[1] == "Guest":
            total_guests += 1
        elif attendee[1] == "VIP":
            total_vip += 1
        elif attendee[1] == "Staff(Off-duty)":
            total_staff_off += 1
        elif attendee[1] == "Staff(On-duty)":
            total_staff_on += 1
        elif attendee[1] == "Volunteer":
            total_volunteers += 1
    attendee_count_dict.update({"Members": total_members})
    attendee_count_dict.update({"Guests": total_guests})
    attendee_count_dict.update({"VIPs": total_vip})
    attendee_count_dict.update({"Off-duty Staff": total_staff_off})
    attendee_count_dict.update({"On-duty Staff": total_staff_on})
    attendee_count_dict.update({"Volunteers": total_volunteers})
    return(attendee_count_dict)

# function to calculate total number of each menu choice
def menu_count(attendees, menu_count_dict):
    total_chicken = 0
    total_beef = 0
    total_vegetarian = 0
    total_fish = 0
    total_pork = 0
    total_duck = 0
    total_gluten_free = 0
    for attendee in attendees:
        if attendee[2] == "Chicken Entree":
            total_chicken += 1
        elif attendee[2] == "Beef Entree":
            total_beef += 1
        elif attendee[2] == "Vegetarian Meal":
            total_vegetarian += 1
        elif attendee[2] == "Fish Entree":
            total_fish += 1
        elif attendee[2] == "Pork Entree":
            total_pork += 1
        elif attendee[2] == "Duck Entree":
            total_duck += 1
        elif attendee[2] == "Gluten-free Meal":
            total_gluten_free += 1
    menu_count_dict.update({"Chicken Entrees": total_chicken})
    menu_count_dict.update({"Beef Entrees": total_beef})
    menu_count_dict.update({"Vegetarian Meals": total_vegetarian})
    menu_count_dict.update({"Fish Entrees": total_fish})
    menu_count_dict.update({"Pork Entrees": total_pork})
    menu_count_dict.update({"Duck Entrees": total_duck})
    menu_count_dict.update({"Gluten-free Meals": total_gluten_free})
    return(menu_count_dict)

# function to convert dictionary into list of lists
def format_dict(count_dict):
    while True:
        for char in "}{'":
            count_dict = str(count_dict).replace(char, "")
        count_dict = count_dict.split(", ")
        item_list = []
        for item in count_dict:
            item = item.split(": ")
            item_list += item
        count_dict = [item_list[i: i+2] for i in range(0, len(item_list), 2)]
        return count_dict

# function to add new attendee data to the attendee csv file
def add_attendee(attendees):
    name = input("Name: ")
    print()
    print("Select Attendee Type")
    list_attendee_types()
    attendee_type = 0
    attendee_type = validate_input(attendee_type, 7)
    attendee_type = ATTENDEE_TYPES[int(attendee_type) - 1]
    print()
    print("Select Menu Choice")
    list_menu_choices()
    menu_choice = 0
    menu_choice = validate_input(menu_choice, 8)
    menu_choice = MENU[int(menu_choice) - 1]
    print()
    fee_paid = 0
    fee_paid = validate_float(fee_paid)
    attendee = [name, attendee_type, menu_choice, fee_paid]
    attendees.append(attendee)
    write_attendee_list(attendees)
    print()
    print(f"{name} was added.\n")

# function to edit attendee data category information for selected attendee
def edit_attendee(attendees):
    #establish variables for editing attendee list
    list_attendees(attendees)
    modified_item = 0
    attendee_number = 0
    category_number = 0
    print()

    # initiate validation of attendee choice
    attendee_number = validate_input(attendee_number, len(attendees)+1)
    attendee_number = (int(attendee_number) - 1)

    # display attendee data categories for editing    
    print("Select Edit Category")
    print()
    print("1 - Name")
    print("2 - Attendee type")
    print("3 - Menu choice")
    print("4 - Fee paid")
    print()

    # initiate validation of category choice input
    category_number = validate_input(category_number, 5)
    category_number = (int(category_number) - 1)

    # establish variable for attendee list selections        
    attendee = attendees[attendee_number]
    category = attendee[category_number]
    # display verification of category being edited for selected attendee
    print(f"Editing {LIST_CATEGORIES[category_number].lower()} for {attendee[0]}")
    print()

    if category_number == 0:
        modified_item = input("Input new attendee name: ")
        
    elif category_number == 1:
        list_attendee_types()
        modified_item = validate_input(modified_item, 7)
        modified_item = ATTENDEE_TYPES[int(modified_item) - 1]
                
    elif category_number == 2:
        list_menu_choices()
        modified_item = validate_input(modified_item, 8)
        modified_item = MENU[int(modified_item) - 1]
            
    elif category_number == 3:
        modified_item = validate_float(modified_item)
        
    attendees[attendee_number][category_number] = modified_item
    write_attendee_list(attendees)
    print()
    print(f"{LIST_CATEGORIES[category_number].capitalize()} for {attendee[0]} was updated.\n")

# function to delete an attendee from the attendee csv file
def delete_attendee(attendees):
    list_attendees(attendees)
    print()
    selection = 0
    selection = validate_input(selection, len(attendees)+1)
    attendee = attendees.pop(int(selection) - 1)
    write_attendee_list(attendees)
    print(f"{attendee[0]} was deleted.\n")

# function to display report of attendee data, attendee totals, and fee totals
def attendee_report(attendees, total_attendees, total_fees, attendee_count_dict):
    list_attendees(attendees)
    print(f"{'------------------------------------------------':>72}")
    print(f"{'Total attendees':>39}{total_attendees:>4}{'Total of fees':>18} {locale.currency(total_fees):>10}")
    print()
    attendee_totals(attendee_count_dict)

# function to display report of menu choice totals
def menu_report(menu_count_dict):
    print("Menu Choice Totals")
    print("------------------")
    menu_totals(menu_count_dict)

# function to initiate reporting options and run reports based on user choice
def output_report(attendees):
    # establish attendee and menu dictionaries
    attendee_count_dict = {"Members": 0, "Guests": 0, "VIPs": 0,
                           "Off-duty Staff": 0, "On-duty Staff": 0, "Volunteers": 0}
    menu_count_dict = {"Chicken Entrees": 0, "Beef Entrees": 0, "Vegetarian Meals": 0,
                       "Fish Entrees": 0, "Pork Entrees": 0,
                       "Duck Entrees": 0, "Gluten-free Meals": 0}

    # initiate attendee count to calculate attendee totals
    attendee_count_dict = attendee_count(attendees, attendee_count_dict)
    # calculate total of attendees of all types
    total_attendees = sum(attendee_count_dict.values())
    # establish total fees variable
    total_fees = 0
    # calculate total of fees
    total_fees = calculate_fees(attendees, total_fees)
    # initiate format of attendee dictionary into list format
    attendee_count_dict = format_dict(attendee_count_dict)
    # initiate function to calculate menu choice totals
    menu_count_dict = menu_count(attendees, menu_count_dict)
    # initiate format of menu dictionary into list format
    menu_count_dict = format_dict(menu_count_dict)

    # display user options for report functions
    while True:
        print()
        print("---------------------")
        print("Party Planner Reports")
        print("---------------------")
        print("Input Selection")
        print("attendee - Display attendee report")
        print("menu - Display menu report")
        print("sort - Display attendee list sorted by name")
        print("exit - Return to main menu")
        print()
        report_choice = input("Select report to display: ")
        # activate attendee report for display
        if report_choice.lower() == "attendee":
            print()
            attendee_report(attendees, total_attendees, total_fees, attendee_count_dict)
            print()
        # activate menu report for display
        elif report_choice.lower() == "menu":
            print()
            menu_report(menu_count_dict)
            print()
        # sort attendee list by attendee name in ascending order
        elif report_choice.lower() == "sort":
            print()
            list_attendees(sorted(attendees))
        # exit report options and return to main menu
        elif report_choice.lower() == "exit":
            print()
            main()
        else:
            print()
            print("Please select a valid option.")

# function to display main menu of options for user selection            
def display_menu():
    print("-----------------")
    print("The Party Planner")
    print("-----------------")
    print("Input Selection")
    print("list - Display attendee list")
    print("add - Add a new attendee")
    print("edit - Edit existing attendee")
    print("delete - Delete an attendee")
    print("report - Display reports")
    print("exit - Exit the program")
    print()

# main function to initiate program and call functions based on user choice    
def main():
    attendees = read_attendee_list()
    while True:
        print()
        display_menu()
        command = input("Input menu option: ")
        if command.lower() == "list":
            list_attendees(attendees)
        elif command.lower() == "add":
            add_attendee(attendees)
        elif command.lower() == "edit":
            edit_attendee(attendees)
        elif command.lower() == "delete":
            delete_attendee(attendees)
        elif command.lower() == "report":
            output_report(attendees)
        elif command.lower() == "exit":
            exit_program()
        else:
            print()
            print("Please select a valid option.")
            print()

if __name__ == "__main__":
    main()
