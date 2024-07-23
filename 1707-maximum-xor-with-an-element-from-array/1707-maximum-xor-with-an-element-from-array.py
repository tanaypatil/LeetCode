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
        if not curr or not curr.child:
            return -1
        for i in range(31, -1, -1):
            v = (number >> i) & 1
            if 1-v in curr.child:
                curr = curr.child[1-v]
                ans |= 1<<i
            elif v in curr.child:
                curr = curr.child[v]
        return ans


class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        queries = sorted(enumerate(queries), key=lambda x: x[1][1])
        
        i = 0
        trie = TrieNode()
        ans = [-1]*len(queries)
        for j, (x, m) in queries:
            while i < len(nums) and nums[i] <= m:
                trie.insert(nums[i])
                i += 1
            ans[j] = trie.findMax(x)
        return ans
        