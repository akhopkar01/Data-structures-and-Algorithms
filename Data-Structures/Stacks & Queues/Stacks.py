# Two implementations: 1. Using Arrays, 2. Using Linked Lists

class Stack1:

    def __init__(self, initial_size=10):
        self.arr = [0 for _ in range(initial_size)]
        self.next_index = 0
        self.num_elements = 0

    def push(self, data):
        """
        Pushing the data in the stack
        :param data: value
        :return:
        """
        if self.next_index == len(self.arr):
            print("Out of space! Increasing array capacity ...")
            self._handle_stack_capacity_full()

        self.arr[self.next_index] = data
        self.next_index += 1
        self.num_elements += 1

    # TODO: Add the pop method
    def pop(self):
        """
        Pop the last element out LIFO
        :return: last element
        """
        if self.is_empty():
            return None
        self.next_index -= 1
        self.num_elements -= 1
        return self.arr[self.next_index]

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

    def _handle_stack_capacity_full(self):
        """
        Handles when the array is at full capacity
        """
        old_arr = self.arr
        self.arr = [0 for _ in range(2 * len(old_arr))]
        for index, value in enumerate(old_arr):
            self.arr[index] = value
        return

## Implementation using a Linked List
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack2:
    def __init__(self):
        self.head = None
        self.num_elements = 0

    def push(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.num_elements+=1

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements==0

    def pop(self):
        if self.is_empty():
            return None
        val = self.head.value
        self.head = self.head.next
        self.num_elements-=1
        return val

    def top(self):
        if self.head is None:
            return None
        return self.head.value

    def return_stack(self):
        PyList =[]
        if self.head is None:
            return None
        else:
            node = self.head
            while node:
                PyList.append(node.value)
                node = node.next
            return PyList[::-1]


def minimum_bracket_reversal(input_string):
    stack = Stack2()
    for char in input_string:
        if stack.is_empty():
            stack.push(char)
        elif char != stack.top() and stack.top() == '{': # Check if the first bracket is the open bracket or closed \
                                                  # and check if the current bracket is different than the top, if so: pop
                    stack.pop()
        else:
            stack.push(char)

    bracks = []
    count = 0
    while not stack.is_empty():
        first = stack.pop()
        second = stack.pop()
        bracks.append(first)
        bracks.append(second)
        if first == '{' and second == '{':
            count+=1
        elif first == '{' and second == '}':
            count+=2
        elif first == '}' and second == '}':
            count+=1
    return count



def postfix(input_list):
    """
    For a given input length with post-fixed operators for eg. instead of (3+1)*4
    It is, 3 1 + 4 *, We have to get the operations right to produce the right result
    :param input_list: List of operands
    :return: Result
    """

    stack = Stack2()
    for char in input_list:
        if char == "*":
            second = stack.pop()
            first = stack.pop()
            out = first * second
            stack.push(out)

        elif char == "+":
            second = stack.pop()
            first = stack.pop()
            out = first+second
            stack.push(out)

        elif char == "/":
            second = stack.pop()
            first = stack.pop()
            out = int(first/second)
            stack.push(out)

        elif char == "-":
            second = stack.pop()
            first = stack.pop()
            out = first-second
            stack.push(out)

        else:
            stack.push(int(char))
    return int(stack.pop())


if __name__ == "__main__":
    choice = input("1. Array Implementation 2. Linked List Implementation: ")
    if choice == "1":
        lifo = Stack1()
        lifo.push(1)
        lifo.push(5)
        lifo.push("Sex")
        lifo.push(17)
        print("{}, Pop: {}, Stack size: {}, New Stack {}".format(lifo.arr, lifo.pop(),
                                                                 lifo.size(), lifo.arr))
    elif choice == "2":
        lifo = Stack2()
        lifo.push(1)
        lifo.push(5)
        lifo.push("Sex")
        lifo.push(17)
        print("{}, Pop: {}, Stack size: {}, New Stack: {}, Stack Top: {}, Stack Size: {}".format(lifo.return_stack(),lifo.pop(),
                                                                                 lifo.size(), lifo.return_stack(),

                                                                                 lifo.top(), lifo.size()))
        print("Test1")
        test1 = "{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}"
        # print(len(test1))
        print(minimum_bracket_reversal(test1))

        print("Test2")
        test2 = "}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{"
        print(minimum_bracket_reversal(test2))

