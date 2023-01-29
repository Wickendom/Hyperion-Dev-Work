# This asks the user for the price of their package but casts it to a float and rounds it to 2 decimal places
package_price = round(float(input("Please enter the price of the package you would like to purchase ")), 2)
delivery_distance_in_kms = int(input("Please enter the distance of the delivery in kms "))

total_cost = package_price
# the user inputs either 1 or 2 for the delivery type
if int(input("Please enter 1 for Air R0.36 per km or enter 2 for freight R0.25 per km ")) == 1:
    total_cost += (0.36 * delivery_distance_in_kms)  # if the user wants Air this option is selected
else:
    total_cost += (0.25 * delivery_distance_in_kms)  # else, freight is selected

# the user inputs 1 or 2 for insurance type
if int(input("Please enter 1 for Full Insurance R50.00 or enter 2 for limited insurance R25.00 ")) == 1:
    total_cost += 50.00  # if the user selected it increases the total amount by 50
else:
    total_cost += 25.00  # else the total amount is increased by 25

# the user inputs 1 or 2 for if the package is a gift
if int(input("Please enter 1 for Gift R15.00 or enter 2 for no gift R0.00 ")) == 1:
    total_cost += 15.00  # if the user wanted it as a gift, it increases the total amount by 15.00

# there is no need to add anything if they did not want it as a gift due to it adding nothing to the total price

# the user inputs 1 or 2 for insurance type
if int(input("Please enter 1 for priority delivery R100.00 or enter 2 for standard delivery R20.00 ")) == 1:
    total_cost += 100.00  # if the user selected priority delivery then increase the total price by 100.00
else:
    total_cost += 20.00  # else the total amount is increased by 20.00

print(f"The final cost of the package is R{total_cost}")