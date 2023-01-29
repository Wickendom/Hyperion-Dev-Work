side1 = float(input("Please enter the length of the first side of the triangle "))
side2 = float(input("Please enter the length of the second side of the triangle "))
side3 = float(input("Please enter the length of the third side of the triangle "))

s = (side1 + side2 + side3) / 2
# I use ** 0.5 in the below calculation which is a shorter version of using math.sqrt.
# I found this out in the below link
# https://stackoverflow.com/questions/70793490/how-do-i-calculate-square-root-in-python
# I thought using this version would be better than importing a library for 1 calculation
area = (s*(s-side1)*(s-side2)*(s-side3)) ** 0.5
print(area)
