def instructions():
    print("this tells you your modified salary based off years and current salary")


def get_year():
    year = int(input("how long have you worked here? (in years) "))
    return year


def get_sal():
    salary = int(input("what is your salary? (in dollars) "))
    return salary


def bonus_sal(sal):
    return sal*1.05


def main():
    instructions()
    if get_year() >= 5:
        print(bonus_sal(get_sal()))
    else:
        print(get_sal())


if __name__ == '__main__':
    main()