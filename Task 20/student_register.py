student_amount = int(input("Please enter the amount of students on this register "))

# creating a file called reg_form with write permissions
file = open('reg_form.txt', 'w')

# loop over the below code equal to an amount the user enters
for line in range(0, student_amount):
    # each student can input their id here and then add a new line for when this code runs again.
    file.write(f"{input('Please enter your student ID number ')} .............................\n")

file.close()  # close the file when we are finished using it
