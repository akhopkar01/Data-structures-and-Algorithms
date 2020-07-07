from Trees import *

def bfs_tree(tree):
    root = tree.get_root()
    visit_order = []
    q = Queue()
    q.enq(root)
    while q:
        node = q.deq()
        if node is None:
             break

        visit_order.append(node)

        if node.has_left_child():
            q.enq(node.get_left_child())

        if node.has_right_child():
            q.enq(node.get_right_child())

    return visit_order

def get_tree():
    tree = Tree("apple")
    tree.get_root().set_left_child(Node("banana"))
    tree.get_root().set_right_child(Node("cherry"))
    tree.get_root().get_left_child().set_left_child(Node("dates"))
    return tree

def check_queue(arr):
    q = Queue()
    for num in arr:
        q.enq(num)
        print(q)
    x = q.deq()
    print(q)

def __repr__(self):
    node = self.root
    q = Queue()
    visit_order = []
    level = 0
    q.enq( (node, level) )
    while len(q)>0:
        node, level = q.deq()

        if node is None:
            visit_order.append( ('<empty>', level) )
            continue

        visit_order.append( (node, level) )

        if node.has_left_child():
            q.enq( (node.get_left_child(), level+1) )

        if node.has_right_child():
            q.enq( (node.get_right_child(), level+1) )
    s = "Trees \n"
    prev_level = -1
    for i in range(len(visit_order)):
        node, level = visit_order[i]
        if level == prev_level:
            s+=" | " + str(node)
        else:
            s+="\n" + str(node)
            prev_level = level
    return s

Tree.__repr__ = __repr__


if __name__=="__main__":
    tree = get_tree()
    order =bfs_tree(tree)
    print(order)
    # check_queue([1, 3, 5, 6, 8])
    print(tree)