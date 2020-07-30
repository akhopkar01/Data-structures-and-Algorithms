# def rearrange_digits(input_list):
#     """
#     Rearrange Array Elements so as to form two number such that their sum is maximum.
#
#     Args:
#        input_list(list): Input List
#     Returns:
#        (int),(int): Two maximum sums
#     """
#     # if len(input_list)<=1:
#     #     return input_list
#     #
#     # mid = len(input_list)//2
#     #
#     # left = input_list[:mid]
#     # right = input_list[mid:]
#     #
#     # left = rearrange_digits(left)
#     # right = rearrange_digits(right)
#     sorted_list = sorted(input_list)
#     left = ""
#     right = ""
#
#     for i in range(len(sorted_list)):
#         if i % 2 == 0:
#             left += str(sorted_list[i])
#         else:
#             right += str(sorted_list[i])
#     return [int(left), int(right)]

    # return merge(left, right, first_layer=True)
    # pass

# def _first_merge_(left, right):
#
#

def rearrange_digits(input_list: list, first_layer: bool = False) -> list:
    """
        Rearrange Array Elements so as to form two number such that their sum is maximum.
        Args:
           input_list(list): Input List
           first_layer(bool): placeholder to know if we are in the first layer of the recursion (special case)
        Returns:
           (int),(int): Two maximum sums
        """

    if len(input_list) <= 1:
        return input_list

    mid = len(input_list) // 2
    left = input_list[:mid]
    right = input_list[mid:]

    left = rearrange_digits(left)
    right = rearrange_digits(right)

    return merge(left, right, first_layer)

def merge(left: list, right: list, first_layer: bool = False) -> list:
    merged = []
    left_index = 0
    right_index = 0

    if first_layer:  # Special case for the last merging step
        num_max_left = ''
        num_max_right = ''
        num_to_left = True

        # Alternating between left and right indexes
        while left_index < len(left) and right_index < len(right):
            if left[left_index] > right[right_index]:
                if num_to_left:
                    num_max_left = str(right[right_index]) + num_max_left
                else:
                    num_max_right = str(right[right_index]) + num_max_right
                right_index += 1
            else:
                if num_to_left:
                    num_max_left = str(left[left_index]) + num_max_left
                else:
                    num_max_right = str(left[left_index]) + num_max_right
                left_index += 1

            num_to_left = not num_to_left  # Distribute the numbers on each of the list

        # Exhausting remaining index
        while left_index < len(left):   # left index is not exhausted
            if num_to_left:
                num_max_left = str(left[left_index]) + num_max_left
            else:
                num_max_right = str(left[left_index]) + num_max_right

            left_index += 1
            num_to_left = not num_to_left

        while right_index < len(right):  # right index is not exhausted
            if num_to_left:
                num_max_left = str(right[right_index]) + num_max_left
            else:
                num_max_right = str(right[right_index]) + num_max_right

            right_index += 1
            num_to_left = not num_to_left

        return [int(num_max_left), int(num_max_right)]

    else:  # Normal merging case
        while left_index < len(left) and right_index < len(right):
            if left[left_index] > right[right_index]:
                merged.append(right[right_index])
                right_index += 1
            else:
                merged.append(left[left_index])
                left_index += 1

        merged += left[left_index:]
        merged += right[right_index:]

        return rearrange_digits(merged, first_layer=True)

# def merged(left, right):
#     merged = []
#     left_idx = 0
#     right_idx = 0
#     while left_idx < len(left) and right_idx < len(right):
#         if left[left_idx] > right[right_idx]:
#             merged.append(right[right_idx])
#             right_idx+=1
#         else:
#             merged.append(left[left_idx])
#             left_idx+=1
#
#     merged += left[left_idx:]
#     merged += right[right_idx:]
#     return merged



merger = rearrange_digits([4,6,2,5,9,8])
# print(left)
# print(right)
print(merger)