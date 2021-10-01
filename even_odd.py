def even_or_odd(number):
    if number % 2 == 0:
        return("the number " + str(number) + " is even.")
    else:
        return("the number " + str(number) + " is odd.")


def get_input():
    number = input("Enter an integer and I will tell you if it is even or odd. ")
    return int(number)


def main():
    print(even_or_odd(get_input()))


if __name__ == '__main__':
    main()