#User function Template for python3

class Solution:
    def knapSack(self, N, W, val, wt):
        # code here
        dp = [0]*(W+1)
        
        # for i in range(1, W+1):
        #     if not (i % wt[0]):
        #         dp[i] = val[0] * (i//wt[0])
        
        for i in range(N):
            for j in range(W+1):
                not_taken = dp[j]
                taken = float('-inf')
                if j >= wt[i]:
                    taken = val[i] + dp[j-wt[i]]
                dp[j] = max(taken, not_taken)
        
        return dp[-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, W = [int(x) for x in input().split()]
        val = input().split()
        for itr in range(N):
            val[itr] = int(val[itr])
        wt = input().split()
        for it in range(N):
            wt[it] = int(wt[it])
        
        ob = Solution()
        print(ob.knapSack(N, W, val, wt))
# } Driver Code Ends