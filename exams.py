
def gets_a_zero(total_classes, class_missed):
    """
    :param total_classes:
    :param class_missed:
    :return: True if miss 25% or more of classes, otherwise False
    """
    if class_missed >= (total_classes / 4):
        return True
    else:
        return False
