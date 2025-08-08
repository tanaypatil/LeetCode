class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        
        @lru_cache(None)
        def isPalindrome(l, r):  # l, r inclusive
            if l >= r: return True
            if s[l] != s[r]: return False
            return isPalindrome(l+1, r-1)
        
        @lru_cache(None)
        def dfs(i):
            if i >= n:
                return 0
            ans = float('inf')
            for j in range(i, n):
                if isPalindrome(i, j):
                    ans = min(ans, 1 + dfs(j+1))
            
            return ans
        
        return dfs(0) - 1
        