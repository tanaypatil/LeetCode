class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        prev = [0]*(m+1)
        text2 = ' ' + text2
        for i in range(n):
            dp = [0]*(m+1)
            for j in range(1, m+1):
                dp[j] = 1 + prev[j-1] if text1[i] == text2[j] else max(dp[j-1], prev[j])
            prev = dp
        return prev[-1]
        