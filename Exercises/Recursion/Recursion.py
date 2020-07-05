import copy

def add_one(arr):
    if arr == [9]:
        return [1, 0]
    borrow = 1
    digits = borrow + arr[-1]

    if digits // 10:
        arr[-1] = 0
        new_arr = arr[:-1]
        arr = add_one(new_arr) + [arr[-1]]
    else:
        arr[-1] = digits

    return arr

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

def is_palindrome(string):

    if len(string) == 0:
        return True

    first_char = string[0]
    last_char = string[-1]

    if first_char == last_char and is_palindrome(string[1:-1]):
        return True
    return False


def reverse_string(string):

    reverse = ""
    if len(string) == 0:
        return ""
    first_char = string[0]
    reverse += reverse_string(string[1:]) + first_char
    return reverse


def permute(inputList):
    finalCompoundList = []
    if len(inputList) == 0:
        finalCompoundList.append([])

    else:
        first_element = inputList[0]
        rest = inputList[1:]

        subCompoundList = permute(rest)
        print(subCompoundList)

        for aList in subCompoundList:
            for j in range(len(aList)+1):
                bList = copy.deepcopy(aList)
                bList.insert(j, first_element)

                finalCompoundList.append(bList)
        return finalCompoundList

def string_permutations(string):
    permute = []
    substring=''
    if len(string) == 0:
        return ['']

    first_char = string[0]
    rest = string[1:]

    substring = string_permutations(rest)
    print(substring)
    # return return_permutations(string, 0)


def return_permutations(string, index):
    # output to be returned
    output = list()

    # Terminaiton / Base condition
    if index >= len(string):
        return [""]

    # Recursive function call
    small_output = return_permutations(string, index + 1)

    # Pick a character
    current_char = string[index]

    # Iterate over each sub-string available in the list returned from previous call
    for subString in small_output:

        # place the current character at different indices of the sub-string
        for index in range(len(small_output[0]) + 1):
            # Make use of the sub-string of previous output, to create a new sub-string.
            new_subString = subString[0: index] + current_char + subString[index:]
            output.append(new_subString)

    return output


def tower_of_hanoi(num_disks):
    return _tower_of_hanoi_helper(num_disks, 'S', 'D', 'A')

def _tower_of_hanoi_helper(num_disks, s, d, a):
    if num_disks == 0:
        return
    if num_disks == 1:
        print("{} {}".format(s, d))
        return

    _tower_of_hanoi_helper(num_disks-1, s, d, a)
    print("{} {}".format(s,d))
    _tower_of_hanoi_helper(num_disks-1, a, s, d)


def all_codes(number):
    """
    :param: number - input integer
    Return - list() of all codes possible for this number
    TODO: complete this method and return a list with all possible codes for the input number
    """
    if number == 0:
        return [""]

    rem = number % 100
    out = []
    if rem < 26 and number > 9:
        out = all_codes(number // 100)
        alpha = codes(rem)

        for i, element in enumerate(out):
            out[i] = element + alpha

    rem = number % 10
    out_10 = all_codes(number // 10)
    alpha = codes(rem)
    for i, element in enumerate(out_10):
        out_10[i] = element + alpha
    output = []
    output = out + out_10
    return output

    pass


def codes(number):
    codes = {
        1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j',
        11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't',
        21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'
    }
    if number > 26:
        return -1
    return codes[number]


def subsets(arr):
    return return_subsets(arr, 0)

def return_subsets(arr, index):
    if index >= len(arr):
        return [[]]

    small_output = return_subsets(arr, index + 1)

    output = list()
    # append existing subsets
    for element in small_output:
        output.append(element)

    # add current elements to existing subsets and add them to the output
    for element in small_output:
        current = list()
        current.append(arr[index])
        current.extend(element)
        output.append(current)
    return output


def staircase(n):
    '''Hint'''
    # Base Case - What holds true for minimum steps possible i.e., n == 0, 1, 2 or 3? Return the number of ways the child can climb n steps.
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2

    if n == 3:
        return 4
    # Recursive Step - Split the solution into base case if n > 3.
    if n > 3:
        steps = staircase(n - 1) + staircase(n - 2) + staircase(n - 3)
    return steps


def last_index(arr, target):
    # we start looking from the last index
    return last_index_arr(arr, target, len(arr) - 1)


def last_index_arr(arr, target, index):
    if index < 0:
        return -1

    # check if target is found
    if arr[index] == target:
        return index

    # else make a recursive call to the rest of the array
    return last_index_arr(arr, target, index - 1)

if __name__ == "__main__":
    t1, t2, t3 = [1, 9, 9],  [9,9,9], [1,2,3]
    print(add_one(t1), add_one(t2), add_one(t3))

    print(is_palindrome("madam"))
    print(reverse_string("soumyaa"))

    # permute([1, 0, 2])
    string_permutations("abc")
    tower_of_hanoi(num_disks=3)