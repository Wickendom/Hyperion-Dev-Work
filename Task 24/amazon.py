def min(num_list):
    # convert the line using this function to a list of numbers
    numbers = get_list(num_list)
    lowest_number = -1
    for num in numbers:  # loop through the numbers to find the highest number
        if num < lowest_number or lowest_number == -1:
            lowest_number = num

    # opens the output.txt file with append write permissions and write the minimum number in there
    out = open("output.txt", 'a')
    out.write(f"The min of {numbers} is {lowest_number}\n")
    out.close()


def max(num_list):
    # convert the line using this function to a list of numbers
    numbers = get_list(num_list)
    highest_number = -1
    for num in numbers:  # loop through the numbers to find the highest number
        if num > highest_number or highest_number == -1:
            highest_number = num

    # opens the output.txt file with append write permissions and write the highest number in there
    out = open("output.txt", 'a')
    out.write(f"The max of {numbers} is {highest_number}\n")
    out.close()


def avg(num_list):
    # convert the line using this function to a list of numbers
    numbers = get_list(num_list)
    total = 0
    for num in numbers:  # loop through the numbers to find the highest number
        total += num

    # opens the output.txt file with append write permissions and write the highest number in there
    out = open("output.txt", 'a')
    out.write(f"The avg of {numbers} is {total / len(num_list)}\n")
    out.close()


def get_list(text):
    # split the line up to remove the first section of the string, for example "min:"
    split_text = text.split(":")
    num_list = split_text[1].replace(",","")  # removes commas in the string
    result = []
    #  loop over the numbers and put them into a list ignoring the newline character
    for char in num_list:
        if char != "\n":
            result.append(int(char))

    return result

# open the input.txt file with read permissions
# the first line has a UTF 8 byte order mark in it causing ï»¿ to appear
# to remove this we use a different encoder for it. this was found by using the following link
# https://stackoverflow.com/questions/34399172/why-does-my-python-code-print-the-extra-characters-%C3%AF-when-reading-from-a-tex
f = open('input.txt', 'r', encoding='utf-8-sig')

for line in f:
    # splits the line up in 2 sections, the first being the function, the second being the numbers
    func = line.split(":")
    # depending on the function this selects what function to call
    if func[0] == "min":
        min(line)
    elif func[0] == "max":
        max(line)
    elif func[0] == "avg":
        avg(line)
