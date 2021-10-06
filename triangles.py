def get_length():
    l1 = float(input("l1 "))
    l2 = float(input("l2 "))
    l3 = float(input("l3 "))
    lengths = [l1, l2, l3]
    return lengths

def is_triangle(side1, side2, side3):
    if (side1 + side2) <= side3:
        return False
    elif (side2 + side3) <= side1:
        return False
    elif (side3 + side1) <= side2:
        return False
    else:
        return True

def main():
    lengths = get_length()
    print(lengths)
    if is_triangle(lengths[0], lengths[1], lengths[2]):
        print("is triangle")
    else:
        print("is not triangle")

if __name__ == '__main__':
    main()

