class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        prev = [j for j in range(m+1)]
        word2 = " " + word2
        word1 = " " + word1
        
        for i in range(1, n+1):
            dp = [0]*(m+1)
            dp[0] = i
            for j in range(1, m+1):
                dp[j] = prev[j-1] if word1[i] == word2[j] else 1 + min(prev[j-1], prev[j], dp[j-1])
            prev = dp
        return prev[-1]
            
        