# =====importing libraries===========
'''This is the section where you will import libraries'''
from datetime import date
from datetime import datetime

from os import path

def find_duplicate_username(username):
    found_username = False
    users_file = open("user.txt", "r")
    # loop over the users and check to see if the inputted name matches a name in the users.txt file
    for line in users_file:
        modified_line = line.split(",")
        user = modified_line[0]
        if username == user:
            found_username = True

    return found_username


def reg_user(username):
    if username == "admin":
        new_username = input("Please enter a username: ").lower()  # ask the user to input a username

        while find_duplicate_username(new_username) is True:
            print(f"A user with this username has already been used, please provide an alternative username" )
            new_username = input("Please enter a username: ").lower()  # ask the user to input a username

        confirmed_password = False  # declare whether the password has been confirmed
        while confirmed_password is False:  # if the password has not been confirmed
            new_password = input("Please enter a password for this user: ").lower()  # ask the user to input a password
            if input("Please confirm your password: ") == new_password:  # ask the user to confirm their password
                file = open("user.txt", 'a')  # opens the user file with appending write permissions
                file.write(
                    f"\n{new_username}, {new_password}")  # writes the new username and password on a new line
                file.close()  # closes the file now we are finished with it
                confirmed_password = True  # set the password as confirmed allowing the code to re-run
    else:
        print("You do not have permission to add a new user, please ask the admin to do this")


def add_task():
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


def view_all():
    tasks = open("tasks.txt", 'r')
    for line in tasks:  # for each line do the below code
        task_details = line.split(", ")  # split the task details by a comma and a space
        # print the task details in a user-friendly way
        print(
            f"User assigned to task: {task_details[0]}\nTitle: {task_details[1]}\nDescription: {task_details[2]}\nAssigned Date: {task_details[3]}\nDue Date: {task_details[4]}\nTask Completed: {task_details[5]}")


def view_mine():
    tasks = open("tasks.txt", 'r')
    current_tasks = []

    line_index = 0
    for line in tasks:
        # splits the current task and checks to see if it is assigned to the currently logged in user
        split_line = line.split(", ")
        if (split_line[0] == username):
            # add the task ID to the current task to help display it later
            modified_line = str(line_index) + ", " + line
            current_tasks.append(modified_line)
        line_index += 1

    # loop over the current tasks assigned to the current user logged in and display each task and its details
    for i in range(0, len(current_tasks)):
        task_details = current_tasks[i].split(", ")
        print(
            f"Task ID: {task_details[0]}\nUser assigned to task: {task_details[1]}\nTitle: {task_details[2]}\nDescription: {task_details[3]}\nAssigned Date: {task_details[4]}\nDue Date: {task_details[5]}\nTask Completed: {task_details[6]}\n")

    tasks = open("tasks.txt", "r")
    task_data = tasks.readlines()

    chosen_task_id = int(input("Please input the task ID to modify that task or enter -1 to return to the main menu: "))
    if chosen_task_id != -1:
        split_chosen_task = task_data[chosen_task_id].split(", ")
        task_choice = input("please input 'c' to mark this task as complete, or input 'e' to edit the task ").lower()
        if task_choice == "c":
            # add a comma back to each word as it is removed by using the split function
            for i in range(0, len(split_chosen_task)-1):
                split_chosen_task[i] = split_chosen_task[i] + ", "
                print(f"added comma to {split_chosen_task[i]}")

            # change the task to be complete
            split_chosen_task[5] = " Yes\n"
            # join each of the strings in the array together into one string
            task_data[chosen_task_id] = "".join(split_chosen_task)
            tasks = open("tasks.txt", "w")
            tasks.writelines(task_data)
            tasks.close()
        elif task_choice == "e":
            if split_chosen_task[5] == " No\n":
                task_edit = input("Please type 'u' to edit the user assigned to this task, or type 'd' to edit the due date: ").lower()
                if task_edit == "u":
                    edit_task_username(chosen_task_id)
                elif task_edit == "d":
                    edit_task_due_date(chosen_task_id)
            else:
                print("This task cannot be edited as it has already been completed")

# this takes in a string which is a line of text from the tasks file
def edit_task_username(task_ID):
    tasks = open("tasks.txt", "r")
    task_data = tasks.readlines()
    split_chosen_task = task_data[task_ID].split(", ")

    user = input("Please enter the username of the person you would like to be assigned to this task: ").lower()
    split_chosen_task[0] = user

    # add a comma back to each word as it is removed by using the split function
    for i in range(0, len(split_chosen_task) - 1):
        split_chosen_task[i] = split_chosen_task[i] + ", "
        print(f"added comma to {split_chosen_task[i]}")

    task_data[task_ID] = "".join(split_chosen_task)
    tasks = open("tasks.txt", "w")
    tasks.writelines(task_data)
    tasks.close()


def edit_task_due_date(task_ID):
    # open the task file and select the required line and split it into an array
    tasks = open("tasks.txt", "r")
    task_data = tasks.readlines()
    split_chosen_task = task_data[task_ID].split(", ")

    # request a new due date from the user
    due_date = input("Please enter a new due date for the task you would like to be assigned to this task: ")
    split_chosen_task[4] = due_date

    # add a comma back to each word as it is removed by using the split function
    for i in range(0, len(split_chosen_task) - 1):
        split_chosen_task[i] = split_chosen_task[i] + ", "
        print(f"added comma to {split_chosen_task[i]}")

    # set the line to the inputed date and write it back to the file
    task_data[task_ID] = "".join(split_chosen_task)
    tasks = open("tasks.txt", "w")
    tasks.writelines(task_data)
    tasks.close()


def generate_reports():
    tasks = open("tasks.txt", "r")
    task_data = tasks.readlines()

    task_amount = 0
    completed_task_amount = 0
    uncompleted_task_amount = 0
    overdue_task_amount = 0

    for line in task_data:
        task_amount += 1

        #splits the current task up and checks if it has been completed or not and if it is overdue. any found are added to the relevant variable
        split_line = line.split(", ")

        if split_line[5] == "Yes\n":
            completed_task_amount += 1
        else:
            uncompleted_task_amount += 1

        if datetime.strptime(split_line[4], "%d %b %Y").date() < date.today():
            overdue_task_amount += 1

    incomplete_task_percent = (uncompleted_task_amount / task_amount) * 100
    overdue_task_percent = (overdue_task_amount / task_amount) * 100

    # write the task details to the task_overview file
    task_overview = open("task_overview.txt", "w")
    task_overview.write(f"The current total task amount is {task_amount}\n")
    task_overview.write(f"The current total completed task amount is {completed_task_amount}\n")
    task_overview.write(f"The current total uncompleted task amount is {uncompleted_task_amount}\n")
    task_overview.write(f"The current total overdue task amount is {overdue_task_amount}\n")
    task_overview.write(f"The current percentage of uncompleted tasks is %{incomplete_task_percent}\n")
    task_overview.write(f"The current percentage of overdue task is %{overdue_task_percent}\n")

    task_overview.close()

    users = open("user.txt", "r")
    user_data = users.readlines()

    total_users = 0
    overall_total_task_amount = task_amount
    user_list = []

    # declare lists for the user details to be used to write to a file later
    total_tasks_for_users = []
    total_tasks_percentage_for_users = []
    total_completed_tasks_percentage_for_users = []
    total_uncompleted_tasks_percentage_for_users = []
    total_overdue_tasks_percentage_for_users = []

    for line in user_data:
        split_line = line.split(", ")
        user = split_line[0]

        total_users += 1
        user_list.append(user)

        total_tasks_for_current_user = 0
        total_completed_tasks_for_user = 0
        total_uncompleted_tasks_for_user = 0
        total_overdue_tasks_for_user = 0

        for task in task_data:
            #splits the current task line and checks for completed/ uncompleted/ overview stats
            split_task = task.split(", ")
            if split_task[0] == user:
                total_tasks_for_current_user += 1
                if split_task[5] == "Yes\n":
                    total_completed_tasks_for_user += 1
                else:
                    total_uncompleted_tasks_for_user += 1

                if datetime.strptime(split_task[4], "%d %b %Y").date() < date.today():
                    total_overdue_tasks_for_user += 1

        # appends the percentages to the relevant variables whilst checking for a divide by 0 error
        total_tasks_for_users.append(total_tasks_for_current_user)
        if total_tasks_for_current_user != 0:
            total_tasks_percentage_for_users.append((total_tasks_for_current_user / task_amount) * 100)
        else:
            total_tasks_percentage_for_users.append(0)
        if total_completed_tasks_for_user != 0:
            total_completed_tasks_percentage_for_users.append((total_completed_tasks_for_user / total_tasks_for_current_user) * 100)
        else:
            total_completed_tasks_percentage_for_users.append(0)
        if total_uncompleted_tasks_for_user != 0:
            total_uncompleted_tasks_percentage_for_users.append((total_uncompleted_tasks_for_user / total_tasks_for_current_user) * 100)
        else:
            total_uncompleted_tasks_percentage_for_users.append(0)
        if total_overdue_tasks_for_user != 0:
            total_overdue_tasks_percentage_for_users.append((total_overdue_tasks_for_user / total_tasks_for_current_user) * 100)
        else:
            total_overdue_tasks_percentage_for_users.append(0)

    user_overview = open("user_overview.txt", "w")
    user_overview.write(f"There are currently {total_users} users registered\n")
    user_overview.write(f"There are currently {overall_total_task_amount} assigned tasks\n")

    for i in range(0, len(user_list)):
        # write the users stats to the user_overview file
        user_overview.write("\n")
        user_overview.write(f"Stats for user {user_list[i]} are listed below\n")

        user_overview.write(f"The total number of tasks assigned to this user is {total_tasks_for_users[i]}\n")
        user_overview.write(f"The percentage of tasks assigned to this user is %{total_tasks_percentage_for_users[i]}\n")
        user_overview.write(f"The percentage of completed tasks assigned to this user is %{total_completed_tasks_percentage_for_users[i]}\n")
        user_overview.write(f"The percentage of uncompleted tasks assigned to this user is %{total_uncompleted_tasks_percentage_for_users[i]}\n")
        user_overview.write(f"The percentage of overdue tasks assigned to this user is %{total_overdue_tasks_percentage_for_users[i]}\n")

    user_overview.close()




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
    generate_reports_menu = ""
    if username == "admin":
        additional_menu = "s - view statistics amount of tasks and users"
        generate_reports_menu = "gr - generate reports"
    # presenting the menu to the user and
    # making sure that the user input is coneverted to lower case.
    menu = input(f'''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
{additional_menu}
{generate_reports_menu}
e - Exit
: ''').lower()

    if menu == 'r':
        pass
        reg_user(username)

    elif menu == 'a':
        pass
        add_task()

    elif menu == 'va':
        pass
        view_all()

    elif menu == 'vm':
        pass
        view_mine()

    elif menu == 's' and username == "admin":
        #checks to see if one of the generated files doesn't exist and generates them if one doesnt
        if path.isfile("user_overview.txt") == False or path.isfile("tasks.txt") == False:
            generate_reports()

        tasks = open("task_overview.txt", 'r')
        users = open("user_overview.txt", 'r')

        # prints the files to the console
        print(tasks.read())
        print(users.read())

    elif menu == 'gr':
        generate_reports()

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
