#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def perfectSum(self, arr, n, s):
		prev = [0]*(s+1)
        prev[0] = 1
        
        MOD = 10**9+7
        
        for i in range(n):
            dp = [0]*(s+1)
            dp[0] = 1
            for j in range(s+1):
                not_taken = prev[j]
                taken = 0
                if arr[i] <= j:
                    taken = prev[j-arr[i]]
                dp[j] = (taken%MOD + not_taken%MOD)%MOD
            prev = dp
            
        return prev[-1]
    
    
    def countPartitions(self, n, d, arr):
        # Code here
        s = sum(arr)
        if s < d or (s-d)%2:
            return 0
        return self.perfectSum(arr, n, (s-d)//2)

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n, d = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.countPartitions(n, d, arr)
        print(res)
# } Driver Code Ends