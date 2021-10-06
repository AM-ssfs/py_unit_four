from random import randint


def instructions():
    """
    tells user they are about to play rock paper scissors
    :return:
    """
    print("play rock paper scissors with me!")


def get_input():
    """
    gets input and returns 1, 2, or 3 (rck, ppr, scrs)
    :return:
    """
    x = input("Rock, Paper or Scissors? ")

    if x.upper() == "ROCK" or x.upper() == "R" or x.upper() == "1":
        return 1

    if x.upper() == "PAPER" or x.upper() == "P" or x.upper() == "2":
        return 2

    if x.upper() == "SCISSORS" or x.upper() == "SCISSOR" or x.upper() == "S" or x.upper() == "3":
        return 3


def get_gen():
    """
    gen random int 1-3, (inclusive)
    :return:
    """
    x = randint(1, 3)
    return x


def who_wins(user, computer):
    """
    fetches user and computer input, evaluates, then returns who wins
    :param user:
    :param computer:
    :return:
    """
    if user == 1:
        if computer == 1:
            return "tied"
        elif computer == 2:
            return "lose"
        else:
            return "win"
    elif user == 2:
        if computer == 1:
            return "win"
        elif computer == 2:
            return "tied"
        else:
            return "lose"
    else:
        if computer == 1:
            return "lose"
        elif computer == 2:
            return "win"
        else:
            return "tied"


def dialouge(user, computer, outcome):
    """
    actually prints who won
    :param user:
    :param computer:
    :param outcome:
    :return:
    """
    rps = ["rock", "paper", "scissor"]
    print("you chose " + rps[user-1] + " and I chose " + rps[computer-1])
    print("you " + outcome)


if __name__ == '__main__':
    instructions()
    user = get_input()
    computer = get_gen()
    outcome = who_wins(user, computer)
    dialouge(user, computer, outcome)
