class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """
    Class to create a linked list and perform some basic operations such as:
    append, display, prepend, convert, insert, remove, search, pop
    """
    def __init__(self, value=None):
        self.head = value

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next is not None:
            node = node.next

        node.next = Node(value)
        return

    def display(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next

    def convert_list(self):
        Pylist = []
        node = self.head
        while node:
            Pylist.append(node.value)
            node = node.next
        return Pylist

def prepand(self, value):
    new_node = Node(value)
    new_node.next = self.head
    self.head = new_node

def search(self, value):
    node = self.head
    while node:
        if node.value == value:
            return node
        node = node.next
    return None

def remove(self, value):
    node = self.head

    #If head contains the value, change the head
    if node is not None:
        if node.value == value:
            self.head = node.next
            node = None
            return
    # Keep track of the previous node of the node that contains the value
    while node:
        if node.value == value:
            break
        prev_node = node
        node = node.next
    if node == None:
        return

    #Link the previous node to the next node
    prev_node.next = node.next
    node = None

def pop(self):
    node = self.head
    value = node.value
    self.head = node.next
    # node = None
    return value

def insert(self, value, pos):
    node = self.head
    new_node = Node(value)

    idx = 0
    prev_node = None
    while node:
        if idx == pos:
            break
        prev_node = node
        node = node.next
        idx+=1

    if prev_node == None:
        new_node.next = self.head
        self.head = new_node
        return
    new_node.next = prev_node.next
    prev_node.next = new_node
    return

LinkedList.insert = insert
LinkedList.prepand = prepand
LinkedList.pop = pop
LinkedList.remove = remove
LinkedList.search = search

def create_linked_list(_list_):
    """
    The function converts a python list/array into a linked list; Time complexity: O(n)
    :param _list_: a Python list
    :return: A linked list
    """
    head = None
    tail = None

    for val in _list_:
        if head is None:
            head = Node(val)
            tail = head

        else:
            tail.next = Node(val)
            tail = tail.next
    return head

def reverse(linked_list):
    """
    Reverse a linked list
    :param linked_list: linked_list
    :return: reversed linked list
    """

    new_list = LinkedList
    prev_node = None
    for value in linked_list:
        new_node = Node(value)
        new_node.next = prev_node
        prev_node = new_node

    new_list.head = prev_node
    return new_list


def isCircular(linked_list):
    """
    Checks if a linked list is circular i.e., has loops
    :param linked_list: Linked list
    :return: True/False
    """
    if linked_list.head is None:
        return False

    fast = linked_list.head
    slow = linked_list.head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False


if __name__ == "__main__":
    llist = LinkedList()
    llist.append(2)
    llist.append(-1)
    llist.append(10)
    llist.append(1)

    _list_ = llist.convert_list()

    print("Linked List: ")
    llist.display()

    print("Python List: ", _list_)

    llist.prepand(8)
    print("Prepanded Linked List")
    llist.display()

    node = llist.search(-1)
    print("Value searched: ", node.value, " Next Node: ", node.next.value)
    rm = 10

    llist.remove(rm)
    print("Linked List after removal {}: ".format(rm))
    llist.display()

    Pop = llist.pop()
    print("Element Popped: {}, Value of the head now: {}, linked list after popping element: ".format(Pop, llist.head.value))
    llist.display()

    print("Insertion: ")
    llist.insert(3, 2)
    llist.display()

    reverse_list = reverse(llist)
    reverse_list.display()