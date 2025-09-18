class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, ans, counts, m = 0, 0, Counter(), 0
        for r in range(len(s)):
            counts[s[r]] += 1
            m = max(m, counts[s[r]])
            while (r-l+1) - m > k:
                counts[s[l]] -= 1
                m = max(m, counts[s[r]])
                l += 1
            ans = max(ans, r-l+1)
        return ans