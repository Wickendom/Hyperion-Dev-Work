height = float(input("Please enter your height in Meters "))
weight = float(input("Please enter your weight in kg "))

BMI = weight / (height * height)  # This calculates the BMI of the user
BMI_weight = ""  # This declares a variable to hold what the user is to be used in the below code

if BMI >= 30:
    BMI_weight = "Obese"
elif BMI >= 25:
    BMI_weight = "Overweight"
elif BMI >= 18.5:
    BMI_weight = "Normal"
else:
    BMI_weight = "Underweight"

print(f"Your BMI is {round(BMI,2)} which means you are {BMI_weight}")
