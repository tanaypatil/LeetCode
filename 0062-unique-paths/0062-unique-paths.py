class Solution:
    def dfs(self, m, n, r, c):
        if r == m-1 and c == n-1:
            return 1
        if (r, c) in Solution.mem:
            return Solution.mem[(r, c)]
        ans = 0
        for di, dj in Solution.moves:
            i, j = r+di, c + dj
            if 0 <= i < m and 0 <= j < n:
                ans += self.dfs(m, n, i, j)
        Solution.mem[(r, c)] = ans
        return ans
        
    def uniquePaths(self, m: int, n: int) -> int:
        Solution.mem = {}
        Solution.moves = [(1, 0), (0, 1)]
        return self.dfs(m, n, 0, 0)
        
            