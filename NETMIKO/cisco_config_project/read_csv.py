#learning how to import csv data and iterate with python

#just python - this prints the content
import csv

rows = []
with open("test_users.csv", 'r') as file:
          csvreader = csv.reader(file)
          header = next(csvreader)
          for row in csvreader:
            rows.append(row)

print("List using 'with Open'\n")
print(header)
print(rows)

#using the .readlines() method

with open("test_users.csv")









#GRAVEYARD#

# users = open("group_users.csv")

# type(users)

# csvreader = csv.reader(users)

# header = []
# header = next(csvreader)
# header