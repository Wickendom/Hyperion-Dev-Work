#import the statistics module as we require this to find the median
import statistics

list_of_numbers = []
print("this program will ask you to input 10 numbers below")
for i in range(0, 10):
    #  ask the user 10 times for a number and input it into the array we declared earlier
    list_of_numbers.append(float(input("please input a number ")))

total_of_numbers = 0.00

for num in list_of_numbers:
    # loop over each number and add it to the total, this creates a total sum of the numbers
    total_of_numbers += num

print(f"The total of the inputted numbers is {total_of_numbers}")

# prints the highest number in the list and the index where it is
print(f"The highest number is {max(list_of_numbers)} at index {list_of_numbers.index(max(list_of_numbers))}")
# prints the lowest number in the list and the index where it is
print(f"The lowest number is {min(list_of_numbers)} at index {list_of_numbers.index(min(list_of_numbers))}")

# this prints the average of the numbers by using the total value divided by the amount of numbers in the list
print(f"the average of the numbers you inputted is {round(total_of_numbers/ len(list_of_numbers),2)}")

# this prints the median of the list of numbers using the statistics module we imported
print(f"The median of the numbers you inputted is {statistics.median(list_of_numbers)}")