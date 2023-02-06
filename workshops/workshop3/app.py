from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register

# NOTES: 
# REMEMBER TO REMOVE THE "DATABASE ARGUMENT FROM ALL CALLS TO THE SHOW_HOMEPAGE() FUNCTION"
#INCLUDING WITHIN HOMEPAGE.PY FILE

# 1. LEFT OFF ON TASK 6 - 

# THE FOLLOWING INSTRUCTIONS ARE NOT WORKING PROPERLY RE-EVALUATE

# Update the code for when the user chooses the option to Donate:
# Delete the "TODO" print statement for this option.
# If the value of authorized_user is an empty string, print "You are not logged in."
# Otherwise:
# Declare a variable named donation and assign to it the return value of calling the donate function, with an argument of authorized_user. This return value should be a string, along the lines of "Bob donated $1000.0".
# Add the donation string to the donations list.

database = {"admin": "password123"}
donations = []
authorized_user = ""

while True:

    show_homepage()

    # add donations, database to the arguments in the call above to test in real time

    if authorized_user == "":
        print("You must be logged in to donate.")

    else:
        print("Logged in as:", authorized_user)


    user_option = input("Choose an option:")
    user_option.lower()

    if user_option == "1" or user_option == "login":
        username = input("\nPlease enter username: ")
        password = input("Please enter password: ")
        authorized_user = login(database, username, password)

    elif user_option == "2" or user_option == "register":
        print(database)
        username = input("\nPlease register a username: ")
        password = input("Please register a password: ")
        authorized_user = register(database, username)
        if authorized_user != "":
            database[username] = password

    elif user_option == "3" or user_option == "donate":
        if authorized_user == "":
            print("\nYou are not logged in!")
        else:
            donation = donate(authorized_user)
            donations.append(donation)

    elif user_option == "4" or user_option == "show donations":
        show_donations(authorized_user, donations)

    elif user_option == "5" or user_option == "exit":
        print("Goodbye!")
        break
    else:
        print("\nInvalid choice. Try again.")

