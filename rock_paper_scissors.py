from random import randint


def instructions():
    print("play rock, paper scissors with me!")


def get_input():
    x = input("Rock, Paper or Scissors? ")

    if x == ("Rock" or "rock" or "R" or "r" or "1"):
        return 1

    if x == ("Paper" or "paper" or "P" or "p" or "2"):
        return 2

    if x == ("Scissors" or "scissors" or "Scissor" or "scissor" or "S" or "s" or "3"):
        return 3


def get_gen():
    x = randint(1, 3)
    return x


def who_wins(user, computer):
    # 1 is rock, 2 is paper, 3 is scissors

    pass


def main():
    pass


if __name__ == '__main__':
    main()