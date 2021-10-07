def simplify_county(county):
    """
    simplifies here so later i don't have to check variations of spelling
    :param county:
    :return:
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
    print(age_county)   # checks to see if this works
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
    :return:
    """
    base_price = 70

    if age < 0:
        new_price = -1
        return new_price

    elif age < 5:
        new_price = 0
        return new_price

    elif county == "M":
        new_price = 60

        if age >= 65:
            new_price = discount(new_price, 50)
            return new_price

        else:
            return new_price

    elif age < 14 and county == "H":
        new_price = discount(base_price, 18)
        return new_price

    elif age >= 65:
        new_price = discount(base_price, 50)

        if county == "P":
            new_price = discount(new_price, 7.5)
            return new_price

        else:
            return new_price


def main():
    age_price = get_age_county()
    final_price = str(get_cost(age_price[0], age_price[1]))
    print("your final price is: " + final_price)


if __name__ == '__main__':
    main()
