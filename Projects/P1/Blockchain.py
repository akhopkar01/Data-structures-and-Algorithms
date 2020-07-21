import hashlib
import time

class Block(object):
    def __init__(self, data, previous_hash=None):
        self.timestamp = time.asctime(time.gmtime(time.time()))
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None

    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str =  self.data.encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()

    def __repr__(self):
        return "Timestamp: {} \n Hash: {} \n Data: {} \n Previous Hash: {}".format(self.timestamp, self.hash, self.data, self.previous_hash)


class Blockchain:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        if self.head is None:
            self.head = Block(data)
            self.tail = self.head

        else:
            self.tail.next = Block(data, self.tail.hash)
            self.tail = self.tail.next



    def search(self, data):
        """
        Returns block of the data to be searched
        :param data:
        :return:
        """

        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return "Not Found !"

    def size(self):
        current = self.head
        size = 0
        while current:
            current = current.next
            size+=1
        return size

    def __repr__(self):
        s = "______________________ \n"
        current = self.head
        while current:
            s+="{} \n ______________________ \n".format(current)
            current = current.next

        return s



if __name__ == "__main__":
    bchain1 = Blockchain()
    bchain2 = Blockchain()
    bchain3 = Blockchain()

    data1 = ["First", "Second"]
    data2 = ["US", "UK", "India", "Australia"]
    data3 = ['4500', '600', '23000', '780000', '12000', '3000']

    for element in data1:
        bchain1.append(element)

    for element in data2:
        bchain2.append(element)

    for element in data3:
        bchain3.append(element)

    print("Test case 1:")
    print(bchain1)
    print(bchain1.size()) #2
    print(bchain1.search("Second"))
    print(bchain1.search("third")) # Not Found !

    print("Test case 2:")
    print(bchain2)
    print(bchain2.size())  # 4
    print(bchain2.search("UK"))
    print(bchain2.search("Spain")) # Not Found!

    print("Test case 3:")
    print(bchain3)
    print(bchain3.size())  # 6
    print(bchain3.search('780000'))
    print(bchain3.search('1')) # Not found!

    edge =  Blockchain()
    edge.append('')
    print("Edge case:")
    print(edge)