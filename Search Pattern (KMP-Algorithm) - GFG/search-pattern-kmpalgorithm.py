#User function Template for python3

class Solution:
    def search(self, pat, txt):
        # code here
        indexes = []
        for i, c in enumerate(s):
            if c == patt[0] and s[i:i+len(patt)] == patt:
                indexes.append(i+1)
        return indexes if indexes else [-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        patt = input().strip()
        ob = Solution()
        ans = ob.search(patt, s)
        if len(ans)==0:
            print(-1,end="")
        for value in ans:
            print(value,end = ' ')
        print()
# } Driver Code Ends