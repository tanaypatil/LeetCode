#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
from bisect import bisect_left
class Solution:
    def longestIncreasingSubsequence(self, N, nums):
        # Code here
        fr = [-1]*N
        dp = [1]*N
        mi = 0
        ml = 1
        for i in range(1, N):
            for j in range(i):
                if nums[i] > nums[j] and dp[i] < 1+dp[j]:
                    dp[i] = 1+dp[j]
                    fr[i] = j
            if dp[i] > ml:
                ml = dp[i]
                mi = i
        res = []
        # print(mi, ml)
        # print(dp)
        # print(fr)
        while mi != -1:
            res.append(nums[mi])
            mi = fr[mi]
        
        return res[::-1]

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.longestIncreasingSubsequence(N, arr)
        for val in res:
            print(val, end =' ')
        print()
# } Driver Code Ends