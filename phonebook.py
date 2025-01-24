# implementing linear search for names

"""

# A list of names
names = ["Yuliia", "David", "John"]

# Ask for name
name = input("Name: ")

# Search for name
for n in names:
    if name == n:
        print("Found")
        break
else:
    print("Not found")

"""

"""

from cs50 import get_string

people = [
    {"name": "Yuliia", "number": "+1-617-495-1000"},
    {"name": "David", "number": "+1-617-495-1000"},
    {"name": "John", "number": "+1-949-468-2750"},
]

# Search for name
name = get_string("Name: ")
for person in people:
    if person["name"] == name:
        print(f"Found {person['number']}")
        break
else:
    print("Not found")

"""

"""
# Implements a phone book using a dictionary

from cs50 import get_string

people = {
    "Yuliia": "+1-617-495-1000",
    "David": "+1-617-495-1000",
    "John": "+1-949-468-2750",
} # dict is implemented using curly braces.

# Search for name
name = get_string("Name: ")
if name in people:
    print(f"Number: {people[name]}") # we can index into the people dictionary using the value of 'name'
else:
    print("Not found")

"""

import csv

name = []
number = []

for i in range(3):
    x = input("Names: ")
    y = input("Number: ")

    name.append(x)
    number.append(y)

file = open("phonebook.csv", "a")

"""
name = input("Name: ")
number = input("Number: ")
"""

#writer = csv.writer(file)

writer = csv.DictWriter(file, fieldnames=["name", "number"]) # save the file with fields

#writer.writerow([name,number])

writer.writerow({"name": name, "number": number})

file.close()

print("File saved as phonebook.csv")
