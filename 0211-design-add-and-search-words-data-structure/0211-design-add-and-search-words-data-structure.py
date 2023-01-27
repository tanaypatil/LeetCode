class WordDictionary:

    def __init__(self):
        self.children = {}
        self.isEnd = False
        

    def addWord(self, word: str) -> None:
        curr = self
        for w in word:
            if w not in curr.children:
                curr.children[w] = WordDictionary()
            curr = curr.children[w]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        curr = self
        if not word:
            return curr.isEnd
        for i, w in enumerate(word):
            if w == ".":
                for c in curr.children:
                    if curr.children[c].search(word[i+1:]):
                        return True
                return False
            elif w not in curr.children:
                return False
            curr = curr.children[w]
        return curr.isEnd


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)