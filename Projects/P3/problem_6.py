import random

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
        return None

    min_num = float('inf')
    max_num = -float('inf')
    for num in ints:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num
    return (min_num, max_num)
    pass


if __name__ == "__main__":
    l1 = [i for i in range(0, 10)]  # a list containing 0 - 9
    random.shuffle(l1)
    print ("Pass" if ((0, 9) == get_min_max(l1)) else "Fail")

    l2 = [i for i in range(-15, 20)]
    random.shuffle(l2)
    print ("Pass" if ((-15, 19) == get_min_max(l2)) else "Fail")

    l3 = []
    print("Pass" if (None == get_min_max(l3)) else "Fail")

    l4 = [i for i in range(-20, -4)]
    random.shuffle(l4)
    print("Pass" if ((-20, -5) == get_min_max(l4)) else "Fail")

    l5 = [i for i in range(150, 151)]
    print("Pass" if ((150,150) == get_min_max(l5)) else "Fail")