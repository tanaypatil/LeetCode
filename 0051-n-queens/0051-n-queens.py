class Solution:
    board = []
    ret = []
    
    def is_valid(self, n, curr_row, col):
        board = Solution.board
        for c in range(n):
            if c != col and board[curr_row][c] == "Q":
                return False
        for r in range(n):
            if r != curr_row and board[r][col] == "Q":
                return False
        d = curr_row-col
        for i in range(n):
            r = d + i
            if 0 <= r < n and (r, i) != (curr_row, col) and board[r][i] == "Q":
                return False
        d = curr_row+col
        for i in range(n):
            r = d-i
            if 0 <= r < n and (r, i) != (curr_row, col) and board[r][i] == "Q":
                return False
        return True
    
    def solve(self, n, curr_row):
        if curr_row >= n:
            c = []
            for i in range(n):
                c.append(''.join(Solution.board[i]))
            Solution.ret.append(c)
            return True
        for i in range(n):
            if self.is_valid(n, curr_row, i):
                Solution.board[curr_row][i] = "Q"
                self.solve(n, curr_row+1)
                Solution.board[curr_row][i] = "."
    
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        Solution.ret = []
        Solution.board = [["."]*n for i in range(n)]
        self.solve(n, 0)
        return Solution.ret
        
        