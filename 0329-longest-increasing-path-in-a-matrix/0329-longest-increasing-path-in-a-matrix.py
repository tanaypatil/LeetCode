class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(matrix), len(matrix[0])
        visited = defaultdict(bool)
        
        @lru_cache(None)
        def dfs(i, j):
            visited[(i, j)] = True
            path_len = 0
            for di, dj in moves:
                r, c = i+di, j+dj
                if 0 <= r < m and 0 <= c < n and not visited[(r, c)] and matrix[r][c] > matrix[i][j]:
                    path_len = max(dfs(r, c), path_len)     
            visited[(i, j)] = False
            return 1+path_len
        
        ans = 1
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))
        return ans