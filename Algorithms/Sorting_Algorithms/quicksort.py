def quicksort(arr):
    end_index = len(arr)-1
    start_index = 0
    return _sort_(arr, end_index, start_index)

def _sort_(arr, end, start):
    if end <= start:
        return

    pivot_index = _sub_sort_(arr, end, start)
    _sort_(arr, pivot_index-1, start)
    _sort_(arr, end, pivot_index+1)
    return arr

def _sub_sort_(arr, end, start):
    left_idx = start
    pivot_idx = end
    pivot = arr[pivot_idx]

    while pivot_idx != left_idx:
        current = arr[left_idx]
        if current <= pivot:
            left_idx+=1
            continue

        arr[pivot_idx] = current
        arr[left_idx] = arr[pivot_idx-1]
        arr[pivot_idx - 1] = pivot
        pivot_idx-=1
    return pivot_idx


arr = [8, 3, 1, 7, 0, 10, 2]
print(quicksort(arr))
