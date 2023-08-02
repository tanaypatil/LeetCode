class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        
        @lru_cache(None)
        def dfs(i, j, stack):
            if i == len(grid)-1 and j == len(grid[0])-1:
                return len(stack) == 1 and grid[i][j] == ")"
            
            if grid[i][j] == "(":
                for di, dj in [(1, 0), (0, 1)]:
                    r, c = i + di, j + dj
                    if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                        if dfs(r, c, stack+"("): return True
            else:
                if stack:
                    for di, dj in [(1, 0), (0, 1)]:
                        r, c = i + di, j + dj
                        if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                            if dfs(r, c, stack[:-1]): return True
            return False
        
        return dfs(0, 0, "")
        