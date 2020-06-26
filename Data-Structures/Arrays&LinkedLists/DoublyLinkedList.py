class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self, value=None):
        self.head = value
        self.tail = None

    def append(self, val):

        if self.head is None:
            self.head = DoubleNode(val)
            self.tail = self.head
            return

        node = self.tail
        node.next = DoubleNode(val)
        node.next.prev = node
        self.tail = self.tail.next
        return

if __name__ == "__main__":
    linked_list = DoubleLinkedList()
    linked_list.append(1)
    linked_list.append(-2)
    linked_list.append(4)

    print("Going forward through the list, should print 1, -2, 4")
    node = linked_list.head
    while node:
        print(node.value)
        node = node.next

    print("\nGoing backward through the list, should print 4, -2, 1")
    node = linked_list.tail
    while node:
        print(node.value)
        node = node.prev