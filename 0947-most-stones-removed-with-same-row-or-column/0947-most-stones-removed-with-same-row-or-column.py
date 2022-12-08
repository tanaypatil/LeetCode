class Solution:
    def dfs(self, r, c):
        if Solution.visited[(r, c)]:
            return
        Solution.visited[(r, c)] = True
        for x, y in Solution.stones:
            if not Solution.visited[(x, y)] and x == r or y == c:
                self.dfs(x, y)
    
    
    def removeStones(self, stones: List[List[int]]) -> int:
        if not stones:
            return 0
        
        Solution.visited = defaultdict(bool)
        count = 0
        Solution.stones = stones
        for r, c in stones:
            if not Solution.visited[(r, c)]:
                count += 1
                self.dfs(r, c)
        return len(stones)-count