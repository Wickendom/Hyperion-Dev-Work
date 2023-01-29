number_given = int(input("Please enter a number "))

number_index = 1  # this is going to be the number that is checked to see if it is even or not
even_numbers = []  # this is the array that will hold all the even numbers

while number_index < number_given:  # whilst the index number is lower than the number the user entered
    if number_index % 2 == 0:  # check to see if the current index number is even
        even_numbers.append(number_index)  # if it is, add it to the even numbers array
    number_index += 1  # increase the index by 1 so the loop is not infinite

even_numbers.append(number_given)  # this adds the user input number to the array as it does not get appened in the while loop
print(even_numbers)