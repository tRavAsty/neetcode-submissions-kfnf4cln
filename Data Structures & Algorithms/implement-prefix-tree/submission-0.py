class PrefixTree:

    def __init__(self):
        self.children = {}
        self.isEnd = False
        

    def insert(self, word: str) -> None:
        if word == "":
            self.isEnd = True
            return
        beginner = word[0]
        if beginner not in self.children:
            self.children[beginner] = PrefixTree()
        
        self.children[beginner].insert(word[1:])


    def search(self, word: str) -> bool:
        if word == "":
            return self.isEnd
        beginner = word[0]
        if beginner not in self.children:
            return False
        
        return self.children[beginner].search(word[1:])
        

    def startsWith(self, prefix: str) -> bool:
        if prefix == "":
            return True
        beginner = prefix[0]
        if beginner not in self.children:
            return False
        
        return self.children[beginner].startsWith(prefix[1:])        
        
        