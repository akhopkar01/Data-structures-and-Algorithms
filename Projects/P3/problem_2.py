def rotated_array_search(input_list, number):
    if len(input_list) == 0:
        return -1

    return recursive_search(input_list, number, 0, len(input_list)-1)

def recursive_search(arr, target, start, end):
    if start>end:
        return -1

    mid = (start+end)//2

    if target == arr[mid]:
        return mid

    index1 = recursive_search(arr, target, start, mid-1)
    index2 = recursive_search(arr, target, mid+1, end)

    if index1 > index2:
        return index1
    else:
        return index2

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

if __name__ == "__main__":
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 8])
    test_function([[6, 7, 8, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 10])
    test_function([[], 1])
    test_function([[5, 6, 7, 8, 1, 2], 2])
    test_function([[5, 6, 7, 8, 1, 2], 7])