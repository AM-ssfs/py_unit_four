from random import randint
from maximum import max


def instructions():
    print("try to guess my number! (1-10)")


def gen_rand():
    return randint(1, 10)


def get_input():
    return int(input("What number do you think I chose? "))


if __name__ == '__main__':
    instructions()
    num = gen_rand()
    guess = get_input()
    if num == guess:
        print("Congratulations! my number was " + str(num))
    else:
        print("Sorry, my number was " + str(num))
        if num == max(num, guess):
            print("your guess was " + str(num-guess) + " away")
        else:
            print("your guess was " + str(guess-num) + " away")
