class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def to_list(self):
        out = []
        current = self.head
        while current:
            out.append(current.value)
            current = current.next
        return out

def union(llist1, llist2):
    list1 = llist1.to_list()
    list2 = llist2.to_list()

    if len(list1) == 0 and len(list2) == 0:
        return None

    union_list = list(set(list1+list2))

    ulist = LinkedList()
    for num in union_list:
        ulist.append(num)

    return ulist

def intersection(llist1, llist2):
    set1 = set(llist1.to_list())
    set2 = set(llist2.to_list())

    intersect_list =[num for num in set1 if num in set2]

    if len(intersect_list) == 0:
        return None

    intersection_llist = LinkedList()
    for num in intersect_list:
        intersection_llist.append(num)

    return intersection_llist

if __name__ == "__main__":

    ## test 1
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print(union(linked_list_1, linked_list_2)) #32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 ->
    print(intersection(linked_list_1, linked_list_2)) #4 -> 6 -> 21 ->

    ## test 2
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
    element_2 = [1, 7, 8, 9, 11, 21, 1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print(union(linked_list_3, linked_list_4)) #65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 ->
    print(intersection(linked_list_3, linked_list_4)) #None

    ## test 3
    linked_list_5 = LinkedList()
    linked_list_6 = LinkedList()

    print(union(linked_list_5, linked_list_6)) # None
    print(intersection(linked_list_5, linked_list_6)) # None

    ## test 4
    linked_list_7 = LinkedList()
    linked_list_8 = LinkedList()

    element_1 = [4, 6, 7, 8, 9 , 10, 2, 31]

    for num in element_1:
        linked_list_7.append(num)

    print(union(linked_list_7, linked_list_8)) # 2 -> 4 -> 6 -> 7 -> 8 -> 9 -> 10 -> 31 ->
    print(intersection(linked_list_7, linked_list_8)) # None