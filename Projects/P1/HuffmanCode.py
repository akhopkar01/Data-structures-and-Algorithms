import collections
import sys

class Node:
    def __init__(self, element=None, priority=None):
        """
        Creating a node class containing the character information - frequency, left and right child and binary code
        :param element: character
        :param priority: frequency of the character
        """
        self.element = element
        self.freq = priority
        self.left = None
        self.right = None
        self.bin = None

    def __repr__(self):
        return "Node[{}|{}|{}]".format(self.element, self.freq, self.bin)

class SimplePriorityQueue:
    def __init__(self, string):
        """
        Creating a simple priority queue for the string character
        :param string: input str message
        """
        self.priority = []

        # Creating the queue based on the characters and their number of occurrences (frequency).
        counts = {}
        for char in string:
            if char in counts:
                counts[char]+=1
            else:
                counts[char]=1

        for char in counts:
            frequency = counts[char]
            self.priority.append(Node(char, frequency))
        self.sort()

    def sort(self):
        # Sorting the queue based on their frequencies
        self.priority = sorted(self.priority, key= lambda x: x.freq, reverse=True)

    def pop(self):
        return self.priority.pop()

    def _insert_(self, node):
        #Internal function to insert the node and sort the queue
        self.priority.append(node)
        self.sort()

    def merge(self):
        """
        Get the two lowest frequency nodes and add them to the priority queue
        :return: merged priority
        """
        new_node = Node()
        node1 = self.pop()
        node2 = self.pop()

        new_frequency = node1.freq + node2.freq
        new_node.left = node1 if min(node1.freq, node2.freq) == node1.freq else node2
        new_node.right = node1 if max(node1.freq, node2.freq) == node1.freq else node2
        new_node.freq = new_frequency
        self._insert_(new_node)

class BinaryTree:
    def __init__(self, string):
        """
        Binary Tree class to initialize a root and create a binary tree
        :param string: str -> msg
        """
        q = SimplePriorityQueue(string)
        # Merge till the queue length is 1
        while len(q.priority) > 1:
            q.merge()
        self.root = q.priority[0]

    def create_Btree(self):
        node = self.root
        self.root = self._binarize_(node)
        self.root.bin = 0

    def _binarize_(self, node):
        # Binarizing the nodes - setting node.bin 0/1
        if node.left is None and node.right is None:
            return node

        if node.left:
            node.left.bin=1
            node.left = self._binarize_(node.left)

        if node.right:
            node.right.bin = 0
            node.right = self._binarize_(node.right)

        return node

    def __repr__(self):
        self.create_Btree()
        level = 0
        q = []
        visit_order = list()
        node = self.root
        q.append((node, level))
        while len(q) > 0:
            node, level = q.pop(0)
            if node is None:
                visit_order.append(("<empty>", level))
                continue
            visit_order.append((node, level))
            if node.left:
                q.append((node.left, level + 1))
            else:
                q.append((None, level + 1))

            if node.right:
                q.append((node.right, level + 1))
            else:
                q.append((None, level + 1))

        s = "Tree\n"
        previous_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                s += " | " + str(node)
            else:
                s += "\n" + str(node)
                previous_level = level

        return s


class Huffman:
    def __init__(self, string):
        """
        Huffman Code class to create encoder and decoder
        :param string: str -> msg
        """
        tree = BinaryTree(string)
        tree.create_Btree()
        self.root = tree.root
        self.encode_dict = {}
        self.decode_dict = {}
        self.table = self._encoding_table_()
        self.msg = string

    def encode(self):
        # Based on the encoding table, update the encoding dictionary
        code = ''
        for elements in self.table:
            self.encode_dict[elements[0]] = elements[1]

        # Iterate through the dictionary, to fetch the code corresponding to the characters
        for char in self.msg:
            code+=str(self.encode_dict[char])
        return code



    def _encoding_table_(self):
        # Perform DFS recursively
        root = self.root
        base_code = ''
        visit_order = []

        def traverse(base_code, node):
            if node:
                if node.freq == -1:
                    current_code = ''
                else:
                    current_code = base_code+str(node.bin)

                if node.element:
                    visit_order.append( (node.element, current_code, node.freq) )
                if node.left:
                    traverse(current_code, node.left)
                if node.right:
                    traverse(current_code, node.right)
        traverse(base_code, root)
        return visit_order



if __name__ == "__main__":

    string1 = "AAAAAABBBBBCCCCDDDEE"
    string2 = "the bird is the word"

    huff1 = Huffman(string1)
    order = huff1._encoding_table_()
    print(order)

    code = huff1.encode()
    print(code)

    huff2 = Huffman(string2)
    order2 = huff2._encoding_table_()
    print(order2)

    code2 = huff2.encode()
    print(code2)