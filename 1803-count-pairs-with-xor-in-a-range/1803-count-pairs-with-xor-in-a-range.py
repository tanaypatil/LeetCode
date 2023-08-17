class Node(object):
    def __init__(self):
        self.children = {}  # child of node
        self.cnt = 0        # cnt the nums having this bit

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, val):
        curr = self.root
        for i in range(31, -1, -1):
            bit = bool(val & (1<<i)) # or (val>>i) & 1
            if bit not in curr.children:
                curr.children[bit] = Node()   # if no node of bit make node of bit
            curr = curr.children[bit]     # go to bit node
            curr.cnt += 1   # increment the cnt of node

    def cntSmallXorQuery(self, val,high):  # cnt the nums having xor with val < high
        res = 0
        curr = self.root
        for i in range(31, -1, -1):
            if not curr :
                break
            bit = (val>>i) & 1
            cmp = (high>>i) & 1 
            if cmp :  # if set 1
                res += curr.children.get(bit,Node()).cnt   # cnt the nums having this bit
                curr = curr.children.get(1-bit,None)   # move to opposite bit
            else: 
                curr = curr.children.get(bit,None)     # move to the same bit
        return res



class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        trie = Trie()
        res = 0
        for num in nums: 
            res += trie.cntSmallXorQuery(num, high+1) - trie.cntSmallXorQuery(num, low)
            trie.insert(num)
        return res