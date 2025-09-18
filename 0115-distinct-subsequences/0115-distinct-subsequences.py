class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        @lru_cache(None)
        def dp(i, curr):
            # print(i, curr)
            if i >= len(s):
                return 1 if curr == t else 0
            
            ans = 0
            if len(s)-i >= len(t)-len(curr):
                ans += dp(i+1, curr)
            
            if len(curr) < len(t) and s[i] == t[len(curr)]:
                ans += dp(i+1, curr+s[i])
                
            return ans
        
        return dp(0, "")
        