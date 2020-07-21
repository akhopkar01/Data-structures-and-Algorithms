def iterative_binary_search(arr, target):
    lo = 0
    hi = len(arr)-1

    while True:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            hi = mid-1
        elif target > arr[mid]:
            lo = mid+1
        else:
            break
    return -1

def recursive_binary_search(target, source, left = 0):
    if len(source) == 0:
        return None
    center = (len(source) - 1) // 2
    if source[center] == target:
        return center + left
    elif source[center] < target:
        return recursive_binary_search(target, source[center + 1:], left + center + 1)
    else:
        return recursive_binary_search(target, source[:center], left)


def find_first(arr, target):
    idx = recursive_binary_search(target, arr)
    if idx is None:
        return None
    while arr[idx] == target:
        if idx == 0:
            return 0
        elif arr[idx-1] == target:
            idx-=1
        elif arr[idx] == target:
            return idx


def find_first_last(arr, target):
    idx = recursive_binary_search(target, arr)
    first = idx
    last = idx
    if idx is None:
        return [first, last]
    while arr[first] == target:
        if first == 0:
            break
        elif arr[first-1] == target:
            first-=1
        elif arr[first] == target:
            break

    while arr[last] == target:
        if last == len(arr)-1:
            break

        elif arr[last+1] == target:
            last+=1

        elif arr[last] == target:
            break
    return [first, last]


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 10, 89, 100]
    target = 89
    print(iterative_binary_search(array, target))
    print(recursive_binary_search(target, array))

    array2 = [1,2,2,2,3,3,4,4,4,4,4,4,5,6,7,7,7,8]
    print(find_first(array2, 3))
    print(find_first(array2, 4))
    print(find_first_last(array2, 7))
