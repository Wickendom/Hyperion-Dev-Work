item1 = input("Please enter the name of a product ")
# I am using the letter f before the string inside the below inputs to allow a format where I can
# include the item variables without the need of concatenation
item1_price = float(input(f"Please enter the price of {item1} with 2 decimal places "))
item2 = input("Please enter another name of a product ")
item2_price = float(input(f"Please enter the price of {item2} with 2 decimal places "))
item3 = input("Please enter another name of a product ")
item3_price = float(input(f"Please enter the price of {item3} with 2 decimal places "))

sum_price = item1_price + item2_price + item3_price

# I looked up the round function, so I was able to keep the average price to 2 decimal places,I used the link below
# https://stackoverflow.com/questions/20457038/how-to-round-to-2-decimals-with-python
# In the above link they show the round function with an argument that allows you to control the decimal places
# So I used the same function here, However they converted the output to a string which I do not need in this case
average_price = round((item1_price + item2_price + item3_price) / 3, 2)

print(f"The Total of {item1}, {item2}, {item3} is R{sum_price} and the average price of the items is R{average_price}")
