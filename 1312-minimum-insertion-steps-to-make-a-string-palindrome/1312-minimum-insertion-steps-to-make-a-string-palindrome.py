class Solution:
    def minInsertions(self, s: str) -> int:
        text1, text2 = s, s[::-1]
        m, n = len(text1), len(text2)
        prev = [0]*(m+1)
        text1 = " "+text1
        for i in range(n):
            dp = [0]*(m+1)
            for j in range(1, m+1):
                dp[j] = prev[j-1] + 1 if text1[j] == text2[i] else max(prev[j], dp[j-1])
            prev = dp
        return m-prev[-1]
        