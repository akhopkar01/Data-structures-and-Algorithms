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
    bchain = Blockchain()

    bchain.append("First Block")

    bchain.append("Second Block")

    bchain.append("Third Block")

    print(bchain)
    print(bchain.size()) #3
    block = bchain.search("Second Block")
    print(block) #block 2
