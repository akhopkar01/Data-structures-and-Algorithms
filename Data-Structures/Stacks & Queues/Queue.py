import Node as ll

class Queue1:
    def __init__(self, initial_size=10):
        self.arr = [0 for _ in range(initial_size)]
        self.next_index = 0
        self.front_index = -1
        self.queue_size = 0

    def enqueue(self, value):
        # TODO: Check if the queue is full; if it is, call the _handle_queue_capacity_full method
        if self.next_index == len(self.arr):
            self._handle_full_capacity()
        # enqueue new element
        self.arr[self.next_index] = value
        self.queue_size += 1
        self.next_index = (self.next_index + 1) % len(self.arr)
        if self.front_index == -1:
            self.front_index = 0

    def dequeue(self):
        # check if queue is empty
        if self.is_empty():
            self.front_index = -1  # resetting pointers
            self.next_index = 0
            return None

        # dequeue front element
        value = self.arr[self.front_index]
        self.front_index = (self.front_index + 1) % len(self.arr)
        self.queue_size -= 1
        return value

    def size(self):
        return self.queue_size

    def is_empty(self):
        return self.size() == 0

    def front(self):
        # check if queue is empty
        if self.is_empty():
            return None
        return self.arr[self.front_index]

    # TODO: Add the _handle_queue_capacity_full method
    def _handle_full_capacity(self):
        old_arr = self.arr
        self.arr = [0 for _ in range(2 * len(old_arr))]

        idx = 0
        for i in range(self.front_index, len(old_arr)):
            self.arr[idx] = old_arr[i]
            idx += 1

        # In case of the queue utilizes the carried over circularly data in the queue
        for i in range(0, self.front_index):
            self.arr[idx] = old_arr[i]
            idx += 1

        self.front_index = 0
        self.next_index = idx

class Queue2:

    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    def enqueue(self, value):
        new_node = ll.Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node  # add data to the next attribute of the tail (i.e. the end of the queue)
            self.tail = self.tail.next  # shift the tail (i.e., the back of the queue)
        self.num_elements += 1

    # Add the dequeue method
    def dequeue(self):
        if self.is_empty():
            return None
        value = self.head.value
        self.head = self.head.next
        self.num_elements -= 1
        return value

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0


class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size() == 0:
            return None
        else:
            return self.items.pop()

    def is_empty(self):
        return self.size() == 0


class Queue3:
    def __init__(self):
        self.instorage = Stack()
        self.outstorage = Stack()

    def size(self):
        return self.outstorage.size() + self.instorage.size()

    def enqueue(self, item):
        self.instorage.push(item)

    def dequeue(self):
        if not self.outstorage.items:
            while self.instorage.items:
                self.outstorage.push(self.instorage.pop())
        return self.outstorage.pop()

    def is_empty(self):
        if self.size() == 0:
            return True
        return False


def reverse_queue(queue):
    stack = Stack()
    while not queue.is_empty():
        val = queue.dequeue()
        stack.push(val)
    while not stack.is_empty():
        queue.enqueue(stack.pop())
    return

def test_function(test_case):
    queue = Queue3()
    for num in test_case:
        queue.enqueue(num)

    reverse_queue(queue)
    index = len(test_case) - 1
    while not queue.is_empty():
        removed = queue.dequeue()
        if removed != test_case[index]:
            print("Fail")
            return
        else:
            index -= 1
    print("Pass")

if __name__ == "__main__":
    choice = input("1. Using arrays, 2. Using Linked Lists, 3. Using Stacks: ")
    if choice == "1":
        q = Queue1()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)

        # Test size
        print("Pass" if (q.size() == 3) else "Fail")

        # Test dequeue
        print("Pass" if (q.dequeue() == 1) else "Fail")

        # Test enqueue
        q.enqueue(4)
        print("Pass" if (q.dequeue() == 2) else "Fail")
        print("Pass" if (q.dequeue() == 3) else "Fail")
        print("Pass" if (q.dequeue() == 4) else "Fail")
        q.enqueue(5)
        print("Pass" if (q.size() == 1) else "Fail")



    if choice == "2":
        q = Queue2()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)

        # Test size
        print("Pass" if (q.size() == 3) else "Fail")

        # Test dequeue
        print("Pass" if (q.dequeue() == 1) else "Fail")

        # Test enqueue
        q.enqueue(4)
        print("Pass" if (q.dequeue() == 2) else "Fail")
        print("Pass" if (q.dequeue() == 3) else "Fail")
        print("Pass" if (q.dequeue() == 4) else "Fail")
        q.enqueue(5)
        print("Pass" if (q.size() == 1) else "Fail")

    if choice == "3":
        q = Queue3()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)

        # Test size
        print("Pass" if (q.size() == 3) else "Fail")

        # Test dequeue
        print("Pass" if (q.dequeue() == 1) else "Fail")

        # Test enqueue
        q.enqueue(4)
        print("Pass" if (q.dequeue() == 2) else "Fail")
        print("Pass" if (q.dequeue() == 3) else "Fail")
        print("Pass" if (q.dequeue() == 4) else "Fail")
        q.enqueue(5)
        print("Pass" if (q.size() == 1) else "Fail")

        test_case_1 = [1, 2, 3, 4]
        test_function(test_case_1)