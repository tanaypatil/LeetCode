class Solution:
    glob_memo = {}
    
    def find(self, board, n, m, row, col, path, word, memo):
        if path == word:
            return True
        memo[(row, col)] = True
        x = [-1, 0, 1, 0]
        y = [0, 1, 0, -1]
        for r, c in zip(y, x):
            nr, nc = row+r, col+c
            if 0 <= nr < n and 0 <= nc < m and not memo[(nr, nc)] and path+board[nr][nc] == word[:len(path)+1]:
                if self.find(board, n, m, nr, nc, path+board[nr][nc], word, memo):
                    return True
        memo[(row, col)] = False
        return False
        
    def exist(self, board: List[List[str]], word: str) -> bool:
        Solution.glob_memo = {}
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.find(board, len(board), len(board[0]), i, j, board[i][j], word, defaultdict(bool)):
                        return True
        return False