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

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def create_linked_list(arr):
    if len(arr) == 0:
        return None

    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
    return head

def display(head):
    node = head
    while node:
        print(node.value)
        node = node.next
    return

# head = create_linked_list([1,2,4,3,5,6])
# display(head)


def even_odd(head):
    #Makes the even values of the linked list occur after all the odd values of the ll

    current_node = head

    even_head = None
    even_tail = None

    odd_head = None
    odd_tail = None

    while current_node:
        next_node = current_node.next
        if current_node.value %2 == 0:
            if even_head is None:
                even_head = current_node
                even_tail = even_head
            else:
                even_tail.next = current_node
                even_tail = even_tail.next
        else:
            if odd_head is None:
                odd_head = current_node
                odd_tail = odd_head
            else:
                odd_tail.next = current_node
                odd_tail = odd_tail.next
        current_node.next = None
        current_node = next_node

    if odd_head is None:
        return even_head

    odd_tail.next = even_head
    return odd_head


def skip(head, i, j):

    # Skip i elements and delete j elements
    # For eg. ll = [1,2,3,4,5,6,7,8,9,10] ; i= 2, j =3
    # New list = [1,2,6,7]

    current = head

    previous = None

    while current:

        for _ in range(i-1):
            if current is None:
                return head
            current = current.next
        previous = current
        current = current.next

        for _ in range(j):
            if current is None:
                break
            current = current.next

        previous.next = current
    return head


# new = skip(head, 2, 3)
# display(new)


def swap_nodes(head, left_index, right_index):
    # Swap the nodes from left index to right index
    if right_index<left_index:
        return None

    if left_index==right_index:
        return head

    current = head

    first_current = None
    first_previous = None

    second_current = None
    second_previous = None

    new_head = None
    idx = 0
    while current:
        if idx == left_index:
            first_current = current

        elif idx == right_index:
            second_current = current
            break

        if first_current is None:
            first_previous = current

        second_previous = current
        current = current.next
        idx+=1

    temp = first_current.next
    second_previous.next = first_current
    first_current.next = second_current.next
    second_current.next = temp
    # first_previous.next = second_current

    if first_previous is None:
        new_head = second_current
    else:
        first_previous.next = second_current
        new_head = head

    return new_head

if __name__ == "__main__":
    head = create_linked_list([1,2,3,4,5,6,7,8,9,10,11,12])
    # arr = [3, 4, 5, 2, 6, 1, 9]
    # head = create_linked_list(arr)
    left_index = 3
    right_index = 4
    swapped = swap_nodes(head, left_index, right_index)
    display(swapped)

    # print(add_one_1([9, 9, 9]))
    # print(add_one_2([9, 9, 9]))
    # print(duplicate_number1([0, 2, 3, 1, 4, 5, 3]))
    # print(duplicate_number2([0, 2, 3, 1, 4, 5, 3]))
    # print(max_sum_subarray([1,-2, 3, 4, -5, 6, 7]))
    # print(n_row_pascal(4))
