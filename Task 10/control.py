age = int(input("please enter your age"))

if age >= 18:
    print("You are old enough!")
elif age >= 16:  # this checks if the user is 16 or older, however, as the code reached here they are not 18 or older
    print("Almost there.")
else:
    print("You are just too young!")