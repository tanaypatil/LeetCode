class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        mat = [[0]*n for _ in range(n)]
        c = 0
        for i in range(n):
            mat[i][i] = 1
            c += 1
            
        for l in range(2, n+1):
            for i in range(n-1):
                j = i + l - 1
                if 0 <= i < n and 0 <= j < n and s[i] == s[j] and (mat[i+1][j-1] or abs(i-j) == 1):
                    mat[i][j] += mat[i+1][j-1] + 2
                    if mat[i][j]:
                        # print(i, j)
                        c += 1
        return c
                
        