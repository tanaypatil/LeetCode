#User function Template for python3

class Solution:
    def longestCommonSubstr(self, text1, text2, n, m):
        # code here
        m, n = len(text1), len(text2)
        prev = [0]*(m+1)
        text1 = " "+text1
        text2 = " "+text2
        ans = float('-inf')
        for i in range(1, n+1):
            dp = [0]*(m+1)
            for j in range(1, m+1):
                if text1[j] == text2[i]:
                    dp[j] = prev[j-1] + 1
                else:
                    dp[j] = 0
                ans = max(ans, dp[j])    
            prev = dp
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n,m = input().strip().split(" ")
        n,m = int(n), int(m)
        S1 = input().strip()
        S2 = input().strip()
        
        
        ob=Solution()
        print(ob.longestCommonSubstr(S1, S2, n, m))
# } Driver Code Ends