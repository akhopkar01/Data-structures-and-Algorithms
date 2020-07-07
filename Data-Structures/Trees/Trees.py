from collections import deque


class Node(object):

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_left_child(self, left):
        self.left = left

    def set_right_child(self, right):
        self.right = right

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None

    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return "Node({})".format(self.get_value())

    def __str__(self):
        return "Node({})".format(self.get_value())


class Tree():
    def __init__(self, value=None):
        self.root = Node(value)

    def get_root(self):
        return self.root


class Stack():
    def __init__(self):
        self.list = list()

    def push(self, value):
        self.list.append(value)

    def pop(self):
        return self.list.pop()

    def top(self):
        if len(self.list) > 0:
            return self.list[-1]
        else:
            return None

    def is_empty(self):
        return len(self.list) == 0

    def __repr__(self):
        if len(self.list) > 0:
            s = "<top of stack>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in self.list[::-1]])
            s += "\n_________________\n<bottom of stack>"
            return s

        else:
            return "<stack is empty>"


class State(object):
    def __init__(self, node):
        self.node = node
        self.visited_left = False
        self.visited_right = False

    def get_node(self):
        return self.node

    def get_visited_left(self):
        return self.visited_left

    def get_visited_right(self):
        return self.visited_right

    def set_visited_left(self):
        self.visited_left = True

    def set_visited_right(self):
        self.visited_right = True

    def __repr__(self):
        s = """{}
    visited_left: {}
    visited_right: {}
        """.format(self.node, self.visited_left, self.visited_right)
        return s

class Queue:
    def __init__(self):
        self.queue = list()

    def enq(self, value):
        self.queue.append(value)

    def deq(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        else:
            return None

    def __len__(self):
        return len(self.queue)

    def __repr__(self):
        if len(self.queue) > 0:
            s = "<enqueue here>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in self.queue])
            s += "\n_________________\n<dequeue here>"
            return s
        else:
            return "<queue is empty>"

# class Queue():
#     def __init__(self):
#         self.q = deque()
#
#     def enq(self, value):
#         self.q.appendleft(value)
#
#     def deq(self):
#         if len(self.q) > 0:
#             return self.q.pop()
#         else:
#             return None
#
#     def __len__(self):
#         return len(self.q)
#
#     def __repr__(self):
#         if len(self.q) > 0:
#             s = "<enqueue here>\n_________________\n"
#             s += "\n_________________\n".join([str(item) for item in self.q])
#             s += "\n_________________\n<dequeue here>"
#             return s
#         else:
#             return "<queue is empty>"
