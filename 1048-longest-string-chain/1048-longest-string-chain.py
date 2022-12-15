class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def lcs(s1, s2):
            n, m = len(s1), len(s2)
            prev = [0]*(m+1)
            s2 = " " + s2
            for i in range(n):
                dpi = [0]*(m+1)
                for j in range(1, m+1):
                    dpi[j] = 1+prev[j-1] if s1[i] == s2[j] else max(prev[j], dpi[j-1])
                prev = dpi
            return prev[-1]
        
        words.sort(key=len)
        dp = [1]*len(words)
        m = 1
        for i in range(1, len(words)):
            for j in range(i):
                if len(words[i])-len(words[j]) == 1 and dp[i] < 1 + dp[j] and lcs(words[i], words[j]) == len(words[j]):
                    dp[i] = 1+dp[j]
            m = max(m, dp[i])
        return m