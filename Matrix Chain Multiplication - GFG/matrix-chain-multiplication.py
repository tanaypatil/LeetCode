#User function Template for python3

class Solution:
    def matrixMultiplication(self, N, arr):
        # code here
        dp = [[0]*N for _ in range(N)]
        
        for l in range(2, N):
            for i in range(N-l):
                j = i + l
                dp[i][j] = float('inf')
                for k in range(i+1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j]+arr[i]*arr[k]*arr[j])
                    
        return dp[0][-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.matrixMultiplication(N, arr))
# } Driver Code Ends