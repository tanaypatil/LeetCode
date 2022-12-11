class Solution:
    def dfs(self, m, n, r, c):
        if r == m-1 and c == n-1:
            return 1
        if (r, c) in Solution.mem:
            return Solution.mem[(r, c)]
        ans = 0
        for di, dj in Solution.moves:
            i, j = r+di, c + dj
            if 0 <= i < m and 0 <= j < n and not Solution.grid[i][j]:
                ans += self.dfs(m, n, i, j)
        Solution.mem[(r, c)] = ans
        return ans
    
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0
        Solution.mem = {}
        Solution.grid = obstacleGrid
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        Solution.moves = [(1, 0), (0, 1)]
        if obstacleGrid[0][0]:
            return 0  
        return self.dfs(m, n, 0, 0)
        