str_manip = input("please enter a sentence ")
print("the length of the sentence is " + str(len(str_manip)))
print(str_manip.replace(str_manip[(len(str_manip) - 1)],"@"))
str_length = len(str_manip)
print(str_manip[:str_length-4:-1])
print(str_manip[:3] + str_manip[str_length - 2:]) #this gets the first 3 characters and concatinates them to the last 2 characters
print(str_manip.split())