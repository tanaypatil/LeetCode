class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        def lcs(text1: str, text2: str) -> int:
            m, n = len(text1), len(text2)
            prev = [0]*(n+1)
            text2 = ' ' + text2

            for i in range(m):
                dp = [0]*(n+1)
                for j in range(1, n+1):
                    dp[j] = max(prev[j], dp[j-1]) if text1[i] != text2[j] else 1 + prev[j-1]
                prev = dp
            return prev[-1]
        
        @lru_cache(None)
        def dp(i, j):
            if i > j: return 0
            if i == j: return 1
            return dp(i+1, j-1) + 2 if s[i] == s[j] else max(dp(i+1, j), dp(i, j-1))
        return dp(0, len(s)-1)
        # return lcs(s, s[::-1])
        