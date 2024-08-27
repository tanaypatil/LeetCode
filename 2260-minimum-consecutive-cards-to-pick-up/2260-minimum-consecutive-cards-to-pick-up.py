class Solution:
    def minimumCardPickup(self, s: List[int]) -> int:
        ans, l = float('inf'), 0
        counts = Counter()
        for r in range(len(s)):
            counts[s[r]] += 1
            while counts[s[r]] > 1:
                ans = min(ans, r-l+1)
                counts[s[l]] -= 1
                l += 1
        return ans if ans != float('inf') else -1
        