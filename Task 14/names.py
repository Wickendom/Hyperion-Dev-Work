name = input("Please enter a name ").lower()  # ask for a name and set the name to lower case so we can detect stop easier

list_of_names = []  # declare the names array
while name != "stop":
    list_of_names.append(name)  # appened the name to the list of names
    name = input("Please enter another name or enter 'stop' to exit the loop").lower()  # ask the user for another name or stop

print(list_of_names)  # if the user input stop, then the list of names will be printed