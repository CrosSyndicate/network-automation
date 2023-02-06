def show_homepage():
    # print("\nRequires database argument.THIS IS HERE TO TEST THE DATABASE: ", database)
    # print("\nRequires donation argument. THIS IS HERE TO TEST THE DONATION LIST: ", str(donations))
    print("")
    print("         === DonateMe Homepage ===       ")
    print("------------------------------------------")
    print("| 1.    Login        | 2.    Register    |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.     Donate      | 4. Show Donations |")
    print("------------------------------------------")
    print("|                5.  Exit                |")
    print("------------------------------------------")

# username = "Breagan"

def donate(username):
    donation_amt = input("Enter amount to donate: ")
    donation_amt = float(donation_amt)
    donation = (username + " has donated $" + str(donation_amt))
    print("Thank you for your donation!")
    return str(donation)

# def donate(username):
#     donation_amt = input("Enter amount to donate: ")
#     if donation_amt != int():
#         print("Must enter a number!")
#     else:
#         donation_amt = float(donation_amt)
#         donation = print(username, "has donated $", donation_amt)
#         print("Thank you for your donation!")
#         return str(donation)

def show_donations(authorized_user, donations):
    print("\n--- All Donations ---")
    if donations == []:
        print("Currently, there are no donations.")
    else:
        for x in donations:
            print(authorized_user +" has donated " + x)


# donate(username)
# print(donate(username))