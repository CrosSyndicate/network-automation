#learning how to import csv data and iterate with python

#just python - this prints the content
import csv
#had to install pandas library
import pandas as pd

def openwith():
    rows = []
    with open("test_users.csv", 'r') as file:
            csvreader = csv.reader(file)
            header = next(csvreader)
            for row in csvreader:
                rows.append(row)

    print("\n***LIST USING WITH CSVREADER METHOD***\n")
    print(header)
    print(rows)
    return

openwith()

#using the .readlines() method

def readlines():
    with open("test_users.csv") as file:
        content = file.readlines()
    header = content[:1]
    rows = content[1:]
    print("\n*** LIST USING READLINES METHOD***\n")
    print(header)
    print(rows)
    return

readlines()

#using pandas library by importing pandas as pd
#this seems cleaner - I will explore using this lib for my script

def pandas_csv():
     data = pd.read_csv("test_users.csv")
     print("\n ***LIST USING PANDAS*** \n")
     print("Header info:\n", data.columns)
     print("\nData in columns:\n", data)


pandas_csv()

def one_column():
     print("\n ***LIST ONE COLUMN USING PANDAS*** \n")
     data = pd.read_csv("test_users.csv", usecols = ['DisplayName'])
     print("\nData only in 'DisplayName':", data)

one_column()






#GRAVEYARD#

# users = open("group_users.csv")

# type(users)

# csvreader = csv.reader(users)

# header = []
# header = next(csvreader)
# header