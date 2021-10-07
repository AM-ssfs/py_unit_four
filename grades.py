
def points(grade, is_AP):
    score = 0
    if grade >= 95:
        score = 4
    elif grade >= 86:
        score = 3
    elif grade >= 78:
        score = 2
    elif grade >= 70:
        score = 1
    else:
        score = 0
    if is_AP:
        score += 0.2
    return score


def main():
    pass


if __name__ == '__main__':
    main()