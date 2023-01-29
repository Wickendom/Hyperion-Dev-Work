# =====importing libraries===========
'''This is the section where you will import libraries'''
from datetime import date
# ====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''
username = ""  #sets a global variable for the username that will be input by the user
users = open("user.txt", 'r')  # gets and reads the user file
list_of_users = []  # declare a list of users
list_of_passwords = []  # declare a list of passwords using the same index as the usernames

for line in users:  # run this code for the amount of lines in the user file
    split_line = line.split(", ")  #splits the username and password into an array
    list_of_users.append(split_line[0])  # adds the username to the list of usernames
    list_of_passwords.append(split_line[1].replace("\n", ""))  # adds the password to the list of passwords and removes the newline character
found_username = False # declare a variable to hold whether a valid username has been found
found_user = False  # set a variable to hold whether a valid user has been found using the correct password

password_id = 0  # create a variable that holds an index of the password that is needed

while not found_user:  # whilst a valid user has not been found do the following code

    split_line = ""

    if found_username is False:  # if a valid username has not been input yet do this code
        username = input("Please enter your username: ").lower()  # ask the user for a username
        for i in range(0, len(list_of_users)):  # go through the list of usernames
            if username == list_of_users[i]:  # if the username at the current index matches the users input
                found_username = True  # then set the username to be found allowing the prompt for a password
                password_id = i  # this sets the password id to the current index so the current password is needed to be found

    if found_username is True:  # if a valid username has been found
        password = input("Please enter your password: ")  # ask the user for the password
        if password == list_of_passwords[password_id]:  # if the password input matches the password at the same index as the username input
                found_user = True  # set the user as found so the next section of code can run

while True:
    additional_menu = ""
    if username == "admin":
        additional_menu = "s - view statistics amount of tasks and users"
    # presenting the menu to the user and
    # making sure that the user input is coneverted to lower case.
    menu = input(f'''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
{additional_menu}
e - Exit
: ''').lower()

    if menu == 'r':
        pass
        '''In this block you will write code to add a new user to the user.txt file
        - You can follow the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same.
            - If they are the same, add them to the user.txt file,
            - Otherwise you present a relevant message.'''
        if (username == "admin"):
            new_username = input("Please enter a username: ").lower()  # ask the user to input a username
            confirmed_password = False  # declare whether the password has been confirmed
            while confirmed_password is False:  # if the password has not been confirmed
                new_password = input("Please enter a password: ").lower()  # ask the user to input a password
                if input("Please confirm your password :") == new_password:  # ask the user to confirm their password
                    file = open("user.txt", 'a')  # opens the user file with appending write permissions
                    file.write(f"\n{new_username}, {new_password}")  # writes the new username and password on a new line
                    file.close()  # closes the file now we are finished with it
                    confirmed_password = True  # set the password as confirmed allowing the code to re-run
        else:
            print("You do not have permission to add a new user, please ask the admin to do this")

    elif menu == 'a':
        pass
        '''In this block you will put code that will allow a user to add a new task to task.txt file
        - You can follow these steps:
            - Prompt a user for the following: 
                - A username of the person whom the task is assigned to,
                - A title of a task,
                - A description of the task and 
                - the due date of the task.
            - Then get the current date.
            - Add the data to the file task.txt and
            - You must remember to include the 'No' to indicate if the task is complete.'''

        # prompt for the task details for the task
        user_to_add = input("Please enter the username of the person to assign to this task: ")
        task_title = input("Please enter the tile of the task: ")
        task_desc = input("Please enter the description of the task: ")
        task_due_date = input("Please enter the due date of the task: ")

        task_file = open("tasks.txt", 'a')  # open the tasks file with write permissions to append
        current_date = date.today().strftime("%d %b %Y")  # get the current date in the correct format
        task_file.write(
            f"\n{user_to_add}, {task_title}, {task_desc}, {current_date}, {task_due_date}, No")  # write the details to the file
        task_file.close()  # close the file now we have finished with it



    elif menu == 'va':
        pass
        '''In this block you will put code so that the program will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 
            - It is much easier to read a file using a for loop.'''

        tasks = open("tasks.txt", 'r')
        for line in tasks:  # for each line do the below code
            task_details = line.split(", ")  # split the task details by a comma and a space
            # print the task details in a user-friendly way
            print(f"User assigned to task: {task_details[0]}\nTitle: {task_details[1]}\nDescription: {task_details[2]}\nAssigned Date: {task_details[3]}\n Due Date: {task_details[4]}\nTask Completed: {task_details[5]}")

    elif menu == 'vm':
        pass
        '''In this block you will put code the that will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the username you have
            read from the file.
            - If they are the same print it in the format of Output 2 in the task PDF'''

        tasks = open("tasks.txt", 'r')
        current_tasks = []

        for line in tasks:
            split_line = line.split(", ")
            if(split_line[0] == username):
                current_tasks.append(line)

        for i in range(0, len(current_tasks)):
            task_details = current_tasks[i].split(", ")
            print(f"User assigned to task: {task_details[0]}\nTitle: {task_details[1]}\nDescription: {task_details[2]}\nAssigned Date: {task_details[3]}\nDue Date: {task_details[4]}\nTask Completed: {task_details[5]}\n")

    elif menu == 's' and username == "admin":
        tasks = open("tasks.txt", 'r')
        users = open("user.txt", 'r')
        print(f"Amount of tasks = {len(tasks.readlines())}\n"
              f"Amount of users = {len(users.readlines())}")

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
