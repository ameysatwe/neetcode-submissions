class Node:
    def __init__(self):
        self.children = {}
        self.eof = False
class WordDictionary:

    def __init__(self):
        self.root = Node()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.eof = True

    def search(self, word: str) -> bool:
        def rec(j,root):
            curr = root

            for i in range(j,len(word)):
                c = word[i]

                if c == ".":
                    for child in curr.children.values():
                        if rec(i+1,child):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            return curr.eof
        
        return rec(0,self.root)
