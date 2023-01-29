def hotel_cost(night_amount):
    # returns the cost of the hotel by multiplying the night amount by 42 (cost of the hotel per night)
    return night_amount * 42


def plane_cost(city):
    # returns the cost of the flight based on the city chosen
    if city == "london":
        return 86
    elif city == "birmingham":
        return 71
    elif city == "brighton":
        return 59


def car_rental(car_rental_days):
    # return the cost of the car rental by multiplying the car rental days by 76
    return car_rental_days * 76


def holiday_cost(night_amount, city, car_rental_days):
    print(f"The cost of the hotel is £{hotel_cost(night_amount)}")
    print(f"The cost of the flight to {city} is £{plane_cost(city)}")
    print(f"The cost of the car rental for {car_rental_days} days is £{car_rental(car_rental_days)}")
    print(f"The total cost of the holiday is £{hotel_cost(night_amount) + plane_cost(city) + car_rental(car_rental_days)}")


# calls the holiday cost function to display the costs for the holiday based on user inputs
holiday_cost(int(input("Please enter the amount of nights you are staying at the hotel ")),
             input("Please enter the city you are visiting from the following: London, Birmingham, Brighton ").lower(),
             int(input("Please enter the amount of days you are going to rent a car for ")))
