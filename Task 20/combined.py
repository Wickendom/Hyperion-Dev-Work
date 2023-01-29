temporary_list = []

# open the numbers1 file with read permissions
num1 = open('numbers1.txt', 'r')
for i in num1:
    # add the numbers from numbers1 file to the temporary list
    temporary_list.append(int(i))

# open the numbers1 file with read permissions
num2 = open('numbers2.txt', 'r')
for i in num2:
    # add the numbers from numbers1 file to the temporary list
    temporary_list.append(int(i))

# sort the list of numbers from smallest to largest
temporary_list = sorted(temporary_list)

# create a new file called all_numbers.txt with write permissions, then write the temporary list to it and then close the file
all_nums = open('all_numbers.txt', 'w')
all_nums.write(str(temporary_list))
all_nums.close()
