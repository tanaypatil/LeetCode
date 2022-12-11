class Solution:
    def dfs(self, m, n, r, c):
        if r == m-1 and c == n-1:
            return Solution.grid[-1][-1]
        if (r, c) in Solution.mem:
            return Solution.mem[(r, c)]
        ans = float('inf')
        for di, dj in Solution.moves:
            i, j = r+di, c+dj
            if 0 <= i < m and 0 <= j < n:
                ans = min(ans, self.dfs(m, n, i, j))
        Solution.mem[(r, c)] = ans + Solution.grid[r][c]
        return ans + Solution.grid[r][c]
        

    def minPathSum(self, grid: List[List[int]]) -> int:
        Solution.grid = grid
        Solution.moves = [(0, 1), (1, 0)]
        Solution.mem = {}
        if not grid:
            return 0
        return self.dfs(len(grid), len(grid[0]), 0, 0)