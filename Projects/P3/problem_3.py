def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """

    if len(input_list) == 0:
        return [0,0]

    sorted_list = merge_sort(input_list)
    left = ""
    right = ""

    # Alternate odd and even indexes would evenly sort the numbers to get maximum sum
    for i in range(len(sorted_list)):
        if i % 2 == 0:
            left += str(sorted_list[i])
        else:
            right += str(sorted_list[i])
    return [int(left), int(right)]

def merge_sort(input_list):


    if len(input_list) <= 1:
        return input_list

    mid = len(input_list) // 2
    left = input_list[:mid]
    right = input_list[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merged(left, right)

def merged(left, right):
    merged = []
    left_idx = 0
    right_idx = 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            merged.append(right[right_idx])
            right_idx+=1
        else:
            merged.append(left[left_idx])
            left_idx+=1

    merged += left[left_idx:]
    merged += right[right_idx:]
    return merged

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

if __name__ == "__main__":
    test1 = [[1, 2, 3, 4, 5], [531, 42]]
    test2 = [[4, 6, 2, 5, 9, 8], [964, 852]]
    test3 = [[2, 4, 6, 7, 1, 3], [742, 631]]
    test4 = [[], [0,0]]
    test5 = [[1, 6, 4, 4], [64, 41]]
    test6 = [[9, 0, 3, 7], [93, 70]]

    testcases = [test1, test2, test3, test4, test5, test6]

    for test in testcases:
        test_function(test)