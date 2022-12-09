#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    mem = {}
    def topDown(self, n):
        mem = Solution.mem
        MOD = 10**9+7
        # Code here
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n in mem:
            return mem[n]
        ans = (self.topDown(n-1)%MOD + self.topDown(n-2)%MOD)%MOD
        mem[n] = ans
        return ans
        
    def bottomUp(self, n):
        MOD = 10**9+7
        # Code here
        if n == 0:
            return 0
        if n == 1:
            return 1
        a, b = 0, 1
        i = 2
        while i <= n:
            t = (a%MOD+b%MOD)%MOD
            a = b
            b = t
            i += 1
        return b

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n = int(input())
        ob = Solution()
        topDownans=ob.topDown(n);
        bottomUpans=ob.bottomUp(n);
        if(topDownans!=bottomUpans):
            print(-1)
        else:
            print(bottomUpans)
# } Driver Code Ends