# declare an Adult class
class Adult:
    name = ""
    age = 0
    hair_colour = ""
    eye_colour = ""

    def __init__(self, name, age, hair_colour, eye_colour):
        self.name = name
        self.age = age
        self.hair_colour = hair_colour
        self.eye_colour = eye_colour

    def can_drive(self):
        print(f"{name} is old enough to drive")


# declare a derived Child class from Adult
class Child(Adult):

    # overrides the can_drive function in the Adult class
    def can_drive(self):
        print(f"{self.name} is too young to drive")

# ask the user for the following inputs
name = input("Please enter your name ")
age = 0
have_age = False
while have_age == False:
    try:
        age = int(input("Please enter your age "))
        have_age = True
    except:
        print("You have entered an invalid age, please enter only whole numbers")

hair_colour = input("Please enter your hair colour ")
eye_colour = input("Please enter your eye colour ")

# check if the person is over 18, if so create an adult class. if not creates a child class and then calls can_drive()
if age >= 18:
    person = Adult(name, age, hair_colour, eye_colour)
    person.can_drive()
else:
    person = Child(name, age, hair_colour, eye_colour)
    person.can_drive()