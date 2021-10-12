def simplify_county(county):
    """
    simplifies here i don't have to check variations of spelling later
    :param county:
    :return [age, county]:
    """
    county = str(county).upper()
    if county == "MONTGOMERY COUNTY" or county == "MONTGOMERY" or county == "MONT" or county == "MG" or county == "M":
        return "M"
    elif county == "HOWARD COUNTY" or county == "HOWARD" or county == "HOW" or county == "HW" or county == "H":
        return "H"
    elif county == "PRINCE GEORGES COUNTY" or county == "PRINCE GEORGES" or county == "PRINCE GEORGE" or county == "PRINCE" or county == "GEORGE" or county == "PG" or county == "P":
        return "P"
    else:
        return "no"


def get_age_county():
    """
    gets age and county and returns them together as a list
    :return:
    """
    age = int(input("How old are you? "))
    county = simplify_county(input("what county are you from? "))   # simplifies here
    age_county = [age, county]
    return age_county   # returns them both together so i don't have to make different functions


def discount(price, discount):
    """
    easily used to calculate discounts, helpful later
    :param price:
    :param discount:
    :return:
    """
    new_price = (price * (1-(discount/100)))
    return new_price


def get_cost(age, county):
    """
    the actual price evaluating is done here, returns final price as float
    :param age:
    :param county:
    :return new_price:
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
    :param price:
    :return:
    """

    price = float(price)

    if price == -1:
        new_price = -1

    # this is unnecessary
    # elif price % 1 == 0:
        # new_price = price
        # new_price = str(new_price)+"0"

    elif (price*10) % 1 == 0:
        # for some reason (price % 0.1) and variations weren't working so i modified it
        new_price = price
        new_price = str(new_price)+"0"

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
    print("your final price is: $" + final_price)


if __name__ == '__main__':
    main()
