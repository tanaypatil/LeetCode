class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        def lcs(str1, str2):
            n, m = len(str1), len(str2)
            prev = [""]*(m+1)
            str2 = " "+str2
            for i in range(n):
                dp = [""]*(m+1)
                for j in range(1, m+1):
                    dp[j] = str1[i] + prev[j-1] if str1[i] == str2[j] else max(prev[j], dp[j-1], key=len)
                prev = dp
            return prev[-1]
        
        res, i, j = "", 0, 0
        lc = lcs(str1, str2)
        # print(lc)
        for c in lc[::-1]:
            while i < len(str1) and str1[i] != c:
                res += str1[i]
                i += 1
            while j < len(str2) and str2[j] != c:
                res += str2[j]
                j += 1
            res += c
            i += 1
            j += 1
        return res + str1[i:] + str2[j:]