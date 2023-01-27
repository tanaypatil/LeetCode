from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0, 0
        if len(s) == 1:
            return 1
        n = len(s)
        m = 0
        counts = defaultdict(int)
        while start < n and end < n:
            while end < n and counts[s[end]] < 1:
                counts[s[end]] += 1
                end += 1
            m = max(m, end-start)
            while start < n and end < n and counts[s[end]] > 0:
                counts[s[start]] -= 1
                start += 1
        return m
                
                