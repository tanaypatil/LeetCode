class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        n = len(hats)
        people = defaultdict(list)
        for i in range(n):
            for hat in hats[i]:
                people[hat-1].append(i)
        MOD = 10**9+7
        if n > 41: return 0
        
        @lru_cache(None)
        def dp(i, mask):
            if mask == (1<<n)-1: return 1
            if i == 40: return 0
            cur = dp(i+1, mask)
            for j in people[i]:
                if not (mask & (1 << j)):
                    cur += dp(i+1, mask|1<<j)
            return cur%MOD
        return dp(0, 0)
        