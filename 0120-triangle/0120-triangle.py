class Solution:
    def dfs(self, m, r, c):
        if r == m-1:
            return Solution.grid[-1][c]
        if (r, c) in Solution.mem:
            return Solution.mem[(r, c)]
        ans = float('inf')
        for di, dj in Solution.moves:
            i, j = r+di, c+dj
            if 0 <= i < m:
                ans = min(ans, self.dfs(m, i, j))
        Solution.mem[(r, c)] = ans + Solution.grid[r][c]
        return ans + Solution.grid[r][c]
    
    
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        Solution.grid = triangle
        Solution.moves = [(1, 1), (1, 0)]
        Solution.mem = {}
        if not triangle:
            return 0
        return self.dfs(len(triangle), 0, 0)
        