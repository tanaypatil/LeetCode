class TrieNode:
    def __init__(self):
        self.child = {}
        
    def insert(self, number):
        curr = self
        for i in range(31, -1, -1):
            v = (number >> i) & 1
            if v not in curr.child:
                curr.child[v] = TrieNode()
            curr = curr.child[v]
    
    def findMax(self, number):
        curr = self
        ans = 0
        for i in range(31, -1, -1):
            v = (number >> i) & 1
            if 1-v in curr.child:
                curr = curr.child[1-v]
                ans |= 1<<i
            else:
                curr = curr.child[v]
        return ans


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = TrieNode()
        for num in nums:
            trie.insert(num)
        
        m = 0
        for num in nums:
            m = max(m, trie.findMax(num))
        return m