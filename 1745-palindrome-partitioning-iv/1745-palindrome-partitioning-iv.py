class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        
        @lru_cache(None)
        def dfs(i, p):
            if not p and i >= n:
                return True
            
            if not p or i >= n:
                return False
            
            for j in range(i, n):
                if s[i:j+1] == s[i:j+1][::-1]:
                    if dfs(j+1, p-1):
                        return True
                    
            return False
        
        return dfs(0, 3)