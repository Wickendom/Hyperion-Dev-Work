import math

calculation_type = input("Choose either 'investment' or 'bond' from the menu below to proceed: \n"
                         "\n"
                         "investment - to calculate the amount of interest you'll earn on your investment \n"
                         "bond       - to calculate the amount you'll have to pay on a home loan \n").lower()

if calculation_type == "investment":
    deposit_amount = int(input("Please input your deposit amount "))
    interest_amount = int(input("Please input the interest amount as a percentage without the % sign "))
    years_investing = int(input("Please input the amount of years you are planning on investing "))
    interest_type = input("Please input 'simple or 'compound' for the type of interest you would like: ").lower()

    final_result = 0.00
    if interest_type == "simple":
        final_result = deposit_amount * (1+(interest_amount*0.01) * years_investing)

    elif interest_type == "compound":
        final_result = deposit_amount * math.pow((1 + (interest_amount * 0.01)), years_investing)

    print(f"Your investment will earn {final_result}")

elif calculation_type == "bond":
    value_of_house = int(input("Please enter the value of the house "))
    interest_amount = int(input("Please input the interest amount as a percentage without the % sign "))
    repayment_length = int(input("Please input the amount of months you plan to repay the bond "))

    monthly_interest_rate = interest_amount / 12  # create a monthly interest rate to use below

    monthly_repayment = (monthly_interest_rate * value_of_house) / (1 - math.pow((1+monthly_interest_rate), -repayment_length))
    print(f"Your monthly repayment rate is {monthly_repayment}")