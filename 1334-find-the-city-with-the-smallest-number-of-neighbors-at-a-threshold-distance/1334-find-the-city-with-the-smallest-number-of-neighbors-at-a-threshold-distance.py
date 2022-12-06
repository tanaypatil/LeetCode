class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        matrix = [[float('inf')]*n for _ in range(n)]
        
        for u, v, w in edges:
            matrix[u][v] = w
            matrix[v][u] = w
            
        for i in range(n):
            matrix[i][i] = 0
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    matrix[i][j] = min(matrix[i][j], matrix[i][k]+matrix[k][j])
        
        m = float('inf')
        ret = -1
        for i in range(n):
            c = 0
            for j in range(n):
                if matrix[i][j] <= distanceThreshold:
                    c += 1
            # print(i, matrix[i], c)
            if c <= m:
                m = c
                ret = i
            
        return ret