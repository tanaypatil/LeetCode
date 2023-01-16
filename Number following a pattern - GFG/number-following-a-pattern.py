#User function Template for python3
from collections import deque


class Solution:
    def printMinNumberForPattern(ob,S):
        # code here 
        stack = deque()
        num = 1
        s = 0
        for c in S:
            stack.append(num)
            num += 1
            if c == "I":
                while stack:
                    s = s*10 + stack.pop()
        stack.append(num)
        num += 1
        while stack:
            s = s*10 + stack.pop()
        return s

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=str(input())

        ob = Solution()
        print(ob.printMinNumberForPattern(S))
# } Driver Code Ends