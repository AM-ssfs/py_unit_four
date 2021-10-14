# Aden Menschik
# Last modified Oct. 12, 2021
# This program helps workers at The Adventure Park determine the price of a ticket


def simplify_county(county):
    """
    checks for variations of county spellings
    simplifies here i don't have to check variations of spelling later
    :param county: (str)
    what county they are in
    :return abbreviated county: (str)
    abbreviated county (first letter)
    """
    county = str(county).upper()
    if county == "MONTGOMERY COUNTY" or county == "MONTGOMERY" or county == "MONT" or county == "MG" or county == "M":
        return "M"
    elif county == "HOWARD COUNTY" or county == "HOWARD" or county == "HOW" or county == "HW" or county == "H":
        return "H"
    elif county == "PRINCE GEORGES COUNTY" or county == "PRINCE GEORGES" or county == "PRINCE GEORGE" or county == "PRINCE" or county == "GEORGE" or county == "PG" or county == "P":
        return "P"
    else:
        return "no"  # returns something so it doesn't cause an error, this can be anything


def get_age_county():
    """
    gets age and county, abbreviates county, then returns them together as a list
    :return age_county: list[ age(int), county(str) ]
    returns them in a list so i can find them both easily and i don't have to get another user input
    """
    age = int(input("How old are you? "))
    county = simplify_county(input("what county are you from? "))   # simplifies county to abbreviation here
    age_county = [age, county]
    return age_county


def discount(price, discount):
    """
    easily used to calculate discounts, helpful later where i do a bunch of them
    :param price: (float)
    the price before i discount it
    :param discount: (float)
    the amount of discount (ex. 17.5% off would be shown as 17.5)
    :return new_price: (float)
    the price after the discount
    """
    new_price = (price * (1-(discount/100)))
    return new_price


def get_cost(age, county):
    """
    the actual price evaluating is done here, returns the 'final' price (however it may not be properly formatted)
    :param age: (int)
    user's age
    :param county: (str)
    user's county (abbreviated)
    :return new_price: (float)
    ticket price based off of age and county
    """
    base_price = 70
    new_price = 0

    if age < 0:
        new_price = -1

    elif age < 5:
        new_price = 0

    elif county == "M":
        new_price = 60

        if age >= 65:
            new_price = discount(new_price, 50)

    elif age < 14 and county == "H":
        new_price = discount(base_price, 18)

    elif age >= 65:
        new_price = discount(base_price, 50)

        if county == "P":
            new_price = discount(new_price, 7.5)

    return new_price


def format_cost(price):
    """
    turns the price into string and into proper currency format (ex. 52.80)
    check number of decimals and adds 0's or rounds to nearest hundredth if needed
    :param price: (float)
    the "final" price from get_cost() before it is formatted correctly
    :return new_price: (str)
    the real final price after formatting it and making it a string
    """

    price = float(price)  # if it was an integer, now it is a float

    if price == -1:
        new_price = -1

    elif (price*10) % 1 == 0:
        # for some reason (price % 0.1) and variations weren't working so i modified it
        new_price = price
        new_price = str(new_price)+"0"  # adds a zero to the end if it is missing a decimal

    elif (price*100) % 1 == 0:
        # if it has the right number of decimals it doesn't change it
        new_price = price

    else:
        # if it has too many decimal places, it rounds down to nearest hundredth
        new_price = price
        new_price *= 100
        new_price = int(new_price)  # rounds down
        new_price /= 100

    return str(new_price)


def main():
    age_price = get_age_county()
    final_price = format_cost(get_cost(age_price[0], age_price[1]))
    print("your ticket price is: $" + final_price)


if __name__ == '__main__':
    main()
