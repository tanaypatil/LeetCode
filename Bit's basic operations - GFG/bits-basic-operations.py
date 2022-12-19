#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insertAll(self, strs):
        for str in strs:
            self.insert(str)    
            
    def insert(self, ns, ms):
        curr = self.root
        for n, m in zip():
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEnd = True

class Solution:
    def XOR(self, n, m):
        # Code here
        return n^m
        
    def check(self, a, b):
        # Code here
        v = bin(b)[2:][::-1]
        if len(v) < a:
            return 0
        return 1 if v[a-1] == "1" else 0
        
    def setBit(self, c, d):
        # Code here
        v = bin(d)[2:][::-1]
        if len(v) < c+1:
            return d+2**c
        else:
            if v[c] == "0":
                return d+2**c
            else:
                return d

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n, m = list(map(int, input().split()))
        a, b = list(map(int, input().split()))
        c, d = list(map(int, input().split()))
        ob = Solution()
        ans1 = ob.XOR(n, m)
        ans2 = ob.check(a, b)
        ans3 = ob.setBit(c, d)
        print(ans1, ans2, ans3)
# } Driver Code Ends