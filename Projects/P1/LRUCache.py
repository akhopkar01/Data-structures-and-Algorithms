
class Node:
    def __init__(self, data=None):
        # self.key = key
        self.val = data
        self.next = None

    def __repr__(self):
        return "Node {}".format(self.val)

    def __str__(self):
        return "Node {}".format(self.val)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    def add(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head

        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        self.num_elements+=1

    def is_empty(self):
        return self.num_elements == 0

    def size(self):
        return self.num_elements


    def get_to_top(self, key):
        if self.tail.val == key:
            return
        if self.head.val == key:
            node = self.head.next
            self.tail.next = self.head
            self.head = node
            self.tail = self.tail.next
            self.tail.next = None
            return

        previous, current_node = self._search_(key)
        if current_node:
            next_node = current_node.next
            previous.next = next_node
            current_node.next = None
            self.tail.next = current_node
            self.tail = self.tail.next
            return

    def pop(self):
        val = self.head.val
        node = self.head
        self.head = node.next
        return val

    def _search_(self, key):

        node = self.head
        while node:
            if node.val == key:
                break
            prev_node = node
            node = node.next
        return prev_node, node


    def __repr__(self):
        node = self.head
        if node is not None:
            s = "<head>"
            while node:
                s += "\n______________{}____________\n".format(node)
                node = node.next
            s += "<tail> \n"
            s += "Size: {}".format(self.size())
            return s
        else:
            return "<Empty List>"



class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = dict()
        self.LRU = LinkedList()
        self.num_elements = 0

    def get(self, key):
        if key in self.cache:
            self.LRU.get_to_top(key)
            return self.cache[key]
        else:
            return -1


    def cache_size(self):
        return self.num_elements

    def _adjust_(self):
        LRkey = self.LRU.pop()
        del self.cache[LRkey]

    def set(self, key, value):
        if self.capacity < 1:

            return

        if self.cache_size() >= self.capacity:
            self._adjust_()
            self.cache[key] = value
            self.LRU.add(key)
        else:
            self.cache[key] = value
            self.LRU.add(key)
        self.num_elements+=1

    def __repr__(self):
        if self.cache_size() > 0:
            s = "<top> \n"
            for key in self.cache:
                s += "\n _________{}:{}_________ \n".format(key, self.cache[key])
            s += "\n <end>"
            return s
        else:
            return '<Empty Cache>'

if __name__ == "__main__":
    cache = LRUCache(5)
    cache.set(1,1)
    cache.set(2,2)
    cache.set(3,3)
    cache.set(4,4)

    print(cache.get(1)) #1
    print(cache.get(2)) #2
    print(cache.get(9)) #-1

    cache.set(5, 5)
    cache.set(5,5)

    print(cache.get(3)) #-1
    print(cache.get(4)) # 4

    cache.set(6, 6)

    print(cache.get(1)) # -1

    cache2 = LRUCache(0)
    cache2.set(1,1)
    cache2.set(2,2)
    cache2.set(3,3)


    print(cache2.get(1)) #-1
    print(cache2.get(2)) #-1

    cache3 = LRUCache(-1)
    cache3.set(0, 0)
    cache3.set(1, 3)

    print(cache3.get(0)) #-1
