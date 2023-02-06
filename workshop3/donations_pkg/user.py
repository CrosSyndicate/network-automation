# FOR TESTING PURPOSES
# database = {"Breagan": "password123"}
# username = "Breagan"
# password = "password123"

def login(database, username, password):
    if username in database and password in database.values():
        print("\nWelcome back ", username, "!")
        return str(username)
    if username in database and password not in database.values():
        print("\nInvalid Password for admin.")
        return ""
    elif username not in database and password not in database.values():
        print("\nUser not found. Please register.")
        return ""
    
# login(database, username, password)

def register(database, username):
    if username in database:
        print("\n", username, " has already been registered!")
        return ""
    else:
        print("\n", username, " has been registered successfully!")
        return str(username)

# register(database, username)
# print(username)