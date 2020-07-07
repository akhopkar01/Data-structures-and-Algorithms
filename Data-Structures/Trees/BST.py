### Binary Search Tree
from Trees import *

class BST(Tree):
    def __init__(self, value=None):
        super().__init__(value)

    def set_root(self, value):
        self.root = Node(value)

    def compare(self, node, new_node):
        if new_node.get_value() == node.get_value():
            return 0
        elif new_node.get_value() < node.get_value():
            return -1
        else:
            return 1

    def insert(self, value):
        if self.root.value is None:
            self.set_root(value)

            return

        self._insert_recursively_(self.root, Node(value))

    def _insert_recursively_(self, node, new_node):
        flag = self.compare(node, new_node)
        if flag == 0:
            node = new_node

        elif flag == -1:
            if node.has_left_child():
                self._insert_recursively_(node.get_left_child(), new_node)
            else:
                node.set_left_child(new_node)

        else:
            if node.has_right_child():
                self._insert_recursively_(node.get_right_child(), new_node)
            else:
                node.set_right_child(new_node)

    def search(self,value):
        node = self.root
        snode = Node(value)
        while True:
            flag = self.compare(node, snode)
            if flag == 0:
                return True
            elif flag == -1:
                if node.has_left_child():
                    node = node.get_left_child()
                else:
                    return False
            else:
                if node.has_right_child():
                    node = node.get_right_child()
                else:
                    return False

    def minNode(self, node):
        current = node

        while current.get_left_child() is not None:
            current = current.get_left_child()

        return current

    def delete(self, value):
        if self.search(value) is False:
            raise ValueError

        try:
            self._delete_(self.root, Node(value))
        except ValueError:
            print("Invalid entry! Value not found")

    def _delete_(self, node, delete_node):
        if node.value is None:
            return node

        flag = self.compare(node, delete_node)
        if flag == -1:
            node_left = self._delete_(node.get_left_child(),delete_node)
            node.set_left_child(node_left)

        elif flag == 1:
            node_right = self._delete_(node.get_right_child(), delete_node)
            node.set_right_child(node_right)

        else:
            if node.has_left_child() is False:
                temp = node.get_right_child()
                node.set_value(None)
                return temp

            elif node.has_right_child() is False:
                temp = node.get_left_child()
                node.set_value(None)
                return temp

            temp = self.minNode(node.get_right_child())
            node.set_value(temp.value)
            node_right = self._delete_(node.get_right_child(), temp)
            node.set_right_child(node_right)
        return node




    def __repr__(self):
        level = 0
        q = Queue()
        visit_order = list()
        node = self.get_root()
        q.enq((node, level))
        while (len(q) > 0):
            node, level = q.deq()
            if node == None:
                visit_order.append(("<empty>", level))
                continue
            visit_order.append((node, level))
            if node.has_left_child():
                q.enq((node.get_left_child(), level + 1))
            else:
                q.enq((None, level + 1))

            if node.has_right_child():
                q.enq((node.get_right_child(), level + 1))
            else:
                q.enq((None, level + 1))

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


def create_BST():
    bst = BST()
    bst.insert(5)
    bst.insert(6)
    bst.insert(2)
    bst.insert(7)
    bst.insert(3)
    bst.insert(1)
    bst.insert(10)
    return bst


def arr_to_binary_tree(arr):
    idx = 0
    if len(arr) <= 0 or arr[0] == -1:
        return None

    root = Node(arr[idx])
    idx+=1
    q = Queue()
    q.enq(root)
    while q:
        current = q.deq()
        left_child = arr[idx]
        idx+=1

        if left_child is not None:
            left_node = Node(left_child)
            current.left = left_node
            q.enq(left_node)

        right_child = arr[idx]
        idx+=1

        if right_child is not None:
            right_node = Node(right_child)
            current.right = right_node
            q.enq(right_node)
    return root




if __name__=="__main__":
    bst = create_BST()
    print(bst)
    bst.delete(1)
    print(bst)
    bst.delete(10)
    print(bst)
    bst.delete(2)
    print(bst)
    bst.delete(10)