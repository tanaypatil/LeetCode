class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        @lru_cache(None)
        def dp(i, f):
            ans = 1 if i == finish else 0
            for j in range(len(locations)):
                d = abs(locations[i]-locations[j])
                if i != j and f - d >= 0:
                    ans += dp(j, f - d)
            return ans
        return dp(start, fuel) % (10**9+7)
            