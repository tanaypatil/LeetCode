class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        prev = [0]*(m+1)
        text1 = " "+text1
        for i in range(n):
            dp = [0]*(m+1)
            for j in range(1, m+1):
                if text1[j] == text2[i]:
                    dp[j] = prev[j-1] + 1
                else:
                    dp[j] = max(prev[j], dp[j-1])
            prev = dp
        return prev[-1]
        