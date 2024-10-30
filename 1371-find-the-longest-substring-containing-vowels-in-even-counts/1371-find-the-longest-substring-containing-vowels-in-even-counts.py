class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        hm, res, m = {0: -1}, 0, 0
        for i, c in enumerate(s):
            m ^= (c in "aeiou")*ord(c)
            res = max(res, i-hm.setdefault(m, i))
        return res
            
        