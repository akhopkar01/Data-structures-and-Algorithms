def fastSelect(Arr, k):  # k is an index
    n = len(Arr)  # length of the original array

    if (k > 0 and k <= n):  # k should be a valid index
        # Helper variables
        setOfMedians = []
        Arr_Less_P = []
        Arr_Equal_P = []
        Arr_More_P = []
        i = 0

        # Step 1 - Break Arr into groups of size 5
        # Step 2 - For each group, sort and find median (middle). Add the median to setOfMedians
        while (i < n // 5):  # n//5 gives the integer quotient of the division
            median = findMedian(Arr, 5 * i, 5)  # find median of each group of size 5
            setOfMedians.append(median)
            i += 1

        # If n is not a multiple of 5, then a last group with size = n % 5 will be formed
        if (5 * i < n):
            median = findMedian(Arr, 5 * i, n % 5)
            setOfMedians.append(median)

        # Step 3 - Find the median of setOfMedians
        if (len(setOfMedians) == 1):  # Base case for this task
            pivot = setOfMedians[0]
        elif (len(setOfMedians) > 1):
            pivot = fastSelect(setOfMedians, (len(setOfMedians) // 2))

        # Step 4 - Partition the original Arr into three sub-arrays
        for element in Arr:
            if (element < pivot):
                Arr_Less_P.append(element)
            elif (element > pivot):
                Arr_More_P.append(element)
            else:
                Arr_Equal_P.append(element)

        # Step 5 - Recurse based on the sizes of the three sub-arrays
        if (k <= len(Arr_Less_P)):
            return fastSelect(Arr_Less_P, k)

        elif (k > (len(Arr_Less_P) + len(Arr_Equal_P))):
            return fastSelect(Arr_More_P, (k - len(Arr_Less_P) - len(Arr_Equal_P)))

        else:
            return pivot

        # Helper function


def findMedian(Arr, start, size):
    myList = []
    for i in range(start, start + size):
        myList.append(Arr[i])

        # Sort the array
    myList.sort()

    # Return the middle element
    return myList[size // 2]

# Solving MaxSum subarray using Divide and Conquer
# Other implementation can be checked in ./Exercises/Algorithms/practice
def maxSubArray(arr):
    '''
    param: An array `arr`
    return: The maximum sum of the contiguous subarray.
    No need to return the subarray itself.
    '''
    return maxSubArrayRecursive(arr, 0, len(arr) - 1)


def maxSubArrayRecursive(arr, start, stop):
    if start == stop:
        return arr[start]

    if start < stop:
        mid = (start + stop) // 2

        L = maxSubArrayRecursive(arr, start, mid)
        R = maxSubArrayRecursive(arr, mid + 1, stop)

        C = maxCrossingSum(arr, start, mid, stop)

        return max(C, max(L, R))
    else:
        return


def maxCrossingSum(arr, start, mid, stop):
    current_left_sum = arr[mid]
    leftMaxSum = arr[mid]

    rightMaxSum = arr[mid + 1]
    current_right_sum = arr[mid + 1]

    for i in range(mid - 1, start - 1, -1):
        current_left_sum += arr[i]
        if current_left_sum > leftMaxSum:
            leftMaxSum = current_left_sum

    for i in range(mid + 2, stop + 1):
        current_right_sum = current_right_sum + arr[i]
        if current_right_sum > rightMaxSum:
            rightMaxSum = current_right_sum

    return leftMaxSum + rightMaxSum

if __name__ == "__main__":
    Arr = [6, 80, 36, 8, 23, 7, 10, 12, 42]
    k = 5
    print(fastSelect(Arr, k))  # Outputs 12

    Arr = [5, 2, 20, 17, 11, 13, 8, 9, 11]
    k = 5
    print(fastSelect(Arr, k))  # Outputs 11

    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print("Maximum Sum = ", maxSubArray(arr))  # Outputs 6

    arr = [-2, 1, -3, 5, 0, 3, 2, -5, 4]
    print("Maximum Sum = ", maxSubArray(arr))  # Outputs 10

    arr = [-2, -5, 6, -2, -3, 1, 5, -6]
    print("Maximum Sum = ", maxSubArray(arr))  # Outputs 7
