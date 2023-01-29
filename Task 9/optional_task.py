employee_type = int(input("Please enter 1 if you are a salesperson or 2 if you are a manager "))

monthly_wage = 0.00

if employee_type == 1:
    gross_amount = round(float(input("Please input your gross sales for the month ")))
    monthly_wage = 2000.00
    monthly_wage += (gross_amount / 100) * 8  # this calculates 8% of the users gross amount and adds it to their wages
else:
    hours_worked = int(input("Please input the amount of hours you have worked this month"))
    monthly_wage = hours_worked * 40.00

print(f"Your monthly wage is R{monthly_wage}")
