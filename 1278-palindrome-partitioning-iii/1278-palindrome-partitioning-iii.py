class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        
        @lru_cache(None)
        def cost(i, j):
            ret = 0
            while i < j:
                if s[i] != s[j]:
                    ret += 1
                i += 1
                j -= 1
            return ret
        
        @lru_cache(None)
        def dp(i, k):
            if n - i == k:
                return 0
            
            if k == 1:
                return cost(i, n-1)
            
            ans = float('inf')
            for j in range(i+1, n-k+2):
                ans = min(ans, dp(j, k-1) + cost(i, j-1))
            return ans
        
        return dp(0, k)