def sort012(input_list):

    # just sort 0s and 2s correctly
    idx_0 = 0
    idx_2 = len(input_list) - 1

    idx = 0
    while idx <= idx_2:
        if input_list[idx] == 0:
            input_list[idx] = input_list[idx_0]
            input_list[idx_0] = 0
            idx_0 += 1
            idx += 1
        elif input_list[idx] == 2:
            input_list[idx] = input_list[idx_2]
            input_list[idx_2] = 2
            idx_2 -= 1
        else:
            idx += 1
    pass

def pair_sum(arr, target):
    arr = sorted(arr)

    front_idx = 0
    back_idx = len(arr)-1
    while front_idx != back_idx:
        if arr[front_idx] + arr[back_idx] == target:
            return [arr[front_idx], arr[back_idx]]

        elif arr[front_idx] < target - arr[back_idx]:
            front_idx += 1
        else:
            back_idx -= 1

arr = [1, 4, 2, 9, 8]
print(pair_sum(arr, 3))