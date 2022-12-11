class Solution:
    def dfs(self, m, r, c):
        if r == m-1:
            return Solution.grid[-1][c]
        if (r, c) in Solution.mem:
            return Solution.mem[(r, c)]
        ans = float('inf')
        for di, dj in Solution.moves:
            i, j = r+di, c+dj
            if 0 <= i < m and 0 <= j < m:
                ans = min(ans, self.dfs(m, i, j))
        Solution.mem[(r, c)] = ans + Solution.grid[r][c]
        return ans + Solution.grid[r][c]
    
    
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        Solution.grid = grid
        Solution.moves = [(1, -1), (1, 0), (1, 1)]
        Solution.mem = {}
        if not grid:
            return 0
        ans = float('inf')
        for i in range(len(grid)):
            ans = min(ans, self.dfs(len(grid), 0, i))
        return ans
        