class TrieNode:
    def __init__(self,val="",isEnd=False):
        self.val = val
        self.children = {}
        self.isEnd = isEnd
    
    def exist(self,val):
        if not val:
            return self.isEnd
        c = val[0]
        if c!="." and c not in self.children:
            return False
        
        if c == ".":
            for child in self.children.values():
                if child.exist(val[1:]):
                    return True
            return False
        else:
            if c not in self.children:
                return False
            return self.children[c].exist(val[1:])


class WordDictionary:
    def __init__(self):
        self.words = TrieNode()
        

    def addWord(self, word: str) -> None:
        n = len(word)
        parent = self.words.children
        for i in range(n):
            c = word[i]
            if c not in parent:
                parent[c] = TrieNode(c,i==n-1)
            parent = parent[c].children
        

    def search(self, word: str) -> bool:
        return self.words.exist(word)

