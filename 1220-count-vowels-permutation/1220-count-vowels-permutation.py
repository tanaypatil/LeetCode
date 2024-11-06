class Solution:
    def countVowelPermutation(self, n: int) -> int:
        
        @lru_cache(None)
        def dp(i, last=""):
            if i <= 0:
                return 1
            
            ans = 0
            if not last:
                ans += dp(i-1, "a") + dp(i-1, "e") + dp(i-1, "i") + dp(i-1, "o") + dp(i-1, "u")
            elif last == "a":
                ans += dp(i-1, "e")
            elif last == "e":
                ans += dp(i-1, "a") + dp(i-1, "i")
            elif last == "i":
                ans += dp(i-1, "a") + dp(i-1, "e") + dp(i-1, "o") + dp(i-1, "u")
            elif last == "o":
                ans += dp(i-1, "u") + dp(i-1, "i")
            elif last == "u":
                ans += dp(i-1, "a")
            return ans
        
        
        ans = dp(n) % (10**9+7)
        dp.cache_clear()
        return ans
        