class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        prev = [0]*(n+1)
        text2 = " " + text2
        for i in range(m):
            dp = [0]*(n+1)
            for j in range(1, n+1):
                if text1[i] == text2[j]:
                    dp[j] = 1 + prev[j-1]
                else:
                    dp[j] = max(dp[j-1], prev[j-1], prev[j])
            prev = dp
        return prev[-1]
        