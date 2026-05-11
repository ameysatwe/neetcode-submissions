class Node:
    def __init__(self):
        self.children = [None] * 26
        self.eof = False
class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            i = ord(c) - ord("a")
            if curr.children[i] == None:
                curr.children[i] = Node()
            curr = curr.children[i]
        curr.eof = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            i = ord(c) - ord('a')
            if curr.children[i] == None:
                return False
            curr = curr.children[i]
        
        return curr.eof

    def startsWith(self, prefix: str) -> bool:

        curr = self.root
        for c in prefix:
            i = ord(c)-ord('a')
            if curr.children[i] == None:
                return False
            curr = curr.children[i]
        
        return True
        
        