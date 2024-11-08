class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        
        @lru_cache(None)
        def dfs(mask, basket):
            if mask == 0: return (1, 0)
            ans = (float("inf"), float("inf"))
            for j in range(n):
                if mask & (1<<j):
                    pieces, last = dfs(mask - (1 << j), basket)
                    full = (last + jobs[j] > basket)
                    ans = min(ans, (pieces + full, jobs[j] + (1-full)*last))  
            return ans
                    
        
        n = len(jobs)
        l, r = max(jobs), sum(jobs)
        while l < r:
            m = (l+r)//2
            if dfs((1<<n) - 1, m)[0] >= k + 1:
                l = m + 1
            else:
                r = m
        return l
        