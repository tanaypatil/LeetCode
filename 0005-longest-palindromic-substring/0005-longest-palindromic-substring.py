class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        mat = [[0]*n for i in range(n)]
        for i in range(n):
            mat[i][i] = 1
        m = 1
        ans = s[0]
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j] and i+1 < n and j-1 > -1:
                    mat[i][j] = mat[i+1][j-1] + 2 if mat[i+1][j-1] > 0 or abs(i-j) == 1 else 0
                    if mat[i][j] > m:
                        ans = s[i:j+1]
                        m = mat[i][j]
        return ans
        