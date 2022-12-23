class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = defaultdict(bool)
        cols = defaultdict(bool)
        zeroes = []
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if not matrix[i][j]:
                    zeroes.append((i, j))
                    
        for i, j in zeroes:
            if not rows[i]:
                matrix[i] = [0]*n
                rows[i] = True
            if not cols[j]:
                for k in range(m):
                    matrix[k][j] = 0
                cols[j] = True