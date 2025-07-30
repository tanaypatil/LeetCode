class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        counts = Counter()
        ans = l = 0
        for r in range(len(s)):
            counts[s[r]] += 1
            while counts["a"] and counts["b"] and counts["c"]:
                ans += len(s) - r
                counts[s[l]] -= 1
                l += 1
        return ans
        