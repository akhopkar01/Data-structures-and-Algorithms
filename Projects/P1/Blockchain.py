import hashlib
import time

class Block(object):
    def __init__(self, data, previous_hash=None, prev_block = None):
        self.timestamp = time.asctime(time.gmtime(time.time()))
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.prev_block = prev_block

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
            self.tail = Block(data, self.tail.hash, self.tail)



    def search(self, data):
        """
        Returns block of the data to be searched
        :param data:
        :return:
        """

        current = self.tail
        while current:
            if current.data == data:
                return current
            current = current.prev_block
        return "Not Found !"

    def size(self):
        current = self.tail
        size = 0
        while current:
            current = current.prev_block
            size+=1
        return size

    def __repr__(self):
        s = "______________________ \n"
        current = self.tail
        while current:
            s+="{} \n ______________________ \n".format(current)
            current = current.prev_block

        return s



if __name__ == "__main__":
    bchain = Blockchain()

    bchain.append("First Block")

    bchain.append("Second Block")

    bchain.append("Third Block")

    print(bchain)
    print(bchain.size())
    #
    block = bchain.search("Second Block")
    print(block)
