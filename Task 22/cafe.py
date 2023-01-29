items = ["Tea", "Coffee", "Hot Chocolate", "Sandwich"]  #declare a list of items
# declare a dictionary of items and the stock amount
stock = {
    "Tea": 12,
    "Coffee": 21,
    "Hot Chocolate": 19,
    "Sandwich": 88
}
# declare a prices dictionary
prices = {
    "Tea": 1.99,
    "Coffee": 2.10,
    "Hot Chocolate": 1.70,
    "Sandwich": 3.20
}

total_value = 0.00 # declare a variable to hold the total stock value
stock_values = list(stock.values())  # declare a variable to hold a list of the stock
price_values = list(prices.values()) # declare a variable to hold a list of the prices

for i in range(0, len(stock)): # for each item in stock do the following code
    total_value += stock_values[i] * price_values[i] # add the stock amount times by the items price to the total value

print(f"Total stock value = {total_value}") # print the total value