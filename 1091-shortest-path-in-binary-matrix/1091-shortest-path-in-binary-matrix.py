class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        if grid[0][0]: return -1
        q = deque({(0, 0)})
        visited = defaultdict(bool)
        r = [-1, -1, -1, 0, 0, 1, 1, 1]
        c = [-1, 0, 1, -1, 1, -1, 0, 1]
        steps = 0
        while q:
            s = len(q)
            for _ in range(s):
                row, col = q.popleft()
                if visited[(row, col)]: continue
                if row == rows-1 and col == cols-1:
                    return steps+1
                visited[(row, col)] = True
                for i in range(8):
                    x, y = r[i] + row, c[i] + col
                    if 0 <= x < rows and 0 <= y < cols and not visited[(x, y)] and not grid[x][y]:
                        q.append((x, y))
            steps += 1   
        return -1
        