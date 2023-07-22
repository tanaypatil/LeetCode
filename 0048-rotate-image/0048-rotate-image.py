class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        max_num = float('-inf')
        min_num = float('inf')
        for i in range(n):
            for j in range(n):
                min_num = min(min_num, matrix[i][j])
                
        if min_num < 0:
            for i in range(n):
                for j in range(n):
                    matrix[i][j] += abs(min_num) + 1
        for i in range(n):
            for j in range(n):
                max_num = max(max_num, matrix[i][j])
        max_num += 1
        
        for i in range(n):
            for j in range(n):
                new_row, new_col = j, n-i-1
                num = matrix[i][j] if matrix[i][j] < max_num else matrix[i][j] // max_num
                matrix[new_row][new_col] = matrix[new_row][new_col] * max_num + num
        for i in range(n):
            for j in range(n):
                matrix[i][j] = matrix[i][j] % max_num
                if min_num < 0:
                    matrix[i][j] -= (abs(min_num)+1)
        