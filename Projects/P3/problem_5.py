from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact

class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = {}

    def insert(self, char):
        ## Add a child node in this Trie
        if char not in self.children:
            self.children[char] = TrieNode()
        else:
            pass

    def suffixes(self, suffix=''):
        ## Recursive function that collects the suffix for
        ## all complete words below this point
        output = []
        if self.is_word and suffix is not '':
            output.append(suffix)

        if len(self.children) == 0:
            return output

        for char in self.children:
            result = self.children[char].suffixes(suffix + char)
            if result:
                output.append(result[0])
        return output

    def __repr__(self):
        return "Children: {}, Word Status: {}".format(self.children, self.is_word)


class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        current = self.root
        for char in word:
            current.insert(char)
            current = current.children[char]
        current.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        current = self.root

        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]

        return current

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')

interact(f,prefix='');





