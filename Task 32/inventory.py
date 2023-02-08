#========The beginning of the class==========
class Shoe:
    country = ""
    code = ""
    product = ""
    cost = 0.0
    quantity = 0

    # initialises the class using this constructor
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    # returns a formatted string based on this shoes data when you print this object
    def __str__(self):
        return f"Shoe details: Country - {self.country}, Code - {self.code}, Product - {self.product}," \
               f" Cost - {self.cost}, quantity - {self.quantity}"

    def get_shoe_data_for_file(self):
        return f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}"


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []
#==========Functions outside the class==============
def read_shoes_data():
    # tries to open the inventory file and creates a shoe object for each line and appends it to the shoe_list var
    try:
        inventory = open("inventory.txt", "r")
        index = 0
        for line in inventory:
            if index > 0:
                split_line = line.split(",")
                shoe = Shoe(split_line[0],split_line[1],split_line[2],float(split_line[3]),int(split_line[4]))
                shoe_list.append(shoe)
            index += 1
    except:
        print("Inventory file not found, please add a file named inventory.txt into the local directory")

def capture_shoes():
    # requests some details for a new shoe asset and add it to the shoe list
    shoe_country = input("Please enter the country for the shoe ")
    shoe_code = input("Please enter the code for the shoe ")
    shoe_product = input("Please enter the product for the shoe ")
    shoe_cost = float(input("Please enter the cost for the shoe "))
    shoe_quantity = int(input("Please enter the quantity for the shoe "))

    shoe_list.append(Shoe(shoe_country,shoe_code,shoe_product,shoe_cost,shoe_quantity))

def view_all():
    # makes sure there is some data in shoe list
    if len(shoe_list) == 0:
        read_shoes_data()

    # prints each shoe data
    for shoe in shoe_list:
        print(shoe)

def re_stock():
    # makes sure there is data in the shoe_list
    if len(shoe_list) == 0:
        read_shoes_data()

    # stores the shoe with the lowest quantity and a variable for the lowest quantity itself
    lowest_quantity_shoe = Shoe
    lowest_quantity = 999

    # find the lowest shoe in the shoe_list
    for shoe in shoe_list:
        if shoe.get_quantity() < lowest_quantity:
            lowest_quantity_shoe = shoe
            lowest_quantity = shoe.quantity

    # asks the user if they would like to add more stock to the shoe with the lowest quantity
    if input(f"The lowest quantity shoe you have in stock is {lowest_quantity_shoe.product} "
             f"with {lowest_quantity_shoe.quantity} left in stock. "
             f"Would you like to add more stock to this? Y/N ").lower() == "y":
        amount = int(input("Please enter the quantity amount you would like to this shoe "))

        # stores each shoe data in a list to write back to the inventory file later
        new_lines = []

        # for each shoe, get the data and check if it matches the lowest quantity shoe
        # if it is the lowest quantity shoe, then update this with the new amount
        # then write all the data back to the inventory file
        for shoe in shoe_list:
            shoe_data = shoe.get_shoe_data_for_file()
            shoe_split_data = shoe_data.split(",")

            if shoe_split_data[1] == lowest_quantity_shoe.code:
                shoe.quantity += amount
                shoe_data = shoe.get_shoe_data_for_file()

            new_lines.append(f"{shoe_data}\n")

        inventory = open("inventory.txt", "w")
        inventory.writelines(new_lines)

def search_shoe(shoe_code):
    # search the shoe list by code
    if len(shoe_list) == 0:
        read_shoes_data()

    # finds and return the requested shoe by code
    for shoe in shoe_list:
        if shoe.code == shoe_code:
            return shoe

    # if no shoe was found, print an error
    print(f"No Shoe found with code {shoe_code}")

def value_per_item():
    # makes sure there is some data in shoe list
    if len(shoe_list) == 0:
        read_shoes_data()

    # prints the total value for each shoe
    for shoe in shoe_list:
        print(f"Total value for {shoe.product} is £{shoe.cost * shoe.quantity}")

def highest_qty():
    highest_shoe_quantity = 0
    highest_shoe = Shoe

    # makes sure there is some data in the shoe list
    if len(shoe_list) == 0:
        read_shoes_data()

    # searches for the shoe with highest quantity
    for shoe in shoe_list:
        if shoe.get_quantity() > highest_shoe_quantity:
            highest_shoe = shoe
            highest_shoe_quantity = shoe.get_quantity()

    print(f"Shoe with highest quantity is {highest_shoe.product} with {highest_shoe_quantity} in stock."
          f" This shoe is for sale")

    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
# create a variable to hold the users input and select a function based on what they requested
request = ""
while request != "quit":
    request = input("Please select an option from the following list. "
            "read inventory/capture/view all/restock/view highest/search/values/quit s").lower()
    if request == "read inventory":
        read_shoes_data()
    elif request == "capture":
        capture_shoes()
    elif request == "view all":
        view_all()
    elif request == "restock":
        re_stock()
    elif request == "view highest":
        highest_qty()
    elif request == "search":
        code = input("Please enter the code for the shoe you require ").upper()
        print(search_shoe(code))
    elif request == "values":
        value_per_item()
    elif request != "quit":
        print("invalid request, please select again from the option list")