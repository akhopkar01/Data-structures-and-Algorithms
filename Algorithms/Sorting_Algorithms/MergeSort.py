def mergesort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)

def merge(left, right):
    merged = []
    left_idx = 0
    right_idx = 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] > right[right_idx]:
            merged.append(right[right_idx])
            right_idx += 1
        else:
            merged.append(left[left_idx])
            left_idx += 1
    merged+=left[left_idx:]
    merged+=right[right_idx:]

    return merged


def count_inversions(arr):
    start_index = 0
    end_index = len(arr) - 1
    output = inversion_count_func(arr, start_index, end_index)
    return output


def inversion_count_func(arr, start_index, end_index):
    if start_index >= end_index:
        return 0

    mid_index = start_index + (end_index - start_index) // 2

    # find number of inversions in left-half
    left_answer = inversion_count_func(arr, start_index, mid_index)

    # find number of inversions in right-half
    right_answer = inversion_count_func(arr, mid_index + 1, end_index)

    output = left_answer + right_answer

    # merge two sorted halves and count inversions while merging
    output += merge_two_sorted_halves(arr, start_index, mid_index, mid_index + 1, end_index)
    return output


def merge_two_sorted_halves(arr, start_one, end_one, start_two, end_two):
    count = 0
    left_index = start_one
    right_index = start_two

    output_length = (end_two - start_two + 1) + (end_one - start_one + 1)
    output_list = [0 for _ in range(output_length)]
    index = 0

    while index < output_length:
        # if left <= right, it's not an inversion
        if arr[left_index] <= arr[right_index]:
            output_list[index] = arr[left_index]
            left_index += 1

        else:
            count = count + (end_one - left_index + 1)  # left > right hence it's an inversion
            output_list[index] = arr[right_index]
            right_index += 1

        index = index + 1

        if left_index > end_one:
            for i in range(right_index, end_two + 1):
                output_list[index] = arr[i]
                index += 1
            break

        elif right_index > end_two:
            for i in range(left_index, end_one + 1):
                output_list[index] = arr[i]
                index += 1
            break

    index = start_one
    for i in range(output_length):
        arr[index] = output_list[i]
        index += 1
    return count


def case_sort(string):
    upper_case_idx = 0
    lower_case_idx = 0

    sorted_string = sorted(string)
    output = ""


    for i, char in enumerate(sorted_string):
        if 97 <= ord(char) <= 127:
            lower_case_idx = i
            break

    for char in string:
        ascii_val = ord(char)
        if 97 <= ascii_val <= 127:
            output+=sorted_string[lower_case_idx]
            lower_case_idx+=1
        else:
            output+=sorted_string[upper_case_idx]
            upper_case_idx+=1
    return output

test_list_1 = [8, 3, 1, 7, 0, 10, 2]
test_list_2 = [1, 0]
test_list_3 = [97, 98, 99]

print('{} to {}'.format(test_list_1, mergesort(test_list_1)))
print('{} to {}'.format(test_list_2, mergesort(test_list_2)))
print('{} to {}'.format(test_list_3, mergesort(test_list_3)))

print(count_inversions([2, 5, 1, 3, 4]))

print(case_sort('fedRTSersUXJ'))
