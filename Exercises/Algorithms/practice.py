def add_one_1(arr):
    i = 0
    pw = len(arr)
    number= 0
    while pw != 0:
        number+= (10**(pw-1)) * arr[i]
        i+=1
        pw-=1
    new_number = number+1
    new_arr = []
    num = new_number
    while num//10 != 0:
        rem = num%10
        num = num//10
        new_arr.append(rem)
    new_arr.append(num)
    return new_arr[::-1]

def add_one_2(arr):
    #Borrow logic
    borrow = 1
    for i in range(len(arr), 0, -1):
        digit = borrow + arr[i-1]

        borrow = digit//10

        if borrow==0:
            arr[i-1] = digit
            break

        else:
            arr[i-1] = digit % 10
    arr = [borrow] + arr
    position =0
    while arr[position] == 0:
        position+=1
    return arr[position:]

def duplicate_number1(arr):

    nmap = {}
    for i in range(0, len(arr)-1):
        nmap[i] = 0
    print(nmap)
    for num in arr:
        nmap[num]+=1
    return max(nmap, key=nmap.get)


def duplicate_number2(arr):
    # Since the numbers in array is 0 to n-1, the element occur just once
    current_sum = 0
    expected_sum = 0
    for num in arr:
        current_sum+=num

    for num in range(len(arr)-1):
        expected_sum+=num

    return current_sum-expected_sum

def max_sum_subarray(arr):
    # A running sum is maintained along with the maximum sum through it
    current_sum = arr[0] #Running sum
    max_sum = arr[0] #Max sum

    for num in arr[1:]:
        current_sum = max(current_sum+num, num)
        max_sum = max(current_sum, max_sum)
    return max_sum


def n_row_pascal(n):
    row = [1]

    for i in range(1, n+1):
        previous_row = row

        row = [1]
        for j in range(1, i):
            new_num = previous_row[j] + previous_row[j-1]
            row.append(new_num)

        row.append(1)
    return row

if __name__ == "__main__":

    print(add_one_1([9, 9, 9]))
    print(add_one_2([9, 9, 9]))
    print(duplicate_number1([0, 2, 3, 1, 4, 5, 3]))
    print(duplicate_number2([0, 2, 3, 1, 4, 5, 3]))
    print(max_sum_subarray([1,-2, 3, 4, -5, 6, 7]))
    print(n_row_pascal(4))
