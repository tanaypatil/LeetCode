class Solution:
    def minDistance(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        if not m:
            return n
        if not n:
            return m
        prev = [j for j in range(m+1)]
        for i in range(1, n+1):
            dp = [0]*(m+1)
            dp[0] = i
            for j in range(1, m+1):
                if text1[j-1] == text2[i-1]:
                    dp[j] = prev[j-1]
                else:
                    dp[j] = 1+min(prev[j], prev[j-1], dp[j-1])
            prev = dp
        return prev[-1]
        