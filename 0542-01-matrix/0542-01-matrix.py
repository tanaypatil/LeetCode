from collections import defaultdict, deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat:
            return mat
        m, n = len(mat), len(mat[0])
        ret = [[-1]*n for _ in range(m)]
        r = [-1, 1, 0, 0]
        c = [0, 0, -1, 1]
        
        q = deque()
        
        for i in range(m):
            for j in range(n):
                if not mat[i][j]:
                    q.append((i, j))
        
        visited = defaultdict(bool)
        count = 0
        while q:
            s = len(q)
            for _ in range(s):
                i, j = q.popleft()
                visited[(i, j)] = True
                if mat[i][j]:
                    ret[i][j] = min(ret[i][j], count) if ret[i][j] > 0 else count
                else:
                    ret[i][j] = 0
                for d in range(4):
                    x, y = i + r[d], j + c[d]
                    if 0 <= x < m and 0 <= y < n and not visited[(x, y)] and mat[x][y]:
                        q.append((x, y))
            count += 1
        return ret
            