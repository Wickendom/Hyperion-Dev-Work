def ask_for_int_input():
    # asks the user for a number and checks if they input a number
    while True:
        try:
            number = int(input("Please enter a number for your calculation "))
            return number

        except:
            print("That was not a valid number, please enter a vaild number")


def ask_for_operation_input():
    # ask the user for an operation and then check to see if they input a valid answer
    while True:
        try:
            operation = input("Please enter one of the following operations +, -, *, / ")
            if operation == "+" or operation == "-" or operation == "*" or operation == "/":
                return operation
            else:
                print("You have not entered a valid operation, please enter a valid operation")
        except:
            print("You have not entered a valid operation, please enter a valid operation")


def do_operation(first_number,operation,second_number):
    # check the input for what operation was requested and then do that operation, write to file and return the result
    if operation == "+":
        answer = first_number + second_number
        write_operation_to_file(first_number,operation,second_number, answer)
        return answer
    elif operation == "-":
        answer = first_number - second_number
        write_operation_to_file(first_number, operation, second_number, answer)
        return answer
    elif operation == "*":
        answer = first_number * second_number
        write_operation_to_file(first_number, operation, second_number, answer)
        return answer
    elif operation == "/":
        answer = first_number / second_number
        write_operation_to_file(first_number, operation, second_number,answer)
        return answer



def write_operation_to_file(first_number, operation, second_number,answer):
    # writes the operation and answer to the operations.txt file
    operations = open("operations.txt", "a")
    operations.write(f"{first_number} {operation} {second_number} = {answer}\n")
    operations.close()


task = input("Please enter o to perform and operation or enter r to ready your previous operations ").lower()
if task == "o":
    #ask the user for each required part of the operation and then print the result and operation
    first_number = ask_for_int_input()
    operation = ask_for_operation_input()
    second_number = ask_for_int_input()

    print(f"The answer to your operations is {do_operation(first_number, operation, second_number)}")
elif task == "r":
    #try open a file with the name a user inputs and prints each line
    while True:
        file_name = input("Please enter the name (including file type) of the file you would like to open ")
        try:
            file = open(file_name, "r")
            for line in file:
                print(line)
            break
        except:
            print("File not found, please enter a valid file name")
