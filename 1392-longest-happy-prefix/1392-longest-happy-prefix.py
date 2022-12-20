class Solution:
    def computeLPSArray(self, pat, M, lps):
        len = 0

        lps[0] = 0
        i = 1

        while i < M:
            if pat[i] == pat[len]:
                len += 1
                lps[i] = len
                i += 1
            else:
                if len != 0:
                    len = lps[len-1]
                else:
                    lps[i] = 0
                    i += 1
    
    def longestPrefix(self, s: str) -> str:
        m = len(s)
        
        pi = [0]*m
        self.computeLPSArray(s, m, pi)
        # i, j = 0, 1
        # while i < m and j < m:
        #     if s[j] == s[i]:
        #         pi[j] = i+1
        #         i += 1
        #     else:
        #         i = 0
        #     j += 1
        # print(pi)
        return "" if not pi[-1] else s[m-pi[-1]:]