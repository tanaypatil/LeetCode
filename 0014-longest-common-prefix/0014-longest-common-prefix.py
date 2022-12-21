class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        
    def insert(self, string):
        curr = self
        for c in string:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEnd = True
        
    def findPrefix(self):
        curr = self
        res = ""
        while len(curr.children) == 1:
            if curr.isEnd:
                break
            k = list(curr.children.keys())[0]
            res += k
            curr = curr.children[k]
        return res


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = TrieNode()
        for s in strs:
            trie.insert(s)
        return trie.findPrefix()