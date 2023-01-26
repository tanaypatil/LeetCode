class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r, c):
            grid[r][c] = "2"
            
            for dr, dc in steps:
                i, j = r+dr, c+dc
                if 0 <= i < n and 0 <= j < m and grid[i][j] == "1":
                    dfs(i, j)
        
        if not grid:
            return 0
        n, m = len(grid), len(grid[0])
        steps = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        islands = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    islands += 1
                    dfs(i, j)
        return islands