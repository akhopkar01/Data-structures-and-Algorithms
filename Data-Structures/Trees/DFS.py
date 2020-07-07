from Trees import *

class With_Stacks:
    def __init__(self, tree):
        self.tree = tree

    def pre_order(self, debug_mode = False):
        tree = self.tree
        node = tree.get_root()
        visit_order = []
        state = State(node)
        stack = Stack()
        stack.push(state)
        count = 0
        visit_order.append(node.get_value())
        while (node):
            if debug_mode:
                print("""
            loop count: {}
            current node: {}
            stack:
            {}
                        """.format(count, node, stack))
            count += 1
            if node.has_left_child() and not state.get_visited_left():
                state.set_visited_left()
                node = node.get_left_child()
                visit_order.append(node.get_value())
                state = State(node)
                stack.push(state)

            elif node.has_right_child() and not state.get_visited_right():
                state.set_visited_right()
                node = node.get_right_child()
                visit_order.append(node.get_value())
                state = State(node)

            else:
                stack.pop()
                if not stack.is_empty():
                    state = stack.top()
                    node = state.get_node()
                else:
                    node = None

        if debug_mode:
            print("""
        loop count: {}
        current node: {}
        stack:
        {}
                    """.format(count, node, stack))
        return visit_order

    def in_order(self, debug_mode = False):
        tree = self.tree
        node = tree.get_root()
        visit_order = []
        state = State(node)
        stack = Stack()
        stack.push(state)
        count = 0
        # visit_order.append(node.get_value())
        while (node):
            if debug_mode:
                print("""
                    loop count: {}
                    current node: {}
                    stack:
                    {}
                                """.format(count, node, stack))
            count += 1
            if node.has_left_child() and not state.get_visited_left():
                state.set_visited_left()
                node = node.get_left_child()
                state = State(node)
                stack.push(state)

            elif node.has_right_child() and not state.get_visited_right():
                state.set_visited_right()
                node = node.get_right_child()
                # visit_order.append(node.get_value())
                state = State(node)
            # elif stack:
            #     state = stack.pop()
            #     node = state.get_node()
            #
            #     node = node.get_right_child()


            else:
                stack.pop()
                if not stack.is_empty():
                    state = stack.top()
                    node = state.get_node()
                    visit_order.append(node.get_value())
                else:
                    node = None
                # break

        if debug_mode:
            print("""
                loop count: {}
                current node: {}
                stack:
                {}
                            """.format(count, node, stack))
        return visit_order


class With_Recursion(object):
    def __init__(self, tree):
        self.tree = tree

    def pre_order(self):
        root = self.tree.get_root()
        visit_order = []

        def traverse(node):
            if node:
                visit_order.append(node)

                traverse(node.get_left_child())

                traverse(node.get_right_child())
        traverse(root)
        return visit_order

    def in_order(self):
        root = self.tree.get_root()
        visit_order = []

        def traverse(node):
            if node:
                traverse(node.get_left_child())

                visit_order.append(node)

                traverse(node.get_right_child())
        traverse(root)
        return visit_order

    def post_order(self):
        root = self.tree.get_root()
        visit_order = []

        def traverse(node):
            if node:
                traverse(node.get_left_child())

                traverse(node.get_right_child())

                visit_order.append(node)

        traverse(root)
        return visit_order


def create_tree():
    tree = Tree("apple")
    tree.get_root().set_left_child(Node("banana"))
    tree.get_root().set_right_child(Node("cherry"))
    tree.get_root().get_left_child().set_left_child(Node("dates"))
    return tree

if __name__ == "__main__":
    tree = create_tree()
    dfs = With_Stacks(tree)
    print(dfs.pre_order())
    print(dfs.in_order(debug_mode=True))