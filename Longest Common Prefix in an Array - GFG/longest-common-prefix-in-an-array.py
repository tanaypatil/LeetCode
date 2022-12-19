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
            
    def insert(self, str):
        curr = self.root
        for c in str:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEnd = True
        
    def findPrefix(self):
        curr = self.root
        res = ""
        while len(curr.children) == 1:
            if curr.isEnd:
                break
            c = list(curr.children.keys())[0]
            res += c
            curr = curr.children[c]
        return res


class Solution:
    def longestCommonPrefix(self, arr, n):
        # code here
        trie = Trie()
        trie.insertAll(arr)
        res = trie.findPrefix()
        return res if res else -1
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n = int(input())
        arr = [x for x in input().strip().split(" ")]
        
        ob=Solution()
        print(ob.longestCommonPrefix(arr, n))
# } Driver Code Ends