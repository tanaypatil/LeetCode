from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        counter = Counter()
        ml = 0
        for r in range(len(s)):
            counter[s[r]] += 1
            while l < r and counter[s[r]] > 1:
                counter[s[l]] -= 1
                l += 1
            ml = max(ml, r-l+1)
        return ml
                
                