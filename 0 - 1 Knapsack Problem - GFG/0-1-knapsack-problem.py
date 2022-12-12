#User function Template for python3

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
       
        # code here
        prev = [0]*(W+1)
        for i in range(wt[0], W+1):
            prev[i] = val[0]
        # print(prev)
            
        for i in range(1, n):
            dp = [0]*(W+1)
            for j in range(1, W+1):
                not_taken = prev[j]
                
                taken = float('-inf')
                
                if wt[i] <= j:
                    taken = val[i] + prev[j-wt[i]]
                
                dp[j] = max(taken, not_taken)
            # print(dp)
                
            prev = dp
            
        return prev[-1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends