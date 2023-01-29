file = open("DOB.txt", "r")  # this opens the DOB file with only permissions to read

birthdays = []  # declare a list to hold birthdates

print("Names")
for line in file:  # loop over every line in the file
    split_line = line.split()  # split the lines into separate strings
    print(f"{split_line[0]} {split_line[1]}")  # print the fist and last name
    birthdays.append(f"{split_line[2]} {split_line[3]} {split_line[4]}")  # appends the birthdate to a list of birthdates

print("Birthdate")
for i in birthdays:  # loop over every line in the birthdate list
    print(i)  # print the current index of the birthdate list