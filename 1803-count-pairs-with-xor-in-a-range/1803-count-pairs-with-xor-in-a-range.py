class Node:
    def __init__(self):
        self.children = {}
        self.count = 0
        
    def insert(self, num):
        curr = self
        for i in range(15, -1, -1):
            bit = (num >> i) & 1
            if bit not in curr.children:
                curr.children[bit] = Node()
            curr = curr.children[bit]
            curr.count += 1
    
    def limit_xor(self, num, limit):
        curr = self
        res = 0
        for i in range(15, -1, -1):
            if not curr:
                break
            bit = (num >> i) & 1
            l = (limit >> i) & 1
            if l:
                res += curr.children.get(bit, Node()).count
                curr = curr.children.get(1^bit, None)
            else:
                curr = curr.children.get(bit, None)
        return res
    


class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        trie = Node()
        ans = 0
        for num in nums:
            ans += trie.limit_xor(num, high+1) - trie.limit_xor(num, low)
            trie.insert(num)
        return ans