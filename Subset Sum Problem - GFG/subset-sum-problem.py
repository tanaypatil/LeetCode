#User function Template for python3

class Solution:
    def isSubsetSum (self, N, arr, s):
        # code here
        prev = [False]*(s+1)
        dp = [False]*(s+1)
        prev[0] = True
        for i in range(N):
            for j in range(s+1):
                if arr[i] > j: continue
                if arr[i] == j or prev[j] or prev[j-arr[i]]:
                    dp[j] = True
            prev = [dp[j] for j in range(s+1)]
            # print(arr[i])
            # print(dp)
            # print("--------------")
            # print()
        return dp[-1]
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        sum = int(input())

        ob = Solution()
        if ob.isSubsetSum(N,arr,sum)==True:
            print(1)
        else :
            print(0)
            
        

# } Driver Code Ends