class Solution:
    rows = 0
    cols = 0
    
    def isBoundaryCell(self, r, c):
        if c == 0 or c == Solution.cols-1 or r == 0 or r == Solution.rows-1:
            return True
        return False
    
    def numEnclaves(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        Solution.rows, Solution.cols = m, n
        boundary_cells = deque()
        one_cells = 0
        
        visited = defaultdict(bool)
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    if self.isBoundaryCell(i, j):
                        boundary_cells.append((i, j))
                    else:
                        one_cells += 1
        r = [-1, 1, 0, 0]
        c = [0, 0, -1, 1]
        while boundary_cells:
            i, j = boundary_cells.popleft()
            if not self.isBoundaryCell(i, j):
                one_cells -= 1
            visited[(i, j)] = True
            for p in range(4):
                x, y = i + r[p], j + c[p]
                if 0 <= x < m and 0 <= y < n and not visited[(x, y)] and grid[x][y]:
                    boundary_cells.append((x, y))
                    visited[(x, y)] = True
        return one_cells