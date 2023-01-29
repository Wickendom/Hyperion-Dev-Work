name = input("Please input a name: ").lower()  # ask the user for a name and set it to be lowercase

incorrect_names = []  # declare a list to hold the incorrect names
while name != "john":  # if the name variable is not john then do the below code
    incorrect_names.append(name)  # add the name to the incorrect name list
    name = input("Please input a name. Enter the name John to stop this loop: ").lower()  # ask the user for a name again

print(incorrect_names)  # print the incorrect names
