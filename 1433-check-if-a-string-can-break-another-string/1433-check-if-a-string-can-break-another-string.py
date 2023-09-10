class Solution:
    def check(self, s1, s2):
        n = len(s1)
        s1 = sorted(s1)
        s2 = sorted(s2)
        
        for c1, c2 in zip(s1, s2):
            if c1 < c2:
                return False
        return True
        
#         @lru_cache(None)
#         def dfs(i, j):
#             if i >= n:
#                 return True
            
#             if j >= n:
#                 return False
            
#             for k in range(j, n):
#                 if s2[k] >= s1[i]:
#                     if dfs(i+1, k+1):
#                         return True
#             return False
        
#         return dfs(0, 0)
    
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        return self.check(s1, s2) or self.check(s2, s1)