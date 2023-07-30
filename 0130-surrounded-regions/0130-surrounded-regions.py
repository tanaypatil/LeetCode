class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        q = deque()
        
        for r in range(m):
            if board[r][0] == "O":
                q.append((r, 0))
            if board[r][n-1] == "O":
                q.append((r, n-1))
                
        for c in range(n):
            if board[0][c] == "O":
                q.append((0, c))
            if board[m-1][c] == "O":
                q.append((m-1, c))
        
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while q:
            i, j = q.popleft()
            board[i][j] = "C"
            for di, dj in moves:
                r, c = i+di, j+dj
                if 0 <= r < m and 0 <= c < n and board[r][c] == "O":
                    board[r][c] = "C"
                    q.append((r, c))
            
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "C":
                    board[i][j] = "O"
        