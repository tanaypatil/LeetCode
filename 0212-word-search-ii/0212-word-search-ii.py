class Trie:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        
    def insert(self, word):
        curr = self
        for c in word:
            curr = curr.children.setdefault(c, Trie())
        curr.isEnd = True

class Solution:
    def dfs(self, i, j, node, path):
        if not self.numWords:
            return
            
        if node.isEnd:
            self.ret.append(path)
            self.numWords -= 1
            node.isEnd = False
                
        if i < 0 or i >= self.n or j < 0 or j >= self.m:
            return
            
        tmp = self.board[i][j]
        if tmp not in node.children: return
            
        self.board[i][j] = "#"
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            self.dfs(i+di, j+dj, node.children[tmp], path+tmp)
        self.board[i][j] = tmp
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:   
        if not board:
            return []
        
        self.board = board
        self.n, self.m = len(board), len(board[0])
        
        trie = Trie()
        for word in words:
            trie.insert(word)
            
        self.numWords = len(words)
        self.ret = []
        
        for i in range(self.n):
            for j in range(self.m):
                self.dfs(i, j, trie, "")
        return self.ret
                            