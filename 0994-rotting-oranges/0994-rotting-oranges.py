from collections import deque, defaultdict


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        minutes = -1
        mem = defaultdict(int)
        while queue:
            l = len(queue)
            for i in range(l):
                row, col = queue.popleft()
                r = [-1, 1, 0, 0]
                c = [0, 0, -1, 1]
                for p in range(4):
                    a, b = row + r[p], col + c[p]
                    # print(a, b, 0 <= a < rows, 0 <= b <= cols)
                    if 0 <= a < rows and 0 <= b < cols and grid[a][b] == 1 and not mem[(a, b)]:
                        queue.append((a, b))
                        fresh -= 1
                        mem[(a, b)] = 1
            minutes += 1
            
        return (minutes if minutes > 0 else 0) if not fresh else -1
                