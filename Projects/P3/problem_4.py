def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    if len(input_list) < 1:
        return []

    low = 0
    high = len(input_list)-1
    mid = (low+high)//2

    idx = 0
    while idx <= high:
        if input_list[idx] == 0:
            input_list[idx], input_list[low] = input_list[low], input_list[idx]
            low += 1
            idx += 1
        elif input_list[idx] == 1:
            idx += 1
        else:
            input_list[idx], input_list[high] = input_list[high], input_list[idx]
            high -= 1

    return input_list

    pass

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

if __name__ == "__main__":
    test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
    test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
    test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
    test_function([])
    test_function([1,2])
    test_function([2,0,1])
    test_function([1,1,1,1,1,1,1,1,1,0,1,1,1,2,2,2,2,2,0,2,2,2,2,2,2,2,2,2,2])