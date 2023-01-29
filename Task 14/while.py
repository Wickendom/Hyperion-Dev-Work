number_given = int(input("Please enter a number "))

list_of_numbers = []  # declare an array of numbers ready to hold inputs

while number_given != -1:  # if the number given by the user is not -1
    list_of_numbers.append(number_given)  # append that number to the list of numbers
    number_given = int(input("Please enter another number of enter -1 to exit the loop "))  # then ask the user for another number and repeat the loop

number_average = 0

for i in list_of_numbers:
    number_average += i  # loop through the list of numbers and add them all together

number_average /= len(list_of_numbers)  #once the numbers have been added together, divide the number by the amount of numbers in the list of numbers
print(number_average)